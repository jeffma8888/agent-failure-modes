"""Invariants the corpus and its generated artifacts must always uphold."""
from __future__ import annotations
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from corpus import INCIDENTS, CLASSES, PRACTICES  # noqa: E402
from leakscan import scan_text, selftest, rules_for, PUBLIC_RULES  # noqa: E402


def test_leakscan_does_not_flag_ordinary_technical_prose():
    """Regression: short uppercase acronyms matched case-insensitively ate real words.

    'pip install pytest' tripped an HR-acronym rule, and any three-letter product
    name banned case-insensitively eats ordinary words like 'making' or 'taking'.
    Whatever a matcher is blind to deserves a test that reintroduces that case.
    """
    rules = rules_for(ROOT)
    for clean in (
        "pip install pytest",
        "run pip install -r requirements.txt",
        "making progress while taking the slower path",
        "the baking step is akin to a deadlock",
    ):
        assert scan_text(clean, rules) == [], f"false positive on {clean!r}"


def test_leakscan_selftest_two_sided():
    """The scanner itself must fire on planted hits and stay quiet on clean text.

    Runs against whatever rule set this checkout actually has: public structural
    rules everywhere, plus the operator's gitignored literal rules if present.
    A detector unproven against a known-bad sample is worthless (INC-0018).
    """
    assert selftest(PUBLIC_RULES) == []
    assert selftest(rules_for(ROOT)) == []


def test_every_incident_has_all_required_fields():
    required = {"id", "title", "date", "classes", "severity", "status", "cost",
                "signature", "what", "root_cause", "why_hard", "fix",
                "verification", "rule"}
    for inc in INCIDENTS:
        missing = required - inc.keys()
        assert not missing, f"{inc.get('id')}: missing {missing}"
        for f in required:
            assert inc[f], f"{inc['id']}: empty {f!r}"


def test_ids_are_unique_and_sequential():
    ids = [i["id"] for i in INCIDENTS]
    assert len(ids) == len(set(ids)), "duplicate incident id"
    for i, inc in enumerate(sorted(INCIDENTS, key=lambda x: x["id"]), 1):
        assert inc["id"] == f"INC-{i:04d}", f"expected INC-{i:04d}, got {inc['id']}"


def test_dates_are_iso_format():
    for inc in INCIDENTS:
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", inc["date"]), \
            f"{inc['id']}: date {inc['date']!r} is not ISO YYYY-MM-DD"


def test_severity_and_status_use_the_defined_vocabulary():
    for inc in INCIDENTS:
        assert inc["severity"] in {"low", "medium", "high", "critical"}
        assert inc["status"] in {"fixed", "mitigated", "open", "structural"}


def test_every_class_reference_is_defined():
    for inc in INCIDENTS:
        for c in inc["classes"]:
            assert c in CLASSES, f"{inc['id']}: unknown class {c!r}"


def test_every_related_id_exists():
    ids = {i["id"] for i in INCIDENTS}
    for inc in INCIDENTS:
        for r in inc.get("related", []):
            assert r in ids, f"{inc['id']}: related id {r!r} does not exist"


def test_rule_fits_in_a_prompt_line():
    """Rules ship into agent prompts; if they get long they lose their point."""
    for inc in INCIDENTS:
        n = len(inc["rule"])
        assert n <= 400, f"{inc['id']}: rule is {n} chars; keep it under 400"


def test_every_class_has_at_least_one_incident():
    """A taxonomy class with zero members should be removed or filled."""
    seen = {c for i in INCIDENTS for c in i["classes"]}
    unused = set(CLASSES) - seen
    assert not unused, f"classes with no incidents: {sorted(unused)}"


def test_incident_content_has_no_banned_tokens():
    """The scanner enforces this on files - assert it against the source of truth too."""
    for inc in INCIDENTS:
        for field in ("title", "signature", "what", "root_cause", "why_hard",
                      "fix", "verification", "rule"):
            hits = scan_text(inc[field], rules_for(ROOT))
            assert not hits, f"{inc['id']} field {field!r} leaked: {hits}"


def test_build_is_deterministic_and_idempotent():
    """Running the build twice must produce a byte-identical tree."""
    subprocess.check_call([sys.executable, "tools/build.py"], cwd=ROOT)
    before = _snapshot()
    subprocess.check_call([sys.executable, "tools/build.py"], cwd=ROOT)
    after = _snapshot()
    assert before == after, "build.py is not deterministic"


def _snapshot():
    out = {}
    for base in ("incidents", "data"):
        for dirpath, _, filenames in os.walk(os.path.join(ROOT, base)):
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                out[os.path.relpath(fp, ROOT)] = open(fp, "rb").read()
    for fn in ("RULES.md", "TAXONOMY.md"):
        out[fn] = open(os.path.join(ROOT, fn), "rb").read()
    return out


def test_incidents_json_matches_corpus():
    data = json.load(open(os.path.join(ROOT, "data", "incidents.json")))
    assert data["count"] == len(INCIDENTS)
    assert set(data["classes"]) == set(CLASSES)
    ids_in_json = {i["id"] for i in data["incidents"]}
    ids_in_corpus = {i["id"] for i in INCIDENTS}
    assert ids_in_json == ids_in_corpus


def test_every_practice_has_all_required_fields():
    """A practice with an empty field is a slogan, not guidance."""
    for pra in PRACTICES:
        for field in ("id", "title", "practice", "why", "derived_from"):
            assert pra.get(field), f"{pra.get('id')}: missing or empty {field}"


def test_practice_ids_are_unique_and_sequential():
    ids = [p["id"] for p in PRACTICES]
    assert len(ids) == len(set(ids)), "duplicate practice id"
    for n, pid in enumerate(sorted(ids), start=1):
        assert pid == f"PRA-{n:04d}", f"ids must be gapless PRA-000N; got {pid} at position {n}"


def test_practice_fits_in_a_prompt_line():
    """Practices ship into agent prompts alongside the rules, so they are bounded too."""
    for pra in PRACTICES:
        n = len(pra["practice"])
        assert n <= 600, f"{pra['id']}: practice is {n} chars; keep it under 600"


def test_every_practice_derives_from_real_incidents():
    """A practice may only cite evidence that exists in this corpus."""
    known = {i["id"] for i in INCIDENTS}
    for pra in PRACTICES:
        for ref in pra["derived_from"]:
            assert ref in known, f"{pra['id']} cites unknown incident {ref}"


def test_rules_file_carries_every_practice():
    """RULES.md is the prompt payload; a practice missing from it is not shipped."""
    text = open(os.path.join(ROOT, "RULES.md"), encoding="utf-8").read()
    assert "## Practices" in text
    for pra in PRACTICES:
        assert pra["id"] in text, f"{pra['id']} absent from RULES.md"
