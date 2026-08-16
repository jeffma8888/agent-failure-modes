"""Invariants for the proactive loop watcher.

The watcher's whole value is that it reports each lesson ONCE. Two failures
would silently destroy that: a fingerprint that moves when unrelated lines are
edited (re-reports everything), and a truncated watermark (same effect). Both
are covered here, plus a two-sided threshold check - a detector that only ever
fires, or never fires, is worthless.
"""
from __future__ import annotations
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import watch_loops as W  # noqa: E402


def rec(text="a lesson body long enough to be mined by the miner", product="p1",
        role="FINAL", it="iter07", signal=150.0, tags=None, line=42):
    return {"product": product, "role": role, "iter": it, "text": text,
            "signal": signal, "tags": tags if tags is not None else ["stage-timeout"],
            "line": line}


def test_fingerprint_ignores_line_number_but_not_identity():
    a = rec(line=10)
    b = rec(line=999)
    assert W.fingerprint(a) == W.fingerprint(b), "line number must not change identity"
    assert W.fingerprint(rec(product="p2")) != W.fingerprint(a)
    assert W.fingerprint(rec(text="different")) != W.fingerprint(a)
    assert W.fingerprint(rec(it="iter08")) != W.fingerprint(a)


def test_select_new_is_two_sided_on_the_watermark():
    a, b = rec(text="alpha"), rec(text="beta")
    assert len(W.select_new([a, b], set(), 100.0)) == 2, "must fire on unseen records"
    seen = {W.fingerprint(a)}
    got = W.select_new([a, b], seen, 100.0)
    assert [r["text"] for r in got] == ["beta"], "must stay silent on seen records"
    assert W.select_new([a, b], {W.fingerprint(a), W.fingerprint(b)}, 100.0) == []


def test_select_new_is_two_sided_on_the_threshold():
    hi, lo = rec(text="hi", signal=200.0), rec(text="lo", signal=5.0)
    assert [r["text"] for r in W.select_new([hi, lo], set(), 130.0)] == ["hi"]
    assert len(W.select_new([hi, lo], set(), 1.0)) == 2


def test_select_new_orders_strongest_first_and_is_deterministic():
    recs = [rec(text="weak", signal=131.0), rec(text="strong", signal=180.0)]
    once = [r["text"] for r in W.select_new(recs, set(), 130.0)]
    twice = [r["text"] for r in W.select_new(list(reversed(recs)), set(), 130.0)]
    assert once == ["strong", "weak"] and once == twice


def test_priority_escalates_on_thin_corpus_coverage():
    cov = {"stage-timeout": 5, "checkpoint": 1, "observability": 0}
    assert W.priority(rec(tags=["unclassified"]), cov) == "NEW-CLASS?"
    assert W.priority(rec(tags=["observability"]), cov) == "UNCOVERED"
    assert W.priority(rec(tags=["checkpoint"]), cov) == "THIN"
    assert W.priority(rec(tags=["stage-timeout"]), cov) == "covered"
    # the THINNEST covered class wins, so a cross-cutting lesson is not hidden
    assert W.priority(rec(tags=["stage-timeout", "observability"]), cov) == "UNCOVERED"


def test_render_says_so_when_there_is_nothing_new():
    out = W.render([], {"stage-timeout": 3}, 130.0, ["p1"], 100)
    assert "Nothing new above the threshold" in out
    assert "signal" in out


def test_render_puts_the_most_urgent_first_and_quotes_the_lesson():
    cov = {"stage-timeout": 9, "observability": 0}
    new = [rec(text="covered one", tags=["stage-timeout"], signal=180.0),
           rec(text="uncovered one", tags=["observability"], signal=131.0)]
    out = W.render(new, cov, 130.0, ["p1"], 100)
    assert out.index("uncovered one") < out.index("covered one"), \
        "an UNCOVERED class must outrank a higher signal in a covered class"
    assert "[UNCOVERED]" in out and "[covered]" in out


def test_state_round_trips_and_first_run_baselines_without_reporting(tmp_path):
    products = tmp_path / "products"
    (products / "prod-a").mkdir(parents=True)
    (products / "prod-a" / "LEARNINGS.md").write_text(
        "## Patterns" + chr(10) * 2 +
        "- [FINAL iter07] a genuinely long lesson body about a stage that timed out and "
        "destroyed work, with root cause and the fix, proven and confirmed." + chr(10),
        encoding="utf-8")
    state = tmp_path / "state.json"
    report = tmp_path / "out.md"
    rc = W.main([str(products), "--state", str(state), "--report", str(report)])
    assert rc == 0
    assert state.exists() and not report.exists(), "first run must seed only, never report"
    seeded = json.loads(state.read_text())
    assert len(seeded["seen"]) == 1 and seeded["runs"] == 1

    # second run with no new lessons: reports, finds nothing, keeps the watermark
    rc2 = W.main([str(products), "--state", str(state), "--report", str(report)])
    assert rc2 == 0 and report.exists()
    assert "Nothing new above the threshold" in report.read_text()
    assert len(json.loads(state.read_text())["seen"]) == 1


def test_a_newly_appended_lesson_is_reported_exactly_once(tmp_path):
    products = tmp_path / "products"
    (products / "prod-a").mkdir(parents=True)
    fp = products / "prod-a" / "LEARNINGS.md"
    fp.write_text("- [FINAL iter07] " + "an established lesson " * 8 + chr(10), encoding="utf-8")
    state, report = tmp_path / "s.json", tmp_path / "r.md"
    W.main([str(products), "--state", str(state), "--report", str(report)])  # baseline

    fp.write_text(fp.read_text(encoding="utf-8") +
                  "- [FINAL iter08] NEVER ship this again: the root cause was a destroyed tree "
                  "and the fix is proven, confirmed, and must be enforced because it silently lost work." + chr(10),
                  encoding="utf-8")
    W.main([str(products), "--state", str(state), "--report", str(report), "--threshold", "50"])
    assert "iter08" in report.read_text(), "a new lesson must be reported"
    W.main([str(products), "--state", str(state), "--report", str(report), "--threshold", "50"])
    assert "Nothing new above the threshold" in report.read_text(), \
        "the same lesson must never be reported twice"
