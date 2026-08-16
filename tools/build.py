#!/usr/bin/env python3
"""Generate the knowledge base from the structured corpus in tools/corpus.py.

Everything human-readable here is DERIVED. The corpus is the single source of
truth, so the incident pages, the machine-readable index, the taxonomy and the
README index cannot drift apart. Regenerate with:  python3 tools/build.py
"""
from __future__ import annotations
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import INCIDENTS, CLASSES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["id", "title", "date", "classes", "severity", "status", "cost",
            "signature", "what", "root_cause", "why_hard", "fix", "verification", "rule"]
SEVERITIES = {"low", "medium", "high", "critical"}
STATUSES = {"fixed", "mitigated", "open", "structural"}


def slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60].rstrip("-")


def validate() -> list[str]:
    errs, seen = [], set()
    for inc in INCIDENTS:
        i = inc.get("id", "<no id>")
        for f in REQUIRED:
            if not inc.get(f):
                errs.append(f"{i}: missing required field '{f}'")
        if i in seen:
            errs.append(f"{i}: duplicate id")
        seen.add(i)
        if inc.get("severity") not in SEVERITIES:
            errs.append(f"{i}: severity '{inc.get('severity')}' not in {sorted(SEVERITIES)}")
        if inc.get("status") not in STATUSES:
            errs.append(f"{i}: status '{inc.get('status')}' not in {sorted(STATUSES)}")
        for c in inc.get("classes", []):
            if c not in CLASSES:
                errs.append(f"{i}: unknown class '{c}'")
        if len(inc.get("rule", "")) > 400:
            errs.append(f"{i}: rule is {len(inc['rule'])} chars; keep it under 400 so it fits a prompt")
    ids = {inc["id"] for inc in INCIDENTS}
    for inc in INCIDENTS:
        for r in inc.get("related", []):
            if r not in ids:
                errs.append(f"{inc['id']}: related id '{r}' does not exist")
    return errs


def incident_page(inc: dict) -> str:
    nl = chr(10)
    out = [
        "---",
        f"id: {inc['id']}",
        f"title: {inc['title']}",
        f"date: {inc['date']}",
        f"classes: [{', '.join(inc['classes'])}]",
        f"severity: {inc['severity']}",
        f"status: {inc['status']}",
        "---",
        "",
        f"# {inc['id']} - {inc['title']}",
        "",
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
    if inc.get("evidence"):
        out += ["## Provenance", "",
                "Where this was observed, so the claim is checkable rather than anecdotal:", ""]
        out += [f"- {e}" for e in inc["evidence"]]
        out += [""]
    if inc.get("related"):
        out += ["## Related", "", " ".join(f"[{r}](./{filename(byid(r))})" for r in inc["related"]), ""]
    return nl.join(out)


def byid(iid: str) -> dict:
    return next(i for i in INCIDENTS if i["id"] == iid)


def filename(inc: dict) -> str:
    return f"{inc['id']}-{slug(inc['title'])}.md"


def main() -> int:
    errs = validate()
    if errs:
        print("CORPUS INVALID:")
        for e in errs:
            print("  ", e)
        return 1

    nl = chr(10)
    os.makedirs(os.path.join(ROOT, "incidents"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)

    # Stale-file guard: a renamed title used to leave an orphan page behind.
    keep = {filename(i) for i in INCIDENTS}
    for fn in os.listdir(os.path.join(ROOT, "incidents")):
        if fn.endswith(".md") and fn not in keep:
            os.remove(os.path.join(ROOT, "incidents", fn))
            print("removed orphan page:", fn)

    for inc in INCIDENTS:
        with open(os.path.join(ROOT, "incidents", filename(inc)), "w", encoding="utf-8") as fh:
            fh.write(incident_page(inc))

    index = [{
        "id": i["id"], "title": i["title"], "date": i["date"], "classes": i["classes"],
        "severity": i["severity"], "status": i["status"], "rule": i["rule"],
        "signature": i["signature"], "file": f"incidents/{filename(i)}",
        "related": i.get("related", []),
        "evidence": i.get("evidence", []),
    } for i in sorted(INCIDENTS, key=lambda x: x["id"])]
    with open(os.path.join(ROOT, "data", "incidents.json"), "w", encoding="utf-8") as fh:
        json.dump({"schema": 1, "count": len(index), "classes": CLASSES, "incidents": index},
                  fh, indent=2, ensure_ascii=True)
        fh.write(nl)

    # RULES.md - the agent-loadable ruleset, ordered by severity then id.
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    rules = [
        "# Rules",
        "",
        "Every transferable rule in this knowledge base, one line each, ordered by severity.",
        "This file is the intended payload for an agent prompt: it is derived, so never edit it by hand.",
        "",
    ]
    for inc in sorted(INCIDENTS, key=lambda x: (order[x["severity"]], x["id"])):
        rules.append(f"- **[{inc['id']} / {inc['severity']}]** {inc['rule']}")
    rules.append("")
    with open(os.path.join(ROOT, "RULES.md"), "w", encoding="utf-8") as fh:
        fh.write(nl.join(rules))

    # TAXONOMY.md
    tax = ["# Taxonomy", "",
           "Failure classes observed in production autonomous-agent loops. A single incident often",
           "belongs to several: the interesting failures sit where two classes meet.", ""]
    for cid, meta in CLASSES.items():
        members = [i for i in INCIDENTS if cid in i["classes"]]
        tax += [f"## {cid}", "", meta["what"], "",
                f"**Ask:** {meta['ask']}", "",
                f"**Incidents ({len(members)}):** " +
                (" ".join(f"[{m['id']}](incidents/{filename(m)})" for m in sorted(members, key=lambda x: x['id'])) or "none yet"),
                ""]
    with open(os.path.join(ROOT, "TAXONOMY.md"), "w", encoding="utf-8") as fh:
        fh.write(nl.join(tax))

    print(f"built {len(INCIDENTS)} incidents, {len(CLASSES)} classes")
    print("  incidents/*.md, data/incidents.json, RULES.md, TAXONOMY.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
