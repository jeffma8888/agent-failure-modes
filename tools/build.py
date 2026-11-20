#!/usr/bin/env python3
"""Generate the knowledge base from the structured corpus in tools/corpus.py.

Everything human-readable here is DERIVED. The corpus is the single source of
truth, so the incident pages, the machine-readable index, the catalog tree, the
taxonomy and the README / AGENTS.md regions cannot drift apart. Regenerate with:

    python3 tools/build.py

The catalog is a progressive-disclosure tree an agent can walk without loading
the whole corpus:  catalog/README.md (root router) -> catalog/{class}/README.md
(class node) -> catalog/{class}/{slug}.md (topic leaf) -> incidents/*.md. Every
node is budgeted (NODE_BUDGET) so it can be read whole; catalog/CORE.md is the
prompt-sized payload (CORE_BUDGET).

Rendering is pure: `render(Model(...))` returns {path: text} without touching
disk, so tests can build fixture corpora and inspect the output.
"""
from __future__ import annotations
import datetime, json, os, posixpath, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import INCIDENTS, CLASSES, PRACTICES, TOPICS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["id", "title", "date", "classes", "severity", "status", "cost",
            "signature", "what", "root_cause", "why_hard", "fix", "verification", "rule"]
OPTIONAL = ["related", "evidence", "topic", "recurrence_of", "recurrences"]
SEVERITIES = {"low", "medium", "high", "critical"}
STATUSES = {"fixed", "mitigated", "open", "structural"}
SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

FLAT_MAX = 22            # authoring rule: a class with <= this many home incidents has no topics
MAX_OUTLIERS = 3         # a class with topics may keep this many home incidents at class level
RULE_MAX = 400
ROUTE_MAX = 160
NOTE_MAX = 300
SLUG_MAX = 40
TOPIC_LIMITS = {"title": 70, "go_here_if": 200, "rule": 400}
CLASS_FIELDS = {"what", "ask", "route"}
RECURRENCE_FIELDS = {"date", "note", "evidence"}
NODE_BUDGET = 12 * 1024   # bytes, every catalog node (~3K tokens)
CORE_BUDGET = 16 * 1024   # bytes, catalog/CORE.md
AGENTS_BUDGET = 8 * 1024  # bytes, AGENTS.md
ROOT_TOP = 10             # most-recurrent rows on the root router
ROOT_AREAS = 10           # largest-area rows on the root router
CORE_MAX_RULES = 25       # most-recurrent incident rules in CORE.md (budget permitting)
CORE_MIN_RECURRENT = 10   # of those, reserved before topic rules compete for the budget
JSON_TOP = 50             # most-recurrent ids in data/catalog.json

ID_RE = re.compile(r"^INC-\d{4}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
NL = chr(10)


def slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60].rstrip("-")


def filename(inc: dict) -> str:
    return f"{inc['id']}-{slug(inc['title'])}.md"


def _iso(s) -> bool:
    if not isinstance(s, str) or not DATE_RE.match(s):
        return False
    try:
        datetime.date.fromisoformat(s)
    except ValueError:
        return False
    return True


def _home(inc: dict):
    cls = inc.get("classes")
    return cls[0] if isinstance(cls, list) and cls else None


def _placement(inc: dict) -> tuple:
    return (_home(inc), inc.get("topic"))


# --------------------------------------------------------------------------- validation

def validate(incidents=None, classes=None, topics=None, practices=None) -> list[str]:
    """Every rule the corpus must satisfy. Pure: pass fixtures to test it."""
    incidents = INCIDENTS if incidents is None else incidents
    classes = CLASSES if classes is None else classes
    topics = TOPICS if topics is None else topics
    practices = PRACTICES if practices is None else practices
    errs: list[str] = []

    for cid, meta in classes.items():
        for f in ("what", "ask"):
            if not isinstance(meta.get(f), str) or not meta[f].strip():
                errs.append(f"class {cid}: missing '{f}'")
        if "route" in meta:
            r = meta["route"]
            if not isinstance(r, str) or not r.strip():
                errs.append(f"class {cid}: route must be a non-empty string")
            elif len(r) > ROUTE_MAX:
                errs.append(f"class {cid}: route is {len(r)} chars > {ROUTE_MAX}")
        if extra := sorted(set(meta) - CLASS_FIELDS):
            errs.append(f"class {cid}: unknown field(s) {extra}")

    for key, meta in topics.items():
        cls, _, sl = key.partition("/")
        if cls not in classes:
            errs.append(f"topic {key}: class '{cls}' is not in CLASSES")
        if not SLUG_RE.match(sl) or len(sl) > SLUG_MAX:
            errs.append(f"topic {key}: slug must be kebab-case and at most {SLUG_MAX} chars")
        if not isinstance(meta, dict):
            errs.append(f"topic {key}: must be a dict of {sorted(TOPIC_LIMITS)}")
            continue
        for f, lim in TOPIC_LIMITS.items():
            v = meta.get(f)
            if not isinstance(v, str) or not v.strip():
                errs.append(f"topic {key}: missing '{f}'")
            elif len(v) > lim:
                errs.append(f"topic {key}: {f} is {len(v)} chars > {lim}")
        if extra := sorted(set(meta) - set(TOPIC_LIMITS)):
            errs.append(f"topic {key}: unknown field(s) {extra}")

    seen: set = set()
    allowed = set(REQUIRED) | set(OPTIONAL)
    for inc in incidents:
        i = inc.get("id", "<no id>")
        for f in REQUIRED:
            if not inc.get(f):
                errs.append(f"{i}: missing required field '{f}'")
        if extra := sorted(set(inc) - allowed):
            errs.append(f"{i}: unknown field(s) {extra}; optional fields are {OPTIONAL}")
        if not isinstance(i, str) or not ID_RE.match(i):
            errs.append(f"{i}: id must look like INC-0001")
        if i in seen:
            errs.append(f"{i}: duplicate id")
        seen.add(i)
        if inc.get("date") and not _iso(inc.get("date")):
            errs.append(f"{i}: date {inc.get('date')!r} is not ISO YYYY-MM-DD")
        if inc.get("severity") not in SEVERITIES:
            errs.append(f"{i}: severity '{inc.get('severity')}' not in {sorted(SEVERITIES)}")
        if inc.get("status") not in STATUSES:
            errs.append(f"{i}: status '{inc.get('status')}' not in {sorted(STATUSES)}")
        for c in inc.get("classes") or []:
            if c not in classes:
                errs.append(f"{i}: unknown class '{c}'")
        if len(inc.get("rule") or "") > RULE_MAX:
            errs.append(f"{i}: rule is {len(inc['rule'])} chars; keep it under {RULE_MAX} so it fits a prompt")
        t = inc.get("topic")
        if t is not None:
            if not isinstance(t, str) or t not in topics:
                errs.append(f"{i}: topic {t!r} is not registered in TOPICS")
            elif t.split("/", 1)[0] != _home(inc):
                errs.append(f"{i}: topic '{t}' belongs to class '{t.split('/', 1)[0]}' "
                            f"but the home class (classes[0]) is '{_home(inc)}'")
        if "recurrences" in inc:
            rs = inc["recurrences"]
            if not isinstance(rs, list):
                errs.append(f"{i}: recurrences must be a list of {{date, note, evidence?}}")
                rs = []
            for n, r in enumerate(rs, 1):
                w = f"{i}: recurrences[{n}]"
                if not isinstance(r, dict):
                    errs.append(f"{w} must be a dict")
                    continue
                if extra := sorted(set(r) - RECURRENCE_FIELDS):
                    errs.append(f"{w}: unknown field(s) {extra}")
                if not _iso(r.get("date")):
                    errs.append(f"{w}: date {r.get('date')!r} is not a valid ISO YYYY-MM-DD date")
                elif _iso(inc.get("date")) and r["date"] < inc["date"]:
                    errs.append(f"{w}: date {r['date']} precedes the incident's own date {inc['date']}")
                note = r.get("note")
                if not isinstance(note, str) or not note.strip():
                    errs.append(f"{w}: missing note")
                elif len(note) > NOTE_MAX:
                    errs.append(f"{w}: note is {len(note)} chars > {NOTE_MAX}")
                if "evidence" in r and (not isinstance(r["evidence"], list) or not all(
                        isinstance(e, str) and e.strip() for e in r["evidence"])):
                    errs.append(f"{w}: evidence must be a list of non-empty strings")

    byid = {inc.get("id"): inc for inc in incidents}
    for inc in incidents:
        i = inc.get("id", "<no id>")
        for r in inc.get("related", []):
            if r not in byid:
                errs.append(f"{i}: related id '{r}' does not exist")
        if "recurrence_of" not in inc:
            continue
        a = inc["recurrence_of"]
        if not isinstance(a, str) or a not in byid:
            errs.append(f"{i}: recurrence_of {a!r} does not exist")
            continue
        if a == i:
            errs.append(f"{i}: recurrence_of points at itself")
            continue
        if not a < i:
            errs.append(f"{i}: recurrence_of {a} must point at an EARLIER (lower) id")
        if byid[a].get("recurrence_of"):
            errs.append(f"{i}: recurrence_of {a}, which is itself a recurrence of "
                        f"{byid[a]['recurrence_of']}; point at the canonical directly (no chains)")
        if _placement(inc) != _placement(byid[a]):
            errs.append(f"{i}: recurrence_of {a} must share its home class and topic "
                        f"({_placement(inc)} vs {_placement(byid[a])})")

    carried = defaultdict(int)
    for inc in incidents:
        if isinstance(inc.get("topic"), str):
            carried[inc["topic"]] += 1
    for key in topics:
        if not carried[key]:
            errs.append(f"topic {key}: registered but no incident carries it")
    topic_classes = {k.split("/", 1)[0] for k in topics}
    for cid in classes:
        if cid not in topic_classes:
            continue
        n_home = sum(1 for inc in incidents if _home(inc) == cid)
        if n_home <= FLAT_MAX:
            errs.append(f"class {cid}: has topics but only {n_home} home incidents; a class with "
                        f"{FLAT_MAX} or fewer has none (its class node is the leaf)")
        loose = sorted(inc.get("id", "?") for inc in incidents
                       if _home(inc) == cid and not inc.get("topic"))
        if len(loose) > MAX_OUTLIERS:
            errs.append(f"class {cid}: has topics, so every home incident needs a topic except at most "
                        f"{MAX_OUTLIERS} class-level outliers; {len(loose)} have none: {loose[:8]}")

    for pra in practices:
        for ref in pra.get("derived_from", []):
            if ref not in byid:
                errs.append(f"{pra.get('id')}: derived_from cites unknown incident {ref}")
    return errs


# --------------------------------------------------------------------------- model

class Model:
    """The validated corpus plus everything derived from it (placement, counts)."""

    def __init__(self, incidents, classes, topics, practices):
        self.incidents = sorted(incidents, key=lambda x: x["id"])
        self.classes, self.topics = classes, topics
        self.practices = sorted(practices, key=lambda x: x["id"])
        self.byid = {i["id"]: i for i in self.incidents}
        self.stubs: dict[str, list] = defaultdict(list)
        for inc in self.incidents:
            if inc.get("recurrence_of"):
                self.stubs[inc["recurrence_of"]].append(inc)
        self.occ = {}
        for inc in self.incidents:
            own = 1 + len(inc.get("recurrences", []))
            if not inc.get("recurrence_of"):
                own += sum(1 + len(s.get("recurrences", [])) for s in self.stubs[inc["id"]])
            self.occ[inc["id"]] = own
        self.class_topics = {c: sorted(k for k in topics if k.split("/", 1)[0] == c) for c in classes}
        self.topic_members = {k: [] for k in sorted(topics)}
        self.class_level = {c: [] for c in classes}
        self.home = {c: [] for c in classes}
        self.also = {c: [] for c in classes}
        for inc in self.incidents:
            h = inc["classes"][0]
            self.home[h].append(inc)
            (self.topic_members[inc["topic"]] if inc.get("topic") else self.class_level[h]).append(inc)
            for c in dict.fromkeys(inc["classes"][1:]):
                if c != h:
                    self.also[c].append(inc)

    def rank_key(self, inc):
        return (-self.occ[inc["id"]], SEV_ORDER[inc["severity"]], inc["id"])

    def canonicals(self, incs):
        return sorted((i for i in incs if not i.get("recurrence_of")), key=self.rank_key)

    def most_recurrent(self, n=None):
        ranked = self.canonicals(self.incidents)
        return ranked if n is None else ranked[:n]

    def area_occ(self, incs) -> int:
        return sum(self.occ[i["id"]] for i in incs if not i.get("recurrence_of"))

    def total_occ(self) -> int:
        return self.area_occ(self.incidents)

    def n_stubs(self) -> int:
        return sum(1 for i in self.incidents if i.get("recurrence_of"))

    def n_entries(self) -> int:
        return sum(len(i.get("recurrences", [])) for i in self.incidents)

    def max_occ(self) -> int:
        return max(self.occ.values(), default=0)

    def has_topics(self, c) -> bool:
        return bool(self.class_topics[c])

    def route(self, c) -> str:
        meta = self.classes[c]
        if meta.get("route"):
            return meta["route"]
        return re.split(r"(?<=[.!?])\s+", meta["what"].strip(), maxsplit=1)[0]

    def practices_touching(self, c):
        return [p for p in self.practices
                if any(c in self.byid[r]["classes"] for r in p["derived_from"] if r in self.byid)]

    @staticmethod
    def class_node(c) -> str:
        return f"catalog/{c}/README.md"

    @staticmethod
    def topic_node(key) -> str:
        c, s = key.split("/", 1)
        return f"catalog/{c}/{s}.md"

    def node_of(self, inc) -> str:
        return self.topic_node(inc["topic"]) if inc.get("topic") else self.class_node(inc["classes"][0])

    def where(self, inc) -> str:
        return inc.get("topic") or inc["classes"][0]

    def page(self, inc) -> str:
        return f"incidents/{filename(inc)}"


def rel(target: str, from_dir: str) -> str:
    return posixpath.relpath(target, from_dir or ".")


def cell(s: str) -> str:
    return s.replace("|", "\\|").replace(NL, " ")


def nbytes(s: str) -> int:
    return len(s.encode("utf-8"))


# --------------------------------------------------------------------------- incident pages

def incident_page(inc: dict, m: Model) -> str:
    c = inc["classes"][0]
    crumbs = ["[root](../catalog/README.md)", f"[{c}](../{m.class_node(c)})"]
    if inc.get("topic"):
        crumbs.append(f"[{m.topics[inc['topic']]['title']}](../{m.topic_node(inc['topic'])})")
    out = [
        "---",
        f"id: {inc['id']}",
        f"title: {inc['title']}",
        f"date: {inc['date']}",
        f"classes: [{', '.join(inc['classes'])}]",
        f"severity: {inc['severity']}",
        f"status: {inc['status']}",
        f"topic: {inc.get('topic') or 'null'}",
        f"occurrences: {m.occ[inc['id']]}",
    ]
    if inc.get("recurrence_of"):
        out.append(f"recurrence_of: {inc['recurrence_of']}")
    out += [
        "---",
        "",
        f"# {inc['id']} - {inc['title']}",
        "",
        "**Catalog:** " + " / ".join(crumbs),
        "",
    ]
    if inc.get("recurrence_of"):
        a = m.byid[inc["recurrence_of"]]
        out += [f"> **Recurrence of [{a['id']}](./{filename(a)}).** This record repeats an earlier "
                f"failure and is kept for history; {a['id']} is the canonical record "
                f"({m.occ[a['id']]} occurrences in total) and carries the rule to apply.", ""]
    out += [
        f"**Cost:** {inc['cost']}",
        "",
        "## Signature - how you recognise it",
        "",
        inc["signature"],
        "",
        "## What happened",
        "",
        inc["what"],
        "",
        "## Root cause",
        "",
        inc["root_cause"],
        "",
        "## Why it was hard to see",
        "",
        inc["why_hard"],
        "",
        "## Fix",
        "",
        inc["fix"],
        "",
        "## Verification",
        "",
        inc["verification"],
        "",
        "## Transferable rule",
        "",
        f"> {inc['rule']}",
        "",
    ]
    stubs = m.stubs.get(inc["id"], [])
    entries = sorted(inc.get("recurrences", []), key=lambda r: (r["date"], r["note"]))
    if stubs or entries:
        out += ["## Recurrences", "",
                f"Occurrences: {m.occ[inc['id']]}. Repeats of this failure are recorded here "
                "instead of as new incidents.", ""]
        out += [f"- [{s['id']}](./{filename(s)}) - {s['date']} - {s['title']}" for s in stubs]
        for r in entries:
            out.append(f"- {r['date']} - {r['note']}")
            out += [f"  - {e}" for e in r.get("evidence", [])]
        out.append("")
    if inc.get("evidence"):
        out += ["## Provenance", "",
                "Where this was observed, so the claim is checkable rather than anecdotal:", ""]
        out += [f"- {e}" for e in inc["evidence"]]
        out += [""]
    if inc.get("related"):
        out += ["## Related", "", " ".join(f"[{r}](./{filename(m.byid[r])})" for r in inc["related"]), ""]
    return NL.join(out)


# --------------------------------------------------------------------------- catalog nodes

def _full_entry(inc, m: Model, d: str) -> list[str]:
    out = [f"### [{inc['id']}]({rel(m.page(inc), d)}) - {inc['title']}",
           f"- occurrences {m.occ[inc['id']]}, severity {inc['severity']}, status {inc['status']}",
           f"- **Signature:** {inc['signature']}",
           f"- **Rule:** {inc['rule']}"]
    stubs = m.stubs.get(inc["id"], [])
    entries = sorted(inc.get("recurrences", []), key=lambda r: (r["date"], r["note"]))
    if stubs or entries:
        out.append("- **Recurrences:**")
        out += [f"  - [{s['id']}]({rel(m.page(s), d)}) - {s['date']} - {s['title']}" for s in stubs]
        out += [f"  - {r['date']} - {r['note']}" for r in entries]
    return out + [""]


def _short_entry(inc, m: Model, d: str) -> list[str]:
    out = [f"- [{inc['id']}]({rel(m.page(inc), d)}) - {inc['title']} "
           f"(n={m.occ[inc['id']]}, {inc['severity']})"]
    stubs = m.stubs.get(inc["id"], [])
    n_ent = len(inc.get("recurrences", []))
    if stubs or n_ent:
        links = ", ".join(f"[{s['id']}]({rel(m.page(s), d)})" for s in stubs)
        more = f"{n_ent} recorded repeat(s)" if n_ent else ""
        out.append("  - recurrences: " + ", ".join(x for x in (links, more) if x))
    return out


def fit_entries(head: list[str], incs: list, tail: list[str], m: Model, d: str,
                budget: int = NODE_BUDGET) -> tuple[str, int]:
    """Render as many FULL entries (ranked order) as fit the budget, the rest as one-liners.

    Every incident stays linked whatever happens, so reachability never depends on
    the budget. Returns (text, number of full entries)."""
    fulls = [_full_entry(i, m, d) for i in incs]
    shorts = [_short_entry(i, m, d) for i in incs]
    n = len(incs)
    text = ""
    for k in range(n, -1, -1):
        body: list[str] = []
        for f in fulls[:k]:
            body += f
        if k < n:
            body += [f"The {n - k} entries below are listed by title only so this node stays under "
                     f"{budget // 1024} KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, "
                     "for its signature and rule.", ""]
            for s in shorts[k:]:
                body += s
            body.append("")
        text = NL.join(head + body + tail)
        if nbytes(text) <= budget:
            return text, k
    return text, 0


def _also_tagged(c: str, m: Model, d: str) -> list[str]:
    also = m.also[c]
    if not also:
        return []
    groups: dict[str, list] = defaultdict(list)
    for inc in also:
        groups[m.node_of(inc)].append(inc)
    out = [f"## Also tagged {c}", "",
           f"{len(also)} incidents filed under another home class also carry this class. "
           "Listed by the node where they live:", ""]
    for node in sorted(groups, key=lambda n: (-len(groups[n]), n)):
        incs = groups[node]
        label = m.where(incs[0])
        out.append(f"- [{label}]({rel(node, d)}): " + ", ".join(i["id"] for i in incs))
    return out + [""]


def _practices_block(c: str, m: Model, d: str) -> list[str]:
    ps = m.practices_touching(c)
    if not ps:
        return []
    out = ["## Practices touching this class", ""]
    out += [f"- [{p['id']}]({rel('catalog/CORE.md', d)}#practices) - {p['title']}" for p in ps]
    return out + [""]


def class_node(c: str, m: Model) -> str:
    d = f"catalog/{c}"
    meta = m.classes[c]
    home, also = m.home[c], m.also[c]
    head = [f"# {c}", "",
            f"[Catalog](../README.md) / {c}", "",
            meta["what"], "",
            f"**Ask:** {meta['ask']}", ""]
    if meta.get("route"):
        head += [f"**You are probably here if:** {meta['route']}", ""]
    head += [f"{len(home)} incidents filed here ({m.area_occ(home)} occurrences); "
            f"{len(also)} more filed elsewhere are also tagged {c}.", ""]
    if m.has_topics(c):
        head += ["## Topics", "",
                 "n = occurrences: incidents filed in the topic plus their recorded repeats.", "",
                 "| Topic | Go here if | n | Link |", "|---|---|---|---|"]
        rows = sorted(m.class_topics[c], key=lambda k: (-m.area_occ(m.topic_members[k]), k))
        for k in rows:
            t = m.topics[k]
            head.append(f"| {cell(t['title'])} | {cell(t['go_here_if'])} | "
                        f"{m.area_occ(m.topic_members[k])} | [{k.split('/', 1)[1]}]({rel(m.topic_node(k), d)}) |")
        head.append("")
        loose = m.canonicals(m.class_level[c])
        if loose:
            head += ["## Class-level incidents", "",
                     "Filed in this class but in none of its topics.", ""]
    else:
        loose = m.canonicals(m.class_level[c])
        head += ["## Incidents", "",
                 "This class has no topics, so this node is the leaf. Ordered by occurrences, "
                 "then severity, then id.", ""]
    tail = _also_tagged(c, m, d) + _practices_block(c, m, d)
    text, _ = fit_entries(head, loose, tail, m, d)
    return text


def topic_leaf(key: str, m: Model) -> str:
    c, s = key.split("/", 1)
    d = f"catalog/{c}"
    t = m.topics[key]
    members = m.topic_members[key]
    head = [f"# {t['title']}", "",
            f"[Catalog](../README.md) / [{c}](README.md) / {s}", "",
            f"**Go here if:** {t['go_here_if']}", "",
            f"**Rule:** {t['rule']}", "",
            f"{len(members)} incidents, {m.area_occ(members)} occurrences. "
            "Ordered by occurrences, then severity, then id.", "",
            "## Incidents", ""]
    text, _ = fit_entries(head, m.canonicals(members), [], m, d)
    return text


def _recurrence_note(m: Model) -> str:
    if m.max_occ() <= 1:
        return ("No repeats are recorded yet, so every failure has occurred once and this list falls "
                "back to severity, then id. A repeat recorded as a `recurrences` entry (see "
                "AGENTS.md) raises its incident here.")
    return "Ranked by occurrences (an incident plus its recorded repeats), then severity, then id."


def leaf_areas(m: Model) -> list[tuple[str, str, list]]:
    """(node path, label, incidents) for every node that lists incidents in full."""
    areas = []
    for c in m.classes:
        if m.has_topics(c):
            areas += [(m.topic_node(k), k, m.topic_members[k]) for k in m.class_topics[c]]
        else:
            areas.append((m.class_node(c), c, m.home[c]))
    return areas


def root_node(m: Model) -> str:
    d = "catalog"
    n_topics = len(m.topics)
    out = ["# Agent failure modes - catalog", "",
           f"Start here. {len(m.incidents)} incidents from autonomous agent loops, arranged as a tree: "
           "this root, then a class node, then a topic leaf, then the incident page. Every node is "
           f"small enough to read whole (max {NODE_BUDGET // 1024} KB). Generated by tools/build.py "
           "from tools/corpus.py: never edit it by hand.", "",
           "## How to navigate", "",
           "1. Fastest: `python3 tools/afm.py route \"what you observe\"` prints the best nodes, and "
           "`python3 tools/afm.py search \"text\"` prints matching incidents with their rules. Both run "
           "from any directory.",
           "2. By hand: pick the class below whose \"you are probably here if\" matches what you SEE, "
           "open its node, then the topic whose \"go here if\" matches, then the incident.",
           "3. Before recording a failure, run `python3 tools/afm.py check \"title + signature + root "
           "cause\"`: a repeat becomes a recurrence, not a new incident. See [AGENTS.md](../AGENTS.md).",
           f"4. Standing guidance for a prompt: [CORE.md](CORE.md) (max {CORE_BUDGET // 1024} KB). "
           "Do not load RULES.md, TAXONOMY.md or data/incidents.json whole.", ""]

    out += ["## Most-recurrent failures", "", _recurrence_note(m), "",
            "| Incident | n | Severity | Where | Title |", "|---|---|---|---|---|"]
    for inc in m.most_recurrent(ROOT_TOP):
        out.append(f"| [{inc['id']}]({rel(m.page(inc), d)}) | {m.occ[inc['id']]} | {inc['severity']} | "
                   f"[{m.where(inc)}]({rel(m.node_of(inc), d)}) | {cell(inc['title'])} |")
    out.append("")

    areas = sorted(leaf_areas(m), key=lambda a: (-m.area_occ(a[2]), -len(a[2]), a[0]))[:ROOT_AREAS]
    out += ["## Largest failure areas", "",
            "Leaf nodes ranked by occurrences (n); incidents counts every record filed there.", "",
            "| Area | n | Incidents |", "|---|---|---|"]
    out += [f"| [{label}]({rel(node, d)}) | {m.area_occ(incs)} | {len(incs)} |" for node, label, incs in areas]
    out.append("")

    out += ["## Classes", "",
            "Home = incidents whose first class is this one; also = filed elsewhere but tagged with it. "
            + (f"The classes hold {n_topics} topics." if n_topics else "No class has topics yet."), "",
            "| Class | You are probably here if | Home | Also |", "|---|---|---|---|"]
    for c in m.classes:
        out.append(f"| [{c}]({rel(m.class_node(c), d)}) | {cell(m.route(c))} | "
                   f"{len(m.home[c])} | {len(m.also[c])} |")
    out.append("")

    out += ["## Practices", "",
            "What to do by default, distilled from several incidents each. Full text in "
            "[CORE.md](CORE.md#practices).", ""]
    out += [f"- **{p['id']}** - {p['title']}" for p in m.practices]
    out.append("")
    return NL.join(out)


def _core_parts(m: Model) -> tuple[list[str], list[str], list[str]]:
    """(head with practices, topic keys ranked by importance, most-recurrent rule lines)."""
    head = ["# Core rules - the prompt-sized payload", "",
            f"Load this file into an agent prompt (max {CORE_BUDGET // 1024} KB). It holds the practices, "
            "one distilled rule per catalog topic, and the rules of the most-recurrent incidents, "
            f"distilled from {len(m.incidents)} incidents. The complete list is RULES.md, which is "
            "not prompt-sized. Look any id up with `python3 tools/afm.py show INC-XXXX`. "
            "Generated by tools/build.py: never edit it by hand.", "",
            "## Practices", ""]
    for p in m.practices:
        head += [f"- **{p['id']} - {p['title']}.** {p['practice']}"]
    head.append("")
    ranked = sorted(m.topics, key=lambda k: (-m.area_occ(m.topic_members[k]), -len(m.topic_members[k]), k))
    rec = [f"- **[{inc['id']} / {inc['severity']} / {m.occ[inc['id']]}x]** {inc['rule']}"
           for inc in m.most_recurrent(CORE_MAX_RULES)]
    return head, ranked, rec


def _core_assemble(m: Model, head: list[str], full: set, rec: list[str]) -> str:
    out = list(head)
    if m.topics:
        out += ["## Topic rules", "", "One distilled rule per topic, grouped by class."]
        if len(full) < len(m.topics):
            out += ["", f"{len(full)} of {len(m.topics)} topics, the largest by occurrences, fit here in full; "
                    "the rest are linked, and each leaf states its rule at the top."]
        out.append("")
        for c in m.classes:
            if not m.has_topics(c):
                continue
            out += [f"### {c}", ""]
            out += [f"- **{m.topics[k]['title']}:** {m.topics[k]['rule']}" for k in m.class_topics[c] if k in full]
            rest = [k for k in m.class_topics[c] if k not in full]
            if rest:
                out.append("- Rule in the leaf: " + ", ".join(
                    f"[{m.topics[k]['title']}]({k}.md)" for k in rest))
            out.append("")
    out += ["## Rules of the most-recurrent incidents", "", _recurrence_note(m), ""]
    out += rec
    out.append("")
    return NL.join(out)


def core_md(m: Model) -> str:
    """Practices always; then a reserve of most-recurrent rules; then as many topic rules as fit
    (largest topics first); then more most-recurrent rules. Never exceeds CORE_BUDGET unless
    the practices alone do."""
    head, ranked, rec = _core_parts(m)

    def fits(full: set, n: int) -> bool:
        return nbytes(_core_assemble(m, head, full, rec[:n])) <= CORE_BUDGET

    n = min(CORE_MIN_RECURRENT, len(rec))
    while n and not fits(set(), n):
        n -= 1
    full: set = set()
    for k in ranked:
        if not fits(full | {k}, n):
            break
        full.add(k)
    while n < len(rec) and fits(full, n + 1):
        n += 1
    return _core_assemble(m, head, full, rec[:n])


def core_coverage(m: Model) -> tuple[int, int, int]:
    """(topics with their rule in CORE.md in full, topics, most-recurrent rules in CORE.md)."""
    text = core_md(m)
    full = sum(1 for k in m.topics if f"- **{m.topics[k]['title']}:** {m.topics[k]['rule']}" in text)
    rec = text.count("- **[INC-")
    return full, len(m.topics), rec


# --------------------------------------------------------------------------- flat artifacts

def rules_md(m: Model) -> str:
    rules = [
        "# Rules",
        "",
        "Every transferable rule in this knowledge base, one line each. This is the COMPLETE list, "
        "too large for a prompt: for a prompt payload load [catalog/CORE.md](catalog/CORE.md); to find "
        "the rule for a symptom, run `python3 tools/afm.py search \"...\"` or walk "
        "[catalog/README.md](catalog/README.md).",
        "It is derived from tools/corpus.py, so never edit it by hand.",
        "",
        "## Rules from incidents",
        "",
        "One rule per incident, ordered by severity then id.",
        "",
    ]
    for inc in sorted(m.incidents, key=lambda x: (SEV_ORDER[x["severity"]], x["id"])):
        rules.append(f"- **[{inc['id']} / {inc['severity']}]** {inc['rule']}")
    rules += [
        "",
        "## Practices",
        "",
        "Cross-incident best practice: what to do by DEFAULT, distilled from the incidents above.",
        "Each practice names the incidents it generalizes, so it can never claim evidence the corpus lacks.",
        "",
    ]
    for pra in m.practices:
        rules.append(f"- **[{pra['id']}]** {pra['practice']}")
        rules.append(f"  - _derived from:_ {', '.join(pra['derived_from'])}")
    rules.append("")
    return NL.join(rules)


def taxonomy_md(m: Model) -> str:
    tax = ["# Taxonomy", "",
           "Failure classes observed in production autonomous-agent loops. A single incident often",
           "belongs to several: the interesting failures sit where two classes meet.", "",
           "Each class links to its node in the [catalog](catalog/README.md), which lists its topics and "
           "incidents. To find a class from what you observe, start at the catalog root or run "
           "`python3 tools/afm.py route \"...\"`.", ""]
    for c, meta in m.classes.items():
        tax += [f"## {c}", "", meta["what"], "",
                f"**Ask:** {meta['ask']}", "",
                f"**Incidents:** {len(m.home[c])} filed here, {len(m.also[c])} more from other classes "
                f"tagged with it. **Catalog node:** [catalog/{c}/](catalog/{c}/README.md)", ""]
        if m.has_topics(c):
            tax += ["**Topics:** " + ", ".join(
                f"[{m.topics[k]['title']}](catalog/{k}.md) ({m.area_occ(m.topic_members[k])})"
                for k in m.class_topics[c]), ""]
    return NL.join(tax)


def incidents_json(m: Model) -> str:
    index = [{
        "id": i["id"], "title": i["title"], "date": i["date"], "classes": i["classes"],
        "topic": i.get("topic"), "severity": i["severity"], "status": i["status"],
        "occurrences": m.occ[i["id"]], "recurrence_of": i.get("recurrence_of"),
        "recurrences": i.get("recurrences", []),
        "rule": i["rule"], "signature": i["signature"], "root_cause": i["root_cause"], "what": i["what"],
        "file": m.page(i), "node": m.node_of(i),
        "related": i.get("related", []),
        "evidence": i.get("evidence", []),
    } for i in m.incidents]
    doc = {"schema": 2, "count": len(index), "classes": m.classes, "topics": m.topics, "incidents": index}
    return json.dumps(doc, indent=2, ensure_ascii=True) + NL


def catalog_json(m: Model) -> str:
    classes = {}
    for c in m.classes:
        classes[c] = {"node": m.class_node(c), "home": len(m.home[c]), "also_tagged": len(m.also[c]),
                      "occurrences": m.area_occ(m.home[c]), "topics": m.class_topics[c],
                      "class_level": [i["id"] for i in m.class_level[c]],
                      "also_tagged_ids": [i["id"] for i in m.also[c]]}
    topics = {k: {"title": m.topics[k]["title"], "node": m.topic_node(k),
                  "occurrences": m.area_occ(m.topic_members[k]),
                  "incidents": [i["id"] for i in m.topic_members[k]]} for k in sorted(m.topics)}
    doc = {"schema": 1, "root": "catalog/README.md", "core": "catalog/CORE.md",
           "counts": {"incidents": len(m.incidents), "classes": len(m.classes), "topics": len(m.topics),
                      "practices": len(m.practices), "recurrence_records": m.n_stubs(),
                      "recorded_repeats": m.n_entries(), "occurrences": m.total_occ()},
           "most_recurrent": [[i["id"], m.occ[i["id"]]] for i in m.most_recurrent(JSON_TOP)],
           "classes": classes, "topics": topics}
    return json.dumps(doc, indent=1, ensure_ascii=True) + NL


def render(m: Model) -> dict[str, str]:
    """Every fully generated file, keyed by repo-relative path. Pure."""
    files = {m.page(i): incident_page(i, m) for i in m.incidents}
    files["catalog/README.md"] = root_node(m)
    files["catalog/CORE.md"] = core_md(m)
    for c in m.classes:
        files[m.class_node(c)] = class_node(c, m)
        for k in m.class_topics[c]:
            files[m.topic_node(k)] = topic_leaf(k, m)
    files["data/incidents.json"] = incidents_json(m)
    files["data/catalog.json"] = catalog_json(m)
    files["RULES.md"] = rules_md(m)
    files["TAXONOMY.md"] = taxonomy_md(m)
    return files


# --------------------------------------------------------------------------- hand-written docs with generated regions

def replace_generated_region(text: str, name: str, body: str) -> str:
    """Replace one marked region while preserving human-authored prose."""
    start = f"<!-- BEGIN GENERATED: {name} -->"
    end = f"<!-- END GENERATED: {name} -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"file must contain exactly one {start!r} and {end!r}")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{body.rstrip()}\n{end}{after}"


def readme_text(current: str, m: Model | None = None) -> str:
    """Refresh corpus-derived README facts without owning the whole document."""
    m = m or MODEL()
    summary = NL.join([
        f"- **[incidents/](incidents/)** - {len(m.incidents)} human-readable post-mortems, one per file. Each has: signature (how to recognise it), what happened, root cause, why it was hard to see, fix, verification, and a transferable rule.",
        f"- **[TAXONOMY.md](TAXONOMY.md)** - the {len(m.classes)} failure classes, each with the diagnostic question that surfaces it.",
    ])
    class_table = ["| Class | What it looks like |", "|---|---|"]
    class_table.extend(f"| **{cid}** | {meta['what']} |" for cid, meta in m.classes.items())
    current = replace_generated_region(current, "corpus-summary", summary)
    return replace_generated_region(current, "failure-classes", NL.join(class_table))


def agents_stats(m: Model) -> str:
    top = m.most_recurrent(3)
    return NL.join([
        f"- Incidents: {len(m.incidents)} ({len(m.incidents) - m.n_stubs()} canonical, "
        f"{m.n_stubs()} recurrence records, {m.n_entries()} recorded repeats, "
        f"{m.total_occ()} occurrences in total).",
        f"- Failure classes: {len(m.classes)}; topics: {len(m.topics)}; practices: {len(m.practices)}.",
        f"- Highest occurrence count: {m.max_occ()} "
        f"({', '.join(i['id'] for i in top if m.occ[i['id']] == m.max_occ() and m.max_occ() > 1) or 'no repeats recorded yet'}).",
    ])


def agents_text(current: str, m: Model | None = None) -> str:
    m = m or MODEL()
    return replace_generated_region(current, "agents-stats", agents_stats(m))


def MODEL() -> Model:
    return Model(INCIDENTS, CLASSES, TOPICS, PRACTICES)


# --------------------------------------------------------------------------- main

def over_budget(files: dict[str, str]) -> list[tuple[str, int, int]]:
    out = []
    for path, text in sorted(files.items()):
        if not path.startswith("catalog/"):
            continue
        cap = CORE_BUDGET if path == "catalog/CORE.md" else NODE_BUDGET
        if nbytes(text) > cap:
            out.append((path, nbytes(text), cap))
    return out


def _write(path: str, text: str) -> None:
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    try:
        if open(full, encoding="utf-8").read() == text:
            return
    except OSError:
        pass
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> int:
    errs = validate()
    if errs:
        print("CORPUS INVALID:")
        for e in errs:
            print("  ", e)
        return 1
    m = MODEL()
    files = render(m)

    # Stale-file guard: a renamed title or a removed topic used to leave an orphan behind.
    for base in ("incidents", "catalog"):
        top = os.path.join(ROOT, base)
        if not os.path.isdir(top):
            continue
        for dirpath, _, fns in os.walk(top, topdown=False):
            for fn in fns:
                relp = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace(os.sep, "/")
                if fn.endswith(".md") and relp not in files:
                    os.remove(os.path.join(dirpath, fn))
                    print("removed orphan page:", relp)
            if dirpath != top and not os.listdir(dirpath):
                os.rmdir(dirpath)

    for path, text in files.items():
        _write(path, text)
    for name, fn in (("README.md", readme_text), ("AGENTS.md", agents_text)):
        with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
            _write(name, fn(fh.read(), m))

    print(f"built {len(m.incidents)} incidents, {len(m.classes)} classes, {len(m.topics)} topics, "
          f"{len(m.practices)} practices, {m.total_occ()} occurrences")
    print("  incidents/*.md, catalog/, data/incidents.json, data/catalog.json, RULES.md, TAXONOMY.md, "
          "README.md and AGENTS.md regions")
    if over := over_budget(files):
        print(f"note: {len(over)} catalog node(s) over budget (a class node with too many incidents and no "
              "topics cannot fit even as one-liners; assign topics):")
        for path, n, cap in over:
            print(f"  {path}: {n} bytes > {cap} ({cap // 1024} KB)")
    full, n_topics, n_rec = core_coverage(m)
    if full < n_topics:
        print(f"note: catalog/CORE.md carries {full} of {n_topics} topic rules in full and {n_rec} "
              f"most-recurrent rules; the rest do not fit {CORE_BUDGET // 1024} KB (shorten topic rules)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
