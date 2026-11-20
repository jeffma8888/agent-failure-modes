"""The catalog tree, the topic/recurrence schema, tools/afm.py and tools/sync_repo_meta.py.

Two kinds of test live here. Fixture tests build a small synthetic corpus in memory, so
they pin the rules (validation, occurrence math, rendering) independently of the data.
Real-corpus tests run against the actual build output on disk. The budget tests
(`test_budget_*`) are real-corpus tests that only become meaningful once topic data lands:
a class with many home incidents and no topics cannot fit in one 12 KB node.
"""
from __future__ import annotations
import copy, json, os, posixpath, random, re, subprocess, sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import afm  # noqa: E402
import build  # noqa: E402
import eval_afm  # noqa: E402
import sync_repo_meta  # noqa: E402
from corpus import CLASSES, INCIDENTS, PRACTICES, TOPICS  # noqa: E402

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
SEED = 20261119


# --------------------------------------------------------------------------- fixture corpus

def mk(n: int, cls, topic=None, **kw) -> dict:
    inc = {
        "id": f"INC-{n:04d}", "title": f"Fixture incident {n} about {cls[0]}",
        "date": f"2026-01-{min(n, 28):02d}", "classes": list(cls), "severity": "medium",
        "status": "fixed", "cost": "about an hour", "signature": f"signature text {n}",
        "what": f"what happened {n}", "root_cause": f"root cause {n}", "why_hard": "it was quiet",
        "fix": "fixed it", "verification": "checked it", "rule": f"Do the thing number {n}.",
    }
    if topic:
        inc["topic"] = topic
    inc.update(kw)
    return inc


def fixture() -> dict:
    """24 home incidents in 'alpha' (so it may have topics), 2 in 'beta' (so it may not)."""
    classes = {
        "alpha": {"what": "Alpha failures. A second sentence.", "ask": "Is it alpha?",
                  "route": "the alpha symptom shows up"},
        "beta": {"what": "Beta failures happen quietly. More text.", "ask": "Is it beta?"},
    }
    topics = {
        "alpha/one": {"title": "Alpha one", "go_here_if": "a kiwi crash shows", "rule": "Do alpha one."},
        "alpha/two": {"title": "Alpha two", "go_here_if": "a plum stall shows", "rule": "Do alpha two."},
    }
    incs = [
        mk(1, ["alpha"], "alpha/one", severity="high", recurrences=[
            {"date": "2026-02-01", "note": "recurred in a second loop"},
            {"date": "2026-03-01", "note": "recurred again", "evidence": ["https://example.org/log - the log"]},
        ]),
        mk(2, ["alpha"], "alpha/two"),
        mk(3, ["alpha"], "alpha/one", recurrence_of="INC-0001",
           recurrences=[{"date": "2026-04-01", "note": "the duplicate recurred too"}]),
        mk(4, ["beta"], related=["INC-0001"]),
        mk(5, ["beta", "alpha"], recurrence_of="INC-0004"),
        mk(6, ["alpha"]),  # class-level outlier 1 of at most 3
    ]
    incs += [mk(n, ["alpha"], "alpha/one" if n % 2 == 0 else "alpha/two") for n in range(7, 27)]
    practices = [{"id": "PRA-0001", "title": "A practice", "practice": "Practise it.", "why": "because",
                  "derived_from": ["INC-0001", "INC-0004"]}]
    return {"incidents": incs, "classes": classes, "topics": topics, "practices": practices}


def model(fx: dict) -> build.Model:
    return build.Model(fx["incidents"], fx["classes"], fx["topics"], fx["practices"])


def by_id(fx: dict, iid: str) -> dict:
    return next(i for i in fx["incidents"] if i["id"] == iid)


def errors(fx: dict) -> list[str]:
    return build.validate(fx["incidents"], fx["classes"], fx["topics"], fx["practices"])


# --------------------------------------------------------------------------- validation, two-sided

def test_valid_fixture_is_accepted():
    assert errors(fixture()) == []


def test_real_corpus_is_valid():
    assert build.validate() == []


def _set(iid, **kw):
    def f(fx):
        by_id(fx, iid).update(kw)
    return f


def _drop(iid, field):
    def f(fx):
        by_id(fx, iid).pop(field, None)
    return f


def _many(*fs):
    def f(fx):
        for g in fs:
            g(fx)
    return f


def _topic(key, **meta):
    def f(fx):
        fx["topics"][key] = {"title": "T", "go_here_if": "g", "rule": "r", **meta}
    return f


def _cls(cid, **meta):
    def f(fx):
        fx["classes"][cid].update(meta)
    return f


def _add(inc):
    def f(fx):
        fx["incidents"].append(inc)
    return f


BAD = {
    # topic placement
    "unregistered topic": (_set("INC-0002", topic="alpha/nope"), "not registered in TOPICS"),
    "topic of another class": (_set("INC-0004", topic="alpha/one"), "but the home class (classes[0]) is 'beta'"),
    "topic decided by a non-home class": (_set("INC-0002", classes=["beta", "alpha"]), "home class"),
    "four class-level outliers": (_many(_drop("INC-0007", "topic"), _drop("INC-0008", "topic"),
                                        _drop("INC-0009", "topic")), "at most 3 class-level outliers"),
    "topics in a small class": (_many(_topic("beta/small"), _set("INC-0004", topic="beta/small"),
                                      _set("INC-0005", topic="beta/small")), "only 2 home incidents"),
    "registered topic nobody carries": (_topic("alpha/empty"), "registered but no incident carries it"),
    "topic for an unknown class": (_topic("gamma/x"), "class 'gamma' is not in CLASSES"),
    "topic slug not kebab-case": (_many(_topic("alpha/Bad_Slug"), _set("INC-0006", topic="alpha/Bad_Slug")),
                                  "kebab-case"),
    "topic title too long": (_many(_topic("alpha/long", title="x" * 71), _set("INC-0006", topic="alpha/long")),
                             "title is 71 chars > 70"),
    "topic go_here_if too long": (_many(_topic("alpha/long", go_here_if="x" * 201),
                                        _set("INC-0006", topic="alpha/long")), "go_here_if is 201"),
    "topic rule too long": (_many(_topic("alpha/long", rule="x" * 401), _set("INC-0006", topic="alpha/long")),
                            "rule is 401 chars > 400"),
    "topic unknown field": (_many(_topic("alpha/odd", extra="?"), _set("INC-0006", topic="alpha/odd")),
                            "unknown field(s) ['extra']"),
    # class route
    "route too long": (_cls("alpha", route="x" * 161), "route is 161 chars > 160"),
    "route empty": (_cls("beta", route=" "), "route must be a non-empty string"),
    "class unknown field": (_cls("beta", routes="typo"), "unknown field(s) ['routes']"),
    # recurrence_of
    "recurrence_of missing id": (_set("INC-0003", recurrence_of="INC-0099"), "'INC-0099' does not exist"),
    "recurrence_of itself": (_set("INC-0003", recurrence_of="INC-0003"), "points at itself"),
    "recurrence_of a later id": (_many(_drop("INC-0005", "recurrence_of"), _set("INC-0004", recurrence_of="INC-0005")),
                                 "must point at an EARLIER (lower) id"),
    "recurrence_of a recurrence": (_add(mk(27, ["alpha"], "alpha/one", recurrence_of="INC-0003")), "no chains"),
    "recurrence_of another topic": (_set("INC-0003", topic="alpha/two"), "must share its home class and topic"),
    "recurrence_of another class": (_set("INC-0006", recurrence_of="INC-0004"), "must share its home class and topic"),
    # recurrences entries
    "recurrences not a list": (_set("INC-0002", recurrences={"date": "2026-02-01", "note": "n"}), "must be a list"),
    "recurrence not a dict": (_set("INC-0002", recurrences=["2026-02-01"]), "must be a dict"),
    "recurrence date not ISO": (_set("INC-0002", recurrences=[{"date": "02/01/2026", "note": "n"}]),
                                "not a valid ISO"),
    "recurrence date impossible": (_set("INC-0002", recurrences=[{"date": "2026-02-30", "note": "n"}]),
                                   "not a valid ISO"),
    "recurrence date missing": (_set("INC-0002", recurrences=[{"note": "n"}]), "not a valid ISO"),
    "recurrence before the incident": (_set("INC-0002", recurrences=[{"date": "2025-12-31", "note": "n"}]),
                                       "precedes the incident's own date"),
    "recurrence note too long": (_set("INC-0002", recurrences=[{"date": "2026-02-01", "note": "x" * 301}]),
                                 "note is 301 chars > 300"),
    "recurrence note missing": (_set("INC-0002", recurrences=[{"date": "2026-02-01"}]), "missing note"),
    "recurrence unknown field": (_set("INC-0002", recurrences=[{"date": "2026-02-01", "note": "n", "url": "u"}]),
                                 "unknown field(s) ['url']"),
    "recurrence evidence not a list": (_set("INC-0002", recurrences=[
        {"date": "2026-02-01", "note": "n", "evidence": "https://example.org"}]), "evidence must be a list"),
    # plain incident fields
    "unknown incident field": (_set("INC-0002", topik="alpha/one"), "unknown field(s) ['topik']"),
    "missing required field": (_drop("INC-0002", "rule"), "missing required field 'rule'"),
    "bad incident date": (_set("INC-0002", date="2026-13-01"), "is not ISO"),
    "duplicate id": (_add(mk(2, ["alpha"], "alpha/two")), "duplicate id"),
    "related id missing": (_set("INC-0002", related=["INC-0999"]), "related id 'INC-0999' does not exist"),
    # types: malformed input is an error message, never a traceback
    "rule is a list": (_set("INC-0002", rule=["Do it."]), "'rule' must be a non-empty string, not list"),
    "signature is a list": (_set("INC-0002", signature=["s"]), "'signature' must be a non-empty string"),
    "title is whitespace": (_set("INC-0002", title="   "), "missing required field 'title'"),
    "rule spans two lines": (_set("INC-0002", rule="Do it.\nThen more."), "rule must be one line"),
    "severity is a list": (_set("INC-0002", severity=["high"]), "severity ['high'] not in"),
    "classes is a string": (_set("INC-0004", classes="beta"), "classes must be a non-empty list"),
    "classes is empty": (_set("INC-0004", classes=[]), "classes must be a non-empty list"),
    "class id not a string": (_set("INC-0004", classes=["beta", ["alpha"]]), "class-id strings, not list"),
    "related not a list": (_set("INC-0002", related="INC-0001"), "related must be a list of incident ids"),
    "related entry not a string": (_set("INC-0002", related=[["INC-0001"]]), "related must be a list"),
    "evidence not a list": (_set("INC-0002", evidence="https://example.org"),
                            "evidence must be a list of non-empty strings"),
    "evidence entry blank": (_set("INC-0002", evidence=["https://example.org - x", " "]),
                             "evidence must be a list of non-empty strings"),
    "incident not a dict": (_add("INC-0027"), "incident #27 in INCIDENTS must be a dict, not str"),
    # ids: full match, positive, contiguous
    "id zero": (_set("INC-0002", id="INC-0000"), "id must look like INC-0001"),
    "id with a trailing newline": (_set("INC-0002", id="INC-0002\n"), "id must look like INC-0001"),
    "id not a string": (_set("INC-0002", id=2), "id must look like INC-0001"),
    "id gap": (_add(mk(28, ["alpha"], "alpha/one")), "without a gap; missing INC-0027"),
}


@pytest.mark.parametrize("case", sorted(BAD))
def test_validation_rejects_bad_case(case):
    mutate, expected = BAD[case]
    fx = copy.deepcopy(fixture())
    mutate(fx)
    errs = errors(fx)
    assert errs, f"{case}: accepted, but must be rejected"
    assert any(expected in e for e in errs), f"{case}: expected {expected!r} in {errs}"


@pytest.mark.parametrize("case", [
    "three class-level outliers", "note of exactly 300", "route of exactly 160",
    "recurrence on its own date", "recurrence with evidence", "small class without topics",
    "rule of exactly 400 on one line", "related and evidence lists", "next id appended",
])
def test_validation_accepts_boundary_case(case):
    fx = copy.deepcopy(fixture())
    if case == "three class-level outliers":
        _many(_drop("INC-0007", "topic"), _drop("INC-0008", "topic"))(fx)
    elif case == "note of exactly 300":
        _set("INC-0002", recurrences=[{"date": "2026-02-01", "note": "x" * 300}])(fx)
    elif case == "route of exactly 160":
        _cls("alpha", route="x" * 160)(fx)
    elif case == "recurrence on its own date":
        _set("INC-0002", recurrences=[{"date": "2026-01-02", "note": "same day"}])(fx)
    elif case == "recurrence with evidence":
        _set("INC-0002", recurrences=[{"date": "2026-05-01", "note": "n", "evidence": ["a", "b"]}])(fx)
    elif case == "small class without topics":
        assert not any(k.startswith("beta/") for k in fx["topics"])
    elif case == "rule of exactly 400 on one line":
        _set("INC-0002", rule="x" * 400)(fx)
    elif case == "related and evidence lists":
        _set("INC-0002", related=["INC-0001", "INC-0004"], evidence=["https://example.org - the log"])(fx)
    elif case == "next id appended":
        _add(mk(27, ["alpha"], "alpha/two"))(fx)
    assert errors(fx) == [], case


@pytest.mark.parametrize("value", [[["a", "nested", "list"]], 7, None, {"a": "dict"}],
                         ids=["list", "int", "none", "dict"])
def test_validation_reports_every_malformed_field_without_raising(value):
    for f in build.REQUIRED + build.OPTIONAL:
        fx = copy.deepcopy(fixture())
        by_id(fx, "INC-0002")[f] = value
        errs = errors(fx)  # must not raise
        assert errs, f"{f}={value!r} accepted"


def _sized(n_one: int) -> dict:
    """The fixture with exactly n_one home records in alpha/one (INC-0001 and its stub INC-0003
    count) and alpha/two kept within bounds, alpha staying above FLAT_MAX home incidents."""
    fx = fixture()
    fx["incidents"] = [i for i in fx["incidents"] if int(i["id"][4:]) <= 6]
    n_two = max(10, 21 - n_one)  # alpha/two = INC-0002 + n_two; alpha home = 4 + n_one - 2 + n_two
    keys = ["alpha/one"] * (n_one - 2) + ["alpha/two"] * n_two
    fx["incidents"] += [mk(n, ["alpha"], key) for n, key in enumerate(keys, 7)]
    return fx


@pytest.mark.parametrize("n,ok", [(5, False), (6, True), (25, True), (26, False)])
def test_topic_membership_bounds(n, ok):
    fx = _sized(n)
    assert sum(1 for i in fx["incidents"] if i.get("topic") == "alpha/one") == n
    errs = errors(fx)
    if ok:
        assert errs == []
    else:
        assert errs == [f"topic alpha/one: {n} home records; a topic holds {build.TOPIC_MIN} to "
                        f"{build.TOPIC_MAX} (merge a small one into a neighbour, split a large one)"]


def test_build_refuses_an_invalid_corpus(monkeypatch, capsys):
    fx = fixture()
    _set("INC-0002", topic="alpha/nope")(fx)
    monkeypatch.setattr(build, "INCIDENTS", fx["incidents"])
    monkeypatch.setattr(build, "CLASSES", fx["classes"])
    monkeypatch.setattr(build, "TOPICS", fx["topics"])
    monkeypatch.setattr(build, "PRACTICES", fx["practices"])
    monkeypatch.setattr(build, "_write", lambda *a: pytest.fail("an invalid corpus must not be written"))
    assert build.main() == 1
    assert "not registered in TOPICS" in capsys.readouterr().out


# --------------------------------------------------------------------------- occurrence math

def test_occurrence_math_on_fixture():
    m = model(fixture())
    # INC-0001: itself + 2 entries + its stub INC-0003 (1 + 1 entry)
    assert m.occ["INC-0001"] == 5
    assert m.occ["INC-0003"] == 2       # a stub counts its own entries; it never ranks
    assert m.occ["INC-0004"] == 2       # itself + stub INC-0005
    assert m.occ["INC-0002"] == 1
    assert m.n_stubs() == 2 and m.n_entries() == 3
    # every record and every entry is counted exactly once
    assert m.total_occ() == len(m.incidents) + m.n_entries() == 29
    ranked = [i["id"] for i in m.most_recurrent()]
    assert ranked[:2] == ["INC-0001", "INC-0004"]
    assert "INC-0003" not in ranked and "INC-0005" not in ranked
    assert m.area_occ(m.topic_members["alpha/one"]) == 15  # INC-0001 (5) + 10 one-shot fillers
    assert m.area_occ(m.home["beta"]) == 2


def test_most_recurrent_ties_break_on_severity_then_id():
    fx = fixture()
    _set("INC-0002", recurrences=[{"date": "2026-02-01", "note": "a"}], severity="low")(fx)
    _set("INC-0006", recurrences=[{"date": "2026-02-01", "note": "a"}], severity="critical")(fx)
    _set("INC-0008", recurrences=[{"date": "2026-02-01", "note": "a"}], severity="low")(fx)
    ranked = [i["id"] for i in model(fx).most_recurrent(5)]
    assert ranked == ["INC-0001", "INC-0006", "INC-0004", "INC-0002", "INC-0008"]


def test_real_corpus_occurrences_add_up():
    m = build.MODEL()
    assert m.total_occ() == len(INCIDENTS) + m.n_entries()
    data = json.load(open(os.path.join(ROOT, "data", "catalog.json"), encoding="utf-8"))
    assert data["counts"]["occurrences"] == m.total_occ()


# --------------------------------------------------------------------------- rendering (fixture)

@pytest.fixture(scope="module")
def fx_files():
    m = model(fixture())
    return m, build.render(m)


def _page(m, files, iid):
    return files[m.page(m.byid[iid])]


def test_incident_page_frontmatter_breadcrumb_and_banner(fx_files):
    m, files = fx_files
    stub = _page(m, files, "INC-0003")
    front = stub.split("---", 2)[1]
    assert "\ntopic: alpha/one\n" in front
    assert "\noccurrences: 2\n" in front
    assert "\nrecurrence_of: INC-0001\n" in front
    assert ("**Catalog:** [root](../catalog/README.md) / [alpha](../catalog/alpha/README.md) / "
            "[Alpha one](../catalog/alpha/one.md)") in stub
    assert f"> **Recurrence of [INC-0001](./{build.filename(m.byid['INC-0001'])}).**" in stub

    flat = _page(m, files, "INC-0004")
    assert "\ntopic: null\n" in flat and "\noccurrences: 2\n" in flat
    assert "recurrence_of" not in flat.split("---", 2)[1]
    assert "**Catalog:** [root](../catalog/README.md) / [beta](../catalog/beta/README.md)\n" in flat
    assert "Recurrence of" not in flat


def test_canonical_page_lists_its_recurrences(fx_files):
    m, files = fx_files
    page = _page(m, files, "INC-0001")
    section = page.split("## Recurrences", 1)[1].split("\n## ", 1)[0]
    assert "Occurrences: 5." in section
    assert f"- [INC-0003](./{build.filename(m.byid['INC-0003'])}) - 2026-01-03 -" in section
    assert "- 2026-02-01 - recurred in a second loop" in section
    assert "- 2026-03-01 - recurred again" in section
    assert "  - https://example.org/log - the log" in section
    assert "## Recurrences" not in _page(m, files, "INC-0002")


def test_topic_leaf_nests_stubs_under_their_canonical(fx_files):
    m, files = fx_files
    leaf = files["catalog/alpha/one.md"]
    assert leaf.startswith("# Alpha one\n")
    assert "**Go here if:** a kiwi crash shows" in leaf and "**Rule:** Do alpha one." in leaf
    assert "### [INC-0001]" in leaf and "### [INC-0003]" not in leaf
    entry = leaf.split("### [INC-0001]", 1)[1].split("\n### ", 1)[0]
    assert "occurrences 5" in entry and "  - [INC-0003](" in entry and "- 2026-02-01 - recurred" in entry
    assert leaf.index("### [INC-0001]") < leaf.index("### [INC-0008]"), "ranked by occurrences"


def test_class_nodes(fx_files):
    m, files = fx_files
    alpha = files["catalog/alpha/README.md"]
    assert "**You are probably here if:** the alpha symptom shows up" in alpha
    assert "| Alpha one | a kiwi crash shows | 15 | [one](one.md) |" in alpha
    assert "| Alpha two | a plum stall shows | 11 | [two](two.md) |" in alpha
    assert alpha.index("| Alpha one |") < alpha.index("| Alpha two |")
    assert "## Class-level incidents" in alpha and "[INC-0006](" in alpha
    assert "## Also tagged alpha" in alpha and "- [beta](../beta/README.md): INC-0005" in alpha
    beta = files["catalog/beta/README.md"]
    assert "## Topics" not in beta and "This class has no topics" in beta
    assert "You are probably here if" not in beta, "no route set: the class node does not invent one"
    assert "### [INC-0004]" in beta and "  - [INC-0005](" in beta
    assert set(files) >= {"catalog/alpha/one.md", "catalog/alpha/two.md"}
    assert not any(p.startswith("catalog/beta/") and not p.endswith("README.md") for p in files)


def test_root_router(fx_files):
    m, files = fx_files
    root = files["catalog/README.md"]
    rows = [ln for ln in root.split("## Most-recurrent failures", 1)[1].splitlines() if ln.startswith("| [INC-")]
    assert rows[0].startswith("| [INC-0001](../incidents/") and "| 5 | high |" in rows[0]
    assert "| [alpha](alpha/README.md) | the alpha symptom shows up | 24 | 1 |" in root
    assert "| [beta](beta/README.md) | Beta failures happen quietly. | 2 | 0 |" in root
    assert "**PRA-0001**" in root


def test_core_holds_practices_topic_rules_and_recurrent_rules(fx_files):
    m, files = fx_files
    core = files["catalog/CORE.md"]
    assert build.nbytes(core) <= build.CORE_BUDGET
    assert "**PRA-0001 - A practice.** Practise it." in core
    assert "- **Alpha one:** Do alpha one." in core and "- **Alpha two:** Do alpha two." in core
    assert core.index("[INC-0001 / high / 5x]") < core.index("[INC-0004 / medium / 2x]")


def test_core_degrades_to_links_when_topic_rules_do_not_fit(monkeypatch):
    fx = fixture()
    for key in fx["topics"]:
        fx["topics"][key]["rule"] = f"Rule for {key}: " + "x" * 380
    m = model(fx)
    assert errors(fx) == []
    head, _, rec = build._core_parts(m)
    everything = build._core_assemble(m, head, set(m.topics), rec[:build.CORE_MIN_RECURRENT])
    # 100 bytes short: one 400-char topic rule must give way to a link (a link line is ~50)
    monkeypatch.setattr(build, "CORE_BUDGET", build.nbytes(everything) - 100)
    core = build.core_md(m)
    assert build.nbytes(core) <= build.CORE_BUDGET
    assert "- **Alpha one:** Rule for alpha/one: " in core, "the largest topic keeps its rule"
    assert "- **Alpha two:**" not in core and "[Alpha two](alpha/two.md)" in core
    assert "1 of 2 topics" in core
    assert "[INC-0001 / high / 5x]" in core, "the most-recurrent reserve survives"


def test_fit_entries_degrades_to_one_liners_but_keeps_every_link(fx_files):
    m, _ = fx_files
    incs = m.canonicals(m.home["alpha"])
    roomy, k = build.fit_entries(["# head", ""], incs, [], m, "catalog/alpha")
    assert k == len(incs) and "listed by title only" not in roomy
    tight, k = build.fit_entries(["# head", ""], incs, [], m, "catalog/alpha", budget=4000)
    assert 0 < k < len(incs) and "listed by title only" in tight
    assert build.nbytes(tight) <= 4000
    for inc in incs:
        assert f"[{inc['id']}](../../incidents/{build.filename(inc)})" in tight
    assert "recurrences: [INC-0003](" in tight or "### [INC-0001]" in tight


def test_json_artifacts(fx_files):
    m, files = fx_files
    inc = json.loads(files["data/incidents.json"])
    assert inc["schema"] == 2 and inc["count"] == 26 and set(inc["topics"]) == {"alpha/one", "alpha/two"}
    rec = {i["id"]: i for i in inc["incidents"]}
    assert rec["INC-0001"]["occurrences"] == 5 and rec["INC-0001"]["recurrence_of"] is None
    assert rec["INC-0001"]["topic"] == "alpha/one" and len(rec["INC-0001"]["recurrences"]) == 2
    assert rec["INC-0003"]["recurrence_of"] == "INC-0001"
    assert rec["INC-0004"]["topic"] is None and rec["INC-0004"]["node"] == "catalog/beta/README.md"
    assert rec["INC-0001"]["node"] == "catalog/alpha/one.md"
    cat = json.loads(files["data/catalog.json"])
    assert cat["counts"] == {"incidents": 26, "classes": 2, "topics": 2, "practices": 1,
                             "recurrence_records": 2, "recorded_repeats": 3, "occurrences": 29}
    assert cat["most_recurrent"][:2] == [["INC-0001", 5], ["INC-0004", 2]]
    assert cat["classes"]["alpha"]["class_level"] == ["INC-0006"]
    assert cat["classes"]["alpha"]["also_tagged_ids"] == ["INC-0005"]
    assert "INC-0003" in cat["topics"]["alpha/one"]["incidents"]


def test_render_is_pure_and_deterministic():
    a = build.render(model(fixture()))
    b = build.render(model(copy.deepcopy(fixture())))
    assert a == b


# --------------------------------------------------------------------------- links and reachability

def _slug_anchor(heading: str) -> str:
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def _anchors(text: str) -> set[str]:
    return {_slug_anchor(h) for h in re.findall(r"^#{1,6} (.+)$", text, flags=re.M)}


def _targets(path: str, text: str):
    """(raw link, repo-relative target path, anchor) for every relative link in a file."""
    base = posixpath.dirname(path)
    for raw in LINK_RE.findall(text):
        if "://" in raw or raw.startswith(("mailto:", "#")):
            continue
        target, _, anchor = raw.partition("#")
        yield raw, posixpath.normpath(posixpath.join(base, target)), anchor


def _bfs(files: dict[str, str], start: str = "catalog/README.md") -> tuple[set, set]:
    """Follow links from the root, expanding catalog nodes only (never incident pages, whose
    Related links could hide an incident the catalog itself fails to list)."""
    seen_nodes, seen_pages, todo = {start}, set(), [start]
    while todo:
        node = todo.pop()
        for _, tgt, _ in _targets(node, files[node]):
            if tgt.startswith("catalog/") and tgt.endswith(".md") and tgt in files and tgt not in seen_nodes:
                seen_nodes.add(tgt)
                todo.append(tgt)
            elif tgt.startswith("incidents/"):
                seen_pages.add(tgt)
    return seen_nodes, seen_pages


def test_fixture_tree_reaches_every_incident_and_node(fx_files):
    m, files = fx_files
    nodes, pages = _bfs(files)
    assert pages == {m.page(i) for i in m.incidents}
    assert nodes == {p for p in files if p.startswith("catalog/")}


@pytest.fixture(scope="module")
def built():
    """The real build on disk, as CI sees it."""
    subprocess.check_call([sys.executable, os.path.join(ROOT, "tools", "build.py")], cwd=ROOT,
                          stdout=subprocess.DEVNULL)
    files = {}
    for base in ("catalog", "incidents"):
        for dirpath, _, fns in os.walk(os.path.join(ROOT, base)):
            for fn in fns:
                if fn.endswith(".md"):
                    fp = os.path.join(dirpath, fn)
                    files[os.path.relpath(fp, ROOT).replace(os.sep, "/")] = open(fp, encoding="utf-8").read()
    for fn in ("AGENTS.md", "README.md", "RULES.md", "TAXONOMY.md"):
        files[fn] = open(os.path.join(ROOT, fn), encoding="utf-8").read()
    return files


def test_disk_matches_the_renderer_with_no_stale_pages(built):
    rendered = build.render(build.MODEL())
    on_disk = {p for p in built if p.startswith(("catalog/", "incidents/"))}
    assert on_disk == {p for p in rendered if p.startswith(("catalog/", "incidents/"))}, \
        "stale or missing generated pages"
    for p in sorted(rendered):
        text = built[p] if p in built else open(os.path.join(ROOT, p), encoding="utf-8").read()
        assert text == rendered[p], f"{p} differs from the renderer"


def test_real_tree_reaches_every_incident_page(built):
    nodes, pages = _bfs(built)
    expected = {f"incidents/{build.filename(i)}" for i in INCIDENTS}
    assert not expected - pages, f"unreachable from catalog/README.md: {sorted(expected - pages)[:10]}"
    assert nodes == {p for p in built if p.startswith("catalog/")}, "a catalog node no link reaches"


@pytest.mark.parametrize("scope", ["catalog", "AGENTS.md", "incidents", "RULES.md+TAXONOMY.md+README.md"])
def test_every_relative_link_resolves(built, scope):
    if scope in ("catalog", "incidents"):
        paths = [p for p in built if p.startswith(scope + "/")]
    else:
        paths = scope.split("+")
    broken = []
    for path in paths:
        for raw, tgt, anchor in _targets(path, built[path]):
            if not os.path.exists(os.path.join(ROOT, tgt)):
                broken.append(f"{path}: {raw}")
            elif anchor and tgt.endswith(".md") and anchor not in _anchors(
                    built.get(tgt) or open(os.path.join(ROOT, tgt), encoding="utf-8").read()):
                broken.append(f"{path}: {raw} (no such heading)")
    assert not broken, f"{len(broken)} broken links, first: {broken[:10]}"


def test_every_incident_page_has_a_breadcrumb_to_its_node(built):
    m = build.MODEL()
    for inc in INCIDENTS:
        page = built[f"incidents/{build.filename(inc)}"]
        crumb = next(ln for ln in page.splitlines() if ln.startswith("**Catalog:** "))
        assert f"(../{m.node_of(inc)})" in crumb, inc["id"]


def test_agents_md_generated_region_matches_corpus(built):
    text = built["AGENTS.md"]
    start, end = "<!-- BEGIN GENERATED: agents-stats -->", "<!-- END GENERATED: agents-stats -->"
    assert text.count(start) == 1 and text.count(end) == 1
    region = text.split(start, 1)[1].split(end, 1)[0]
    assert f"- Incidents: {len(INCIDENTS)} (" in region
    assert f"- Failure classes: {len(CLASSES)}; topics: {len(TOPICS)}; practices: {len(PRACTICES)}." in region
    for section in ("## Read protocol", "## Write protocol", "## Provenance rules", "## Push checklist"):
        assert section in text
    for cmd in ("afm.py route", "afm.py search", "afm.py check", "afm.py show", "afm.py top", "afm.py next-id"):
        assert cmd in text, cmd


def test_readme_has_the_usage_section(built):
    assert "## Using this repository (agents and humans)" in built["README.md"]
    assert "[AGENTS.md](AGENTS.md)" in built["README.md"]


# --------------------------------------------------------------------------- budgets (real corpus)

def _budgeted() -> list[str]:
    return sorted(p for p in build.render(build.MODEL()) if p.startswith("catalog/")) + ["AGENTS.md"]


def _cap(path: str) -> int:
    return {"catalog/CORE.md": build.CORE_BUDGET, "AGENTS.md": build.AGENTS_BUDGET}.get(path, build.NODE_BUDGET)


@pytest.mark.parametrize("path", _budgeted())
def test_budget_node_fits(built, path):
    n = len(built[path].encode("utf-8"))
    assert n <= _cap(path), f"{path} is {n} bytes > {_cap(path)}; assign topics to its class"


def test_budget_core_carries_every_topic_rule():
    full, n_topics, _ = build.core_coverage(build.MODEL())
    assert full == n_topics, (f"catalog/CORE.md carries only {full} of {n_topics} topic rules within "
                              f"{build.CORE_BUDGET} bytes; shorten the topic rules")


def test_budget_caps_are_the_documented_ones():
    assert (build.NODE_BUDGET, build.CORE_BUDGET, build.AGENTS_BUDGET) == (12 * 1024, 26 * 1024, 8 * 1024)


# --------------------------------------------------------------------------- afm (library)

@pytest.fixture(scope="module")
def data():
    return afm.load()


def _canonicals():
    return [i for i in INCIDENTS if not i.get("recurrence_of")]


def test_afm_search_recall_on_own_signature(data):
    sample = random.Random(SEED).sample(_canonicals(), 30)
    misses = []
    for inc in sample:
        ids = [h[0]["id"] for h in afm.search(data, inc["signature"], k=3)]
        if inc["id"] not in ids:
            misses.append((inc["id"], ids))
    assert not misses, f"own signature not in top-3: {misses}"


def _synthetic_recurrence(inc: dict) -> str:
    """A draft that re-describes a failure in fewer words: every other word of the
    title, signature and root cause, as a writer recalling it would."""
    words = f"{inc['title']} {inc['signature']} {inc['root_cause']}".split()
    return " ".join(w for n, w in enumerate(words) if n % 2 == 0)


def test_afm_check_finds_the_canonical_for_a_synthetic_recurrence(data):
    sample = random.Random(SEED + 1).sample(_canonicals(), 30)
    misses = []
    for inc in sample:
        ids = [c["incident"]["id"] for c in afm.check(data, _synthetic_recurrence(inc), k=5)]
        if inc["id"] not in ids:
            misses.append((inc["id"], ids))
    assert not misses, f"canonical not in top-5: {misses}"


@pytest.fixture(scope="module")
def fx_data(tmp_path_factory, fx_files):
    m, files = fx_files
    root = tmp_path_factory.mktemp("afm-fixture")
    for path, text in files.items():
        os.makedirs(os.path.join(root, os.path.dirname(path)), exist_ok=True)
        open(os.path.join(root, path), "w", encoding="utf-8").write(text)
    return afm.load(str(root))


@pytest.mark.parametrize("stub,canonical", [("INC-0003", "INC-0001"), ("INC-0005", "INC-0004")])
def test_afm_check_collapses_a_recurrence_record_onto_its_canonical(fx_data, stub, canonical):
    s = fx_data["byid"][stub]
    hits = afm.check(fx_data, f"{s['title']} {s['signature']} {s['root_cause']}", k=5)
    assert hits[0]["incident"]["id"] == canonical and hits[0]["via"] == stub
    assert hits[0]["similarity"] > 0.9 > hits[1]["similarity"]
    assert all(h["incident"]["id"] != stub for h in hits), "a stub is never offered as a canonical"
    assert all(not h["incident"].get("recurrence_of") for h in hits)
    assert [h["similarity"] for h in hits] == sorted((h["similarity"] for h in hits), reverse=True)


def test_afm_route_aggregates_hits_and_node_text(fx_data):
    assert afm.route(fx_data, "a plum stall", k=3)[0]["node"] == "catalog/alpha/two.md"
    assert afm.route(fx_data, "kiwi crash", k=3)[0]["node"] == "catalog/alpha/one.md"
    # incident hits aggregate onto the node the incident lives in
    assert afm.route(fx_data, "signature text 6", k=3)[0]["node"] == "catalog/alpha/README.md"
    beta = afm.route(fx_data, "Beta failures happen quietly", k=3)
    assert beta[0]["node"] == "catalog/beta/README.md"


def test_afm_route_leave_one_out_floor(data):
    """Fixed-seed leave-one-out: each sampled canonical (and its recurrence records) is removed
    from the index and its signature routed. Measured at ROUTE_NODE_WEIGHT 3.0 on 637 incidents:
    node top-1 15/40, node top-3 22/40, home class top-3 26/40 (1.0 gave 13, 21, 25). The floors
    sit a few points below, so a regression fails and new data does not. Full numbers:
    python3 tools/eval_afm.py."""
    r = eval_afm.route_loo(data, eval_afm.route_sample(data, 40, SEED))
    assert r["n"] == 40
    assert r["node_top3"] >= 19 and r["class_top3"] >= 23, r


def test_afm_route_real_symptom(data):
    nodes = [n["node"] for n in afm.route(data, "the gate was green but the code was broken", k=3)]
    assert "catalog/false-green/README.md" in nodes or any(n.startswith("catalog/false-green/") for n in nodes)


def test_afm_top_and_search_class_filter(fx_data):
    assert [i["id"] for i in afm.top(fx_data, 2)] == ["INC-0001", "INC-0004"]
    assert all("beta" in inc["classes"] for inc, _ in afm.search(fx_data, "fixture incident", k=50, cls="beta"))


@pytest.mark.parametrize("raw,expected", [
    ("12", "INC-0012"), ("inc-12", "INC-0012"), ("INC-0012", "INC-0012"), ("inc12", "INC-0012"),
    (" 637 ", "INC-0637"), ("PRA-0001", "PRA-0001"),
])
def test_afm_normalize_id(raw, expected):
    assert afm.normalize_id(raw) == expected


def _source(tmp_path, ids, single_quoted=()) -> str:
    """A tools/corpus.py stand-in: incident dicts, some single-quoted, plus a practice."""
    lines = ["INCIDENTS = ["]
    for n in ids:
        q = "'" if n in single_quoted else '"'
        lines.append(f"    {{{q}id{q}: {q}INC-{n:04d}{q}, {q}signature{q}: {q}s{q}}},")
    lines += ["]", 'PRACTICES = [{"id": "PRA-0001", "derived_from": ["INC-0001"]}]', ""]
    path = tmp_path / "corpus.py"
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)


def _remote(monkeypatch, ids=None):
    """origin/main's index holds these ids; None means there is no origin/main."""
    out = json.dumps({"incidents": [{"id": f"INC-{n:04d}"} for n in ids or []]})
    rc = 0 if ids is not None else 128
    monkeypatch.setattr(afm.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, rc, stdout=out if rc == 0 else "", stderr=""))


def test_afm_next_id_without_a_remote(fx_data, tmp_path, monkeypatch):
    _remote(monkeypatch)
    assert afm.next_id(fx_data, _source(tmp_path, range(1, 27))) == ("INC-0027", [])


def test_afm_next_id_reads_a_newer_single_quoted_source_record_past_a_stale_index(fx_data, tmp_path, monkeypatch):
    # the fixture index ends at INC-0026; the source already has INC-0027, single-quoted, unbuilt
    _remote(monkeypatch)
    nid, warns = afm.next_id(fx_data, _source(tmp_path, range(1, 28), single_quoted={27}))
    assert nid == "INC-0028"
    assert len(warns) == 1 and "ends at INC-0026" in warns[0] and "tools/build.py" in warns[0]


def test_afm_next_id_warns_when_origin_is_ahead(fx_data, tmp_path, monkeypatch):
    _remote(monkeypatch, range(1, 31))
    nid, warns = afm.next_id(fx_data, _source(tmp_path, range(1, 27)))
    assert nid == "INC-0031" and any("INC-0030" in w and "rebase" in w for w in warns)


def test_afm_next_id_never_goes_below_the_built_index(fx_data, tmp_path, monkeypatch):
    # an index id the source no longer has is still never reused
    _remote(monkeypatch, range(1, 20))
    assert afm.next_id(fx_data, _source(tmp_path, range(1, 25)))[0] == "INC-0027"


@pytest.mark.parametrize("ids,expected", [
    ([1, 3], "missing INC-0002"),
    ([1, 2, 2, 3], "duplicated INC-0002"),
    ([2, 3], "missing INC-0001"),
])
def test_afm_next_id_refuses_a_gapped_or_duplicated_source(fx_data, tmp_path, monkeypatch, ids, expected):
    _remote(monkeypatch)
    with pytest.raises(afm.SourceError, match=expected) as exc:
        afm.next_id(fx_data, _source(tmp_path, ids))
    assert "never reuses a hole" in str(exc.value)


@pytest.mark.parametrize("text,expected", [
    ('INCIDENTS = [{"id": f"INC-{1:04d}", "signature": "s"}]', "is not a literal INC-NNNN"),
    ('INCIDENTS = [{"id": "INC-0000", "signature": "s"}]', "is not a literal INC-NNNN"),
    ("INCIDENTS = [{'id': 'INC-1'}]", "is not a literal INC-NNNN"),
    ('INCIDENTS = [{"id": "INC-0001",', "cannot read incident ids"),
    ('PRACTICES = [{"id": "PRA-0001"}]', "no incident dict literals"),
])
def test_afm_source_ids_fails_clearly(tmp_path, text, expected):
    (tmp_path / "corpus.py").write_text(text, encoding="utf-8")
    with pytest.raises(afm.SourceError, match=expected):
        afm.source_ids(str(tmp_path / "corpus.py"))
    with pytest.raises(afm.SourceError, match="cannot read"):
        afm.source_ids(str(tmp_path / "absent.py"))


def test_afm_source_ids_match_the_real_corpus_quote_independently():
    path = os.path.join(ROOT, "tools", "corpus.py")
    assert re.search(r"""["']id["']: 'INC-""", open(path, encoding="utf-8").read()), \
        "the corpus has single-quoted ids, so this test exercises them"
    assert sorted(afm.source_ids(path)) == sorted(int(i["id"][4:]) for i in INCIDENTS)


def test_afm_cli_next_id_refuses_a_gapped_source(fx_data, tmp_path, monkeypatch, capsys):
    src = _source(tmp_path, [1, 3])
    real = afm.source_ids
    monkeypatch.setattr(afm, "load", lambda: fx_data)
    monkeypatch.setattr(afm, "source_ids", lambda path: real(src))
    assert afm.main(["next-id"]) == 2
    out = capsys.readouterr()
    assert out.out == "" and "missing INC-0002" in out.err


def test_afm_load_refuses_schema_1(tmp_path):
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "incidents.json").write_text(json.dumps({"incidents": []}))
    (tmp_path / "data" / "catalog.json").write_text("{}")
    with pytest.raises(SystemExit, match="schema 1"):
        afm.load(str(tmp_path))


# --------------------------------------------------------------------------- CLI smoke, from a foreign cwd

def _cli(tmp_path, script, *args):
    return subprocess.run([sys.executable, os.path.join(ROOT, "tools", script), *args], cwd=tmp_path,
                          capture_output=True, text=True, timeout=120)


AFM_SMOKE = {
    "help": (["--help"], 0, ["search", "route", "check", "top", "show", "next-id"]),
    "search": (["search", "a gate reported green while the tests never ran"], 0, ["INC-", "rule:", "incidents/"]),
    "search-class": (["search", "killed by the timeout", "--class", "stage-timeout", "-k", "3"], 0, ["stage-timeout"]),
    "search-bad-class": (["search", "x", "--class", "no-such-class"], 2, []),
    "route": (["route", "the step was killed by the wall-clock cap"], 0, ["1. catalog/", "score"]),
    "check": (["check", "a gate reported green while the tests never ran"], 0,
              ["1. INC-", "similarity", "NOT a verdict", afm.DECISION]),
    "top": (["top", "-n", "5"], 0, ["  1. INC-", "  5. INC-"]),
    "show": (["show", "INC-0001"], 0, ["---\nid: INC-0001\n", "**Catalog:** [root](../catalog/README.md)"]),
    "show-rule": (["show", "1", "--rule"], 0, ["INC-0001 ["]),
    "show-missing": (["show", "INC-9999"], 2, []),
    "next-id": (["next-id"], 0, ["INC-"]),
    "check-no-candidates": (["check", "zzqqwwvv"], 0, [afm.NO_CANDIDATES]),
}

AFM_REJECT = {
    "search-stopwords-only": (["search", "the of and"], "no searchable word"),
    "route-whitespace": (["route", "   "], "no searchable word"),
    "check-empty": (["check", ""], "no searchable word"),
    "check-punctuation": (["check", "?! -"], "no searchable word"),
    "search-k-negative": (["search", "gate", "-k", "-1"], "must be a positive integer"),
    "route-k-zero": (["route", "gate", "-k", "0"], "must be a positive integer"),
    "check-k-not-a-number": (["check", "gate", "-k", "many"], "must be a positive integer"),
    "top-n-negative": (["top", "-n", "-1"], "must be a positive integer"),
    "top-n-zero": (["top", "-n", "0"], "must be a positive integer"),
}


@pytest.mark.parametrize("case", sorted(AFM_REJECT))
def test_afm_cli_rejects_a_query_without_words_or_a_bad_limit(tmp_path, case):
    args, needle = AFM_REJECT[case]
    r = _cli(tmp_path, "afm.py", *args)
    assert r.returncode == 2 and r.stdout == "", f"{case}: rc {r.returncode}\n{r.stdout[:500]}"
    assert needle in r.stderr and "Traceback" not in r.stderr, r.stderr


def test_afm_check_offers_only_candidates_that_share_a_word(data):
    assert afm.check(data, "zzqqwwvv") == []
    hits = afm.check(data, "a gate reported green while the tests never ran", k=50)
    assert hits and all(h["similarity"] > 0 for h in hits)


@pytest.mark.parametrize("case", sorted(AFM_SMOKE))
def test_afm_cli_smoke(tmp_path, case):
    args, rc, needles = AFM_SMOKE[case]
    r = _cli(tmp_path, "afm.py", *args)
    assert r.returncode == rc, f"{case}: rc {r.returncode}\n{r.stdout}\n{r.stderr}"
    for needle in needles:
        assert needle in r.stdout, f"{case}: {needle!r} missing from:\n{r.stdout[:2000]}"
    if case == "top":
        assert len([ln for ln in r.stdout.splitlines() if re.match(r"\s+\d+\. INC-", ln)]) == 5
    if case == "next-id":
        nid = r.stdout.strip()
        assert re.fullmatch(r"INC-\d{4}", nid)
        assert int(nid[4:]) > max(int(i["id"][4:]) for i in INCIDENTS)
        assert "git fetch origin" in r.stderr
    if case == "check-no-candidates":
        assert "1. INC-" not in r.stdout and "Read the top pages" not in r.stdout
    if case == "show-rule":
        first = next(i for i in INCIDENTS if i["id"] == "INC-0001")
        assert r.stdout.strip() == f"INC-0001 [{first['severity']}]: {first['rule']}"


# --------------------------------------------------------------------------- sync_repo_meta

def test_repo_description_quotes_current_counts():
    text = sync_repo_meta.description()
    c = sync_repo_meta.counts()
    assert len(text) <= 350 and text.endswith("Agents: start at AGENTS.md.")
    assert f"{len(INCIDENTS)} real incidents" in text
    assert f"{len(CLASSES)} failure classes" in text
    if c["stubs"]:
        assert f"({c['distinct']} distinct failures plus {c['stubs']} recorded repeats)" in text
    assert ("occurrences" in text) == (c["occurrences"] != c["incidents"])


def test_repo_description_with_repeats_and_topics():
    fx = fixture()
    c = sync_repo_meta.counts(fx["incidents"], fx["classes"], fx["topics"], fx["practices"])
    assert c == {"incidents": 26, "classes": 2, "topics": 2, "practices": 1, "distinct": 24,
                 "stubs": 2, "entries": 3, "occurrences": 29}
    assert c["occurrences"] == model(fx).total_occ()
    text = sync_repo_meta.description(c)
    assert len(text) <= 350
    assert ("26 real incidents (24 distinct failures plus 2 recorded repeats), 29 occurrences in all, "
            "across 2 failure classes and 2 topics,") in text


def test_repo_description_omits_the_occurrence_count_while_it_equals_the_incident_count():
    c = {"incidents": 637, "classes": 18, "topics": 54, "practices": 5, "distinct": 595,
         "stubs": 42, "entries": 0, "occurrences": 637}
    text = sync_repo_meta.description(c)
    assert "637 real incidents (595 distinct failures plus 42 recorded repeats) across 18" in text
    assert "occurrences" not in text and len(text) <= 350
    plain = sync_repo_meta.description({**c, "distinct": 637, "stubs": 0})
    assert "637 real incidents across 18 failure classes" in plain


def test_repo_description_never_exceeds_the_github_cap():
    huge = {"incidents": 10 ** 60, "classes": 10 ** 60, "topics": 10 ** 60, "practices": 1,
            "distinct": 10 ** 60, "stubs": 10 ** 60, "entries": 10 ** 60, "occurrences": 2 * 10 ** 60}
    text = sync_repo_meta.description(huge)
    assert len(text) <= 350 and str(10 ** 60) in text


def test_sync_repo_meta_prints_by_default_and_applies_only_on_request(monkeypatch, capsys):
    calls = []
    monkeypatch.setattr(sync_repo_meta.subprocess, "run", lambda *a, **k: calls.append(a[0]))
    assert sync_repo_meta.main([]) == 0
    assert calls == [] and capsys.readouterr().out.strip() == sync_repo_meta.description()
    assert sync_repo_meta.main(["--apply"]) == 0
    assert calls == [["gh", "repo", "edit", "--description", sync_repo_meta.description()]]


def test_sync_repo_meta_cli_smoke(tmp_path):
    r = _cli(tmp_path, "sync_repo_meta.py")
    assert r.returncode == 0 and r.stdout.strip() == sync_repo_meta.description()
