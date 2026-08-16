#!/usr/bin/env python3
"""Proactively watch live agent loops and surface NEW failure lessons as incident candidates.

`mine_learnings.py` answers "what is in the whole corpus" - a reactive, one-shot
census. This answers the operational question instead: "what did my loops learn
SINCE I last looked, and does any of it deserve an incident?" Run it on a
schedule and the knowledge base stays current with the loops instead of being
reconstructed from a 6MB log weeks later.

Design mirrors the loops it watches: a pure core (fingerprint / select_new /
render) with two I/O seams (state load+save, corpus mine), so every decision is
testable offline with no filesystem or model calls.

Paths are never hardcoded - the watched corpus is machine-local and may contain
PRIVATE product names, so all output goes to the gitignored `.local/` directory
and nothing from it belongs in a commit.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

DEFAULT_THRESHOLD = 130.0   # empirical p95 of the observed signal distribution
STATE_PATH = os.path.join(ROOT, ".local", "watch_state.json")
REPORT_PATH = os.path.join(ROOT, ".local", "watch-latest.md")


def fingerprint(rec: dict) -> str:
    """Stable identity for a lesson, independent of its LINE NUMBER.

    Line numbers shift whenever anything above a lesson is edited, so keying on
    them would re-report the whole file after any insert. Product + role +
    iteration + the lesson text is stable under edits elsewhere in the file.
    """
    key = "|".join(str(rec.get(k, "")) for k in ("product", "role", "iter", "text"))
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def corpus_coverage() -> dict[str, int]:
    """How many incidents the knowledge base already has per failure class."""
    from corpus import INCIDENTS, CLASSES
    cov = {c: 0 for c in CLASSES}
    for inc in INCIDENTS:
        for c in inc["classes"]:
            cov[c] = cov.get(c, 0) + 1
    return cov


def select_new(records: list[dict], seen: set[str], threshold: float) -> list[dict]:
    """New-since-last-run lessons at or above the signal threshold, strongest first.

    Pure: no I/O. `seen` is the watermark. Ties break on fingerprint so the order
    is deterministic for a given input set.
    """
    out = [r for r in records
           if fingerprint(r) not in seen and float(r.get("signal", 0)) >= threshold]
    return sorted(out, key=lambda r: (-float(r["signal"]), fingerprint(r)))


def priority(rec: dict, coverage: dict[str, int]) -> str:
    """Triage label. Thin or absent corpus coverage is what makes a lesson urgent.

    An `unclassified` lesson is the most interesting case: the miner's 16 classes
    did not match it, which is weak evidence of a failure mode the taxonomy does
    not yet name.
    """
    tags = rec.get("tags") or ["unclassified"]
    if tags == ["unclassified"]:
        return "NEW-CLASS?"
    thinnest = min(coverage.get(t, 0) for t in tags)
    if thinnest == 0:
        return "UNCOVERED"
    if thinnest == 1:
        return "THIN"
    return "covered"


def render(new: list[dict], coverage: dict[str, int], threshold: float,
           products: list[str], total: int) -> str:
    """Markdown digest of the new lessons, highest-priority first."""
    nl = chr(10)
    rank = {"NEW-CLASS?": 0, "UNCOVERED": 1, "THIN": 2, "covered": 3}
    lines = [
        "# Loop watch - new failure lessons",
        "",
        f"- scanned: {total} lessons across {len(products)} live loops",
        f"- new since last run at or above signal {threshold:g}: **{len(new)}**",
        f"- generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    if not new:
        lines += ["Nothing new above the threshold. No action needed.", ""]
        return nl.join(lines)
    by = collections.Counter(priority(r, coverage) for r in new)
    lines += ["Triage: " + ", ".join(f"{k}={v}" for k, v in sorted(by.items(), key=lambda kv: rank.get(kv[0], 9))), ""]
    for rec in sorted(new, key=lambda r: (rank.get(priority(r, coverage), 9), -float(r["signal"]))):
        pr = priority(rec, coverage)
        head = f"## [{pr}] signal {rec['signal']} - {'/'.join(rec.get('tags') or [])}"
        lines += [head, "",
                  f"- role `{rec.get('role')}` iteration `{rec.get('iter') or '-'}`, line {rec.get('line')}",
                  f"- fingerprint `{fingerprint(rec)}`",
                  "",
                  "> " + rec["text"].replace(chr(10), " ").strip()[:1200],
                  ""]
    lines += ["---", "",
              "**How to act on this.** A lesson is worth an incident when it is transferable: it would",
              "bite a different framework, not just this one. Promote it by adding a record to",
              "`tools/corpus.py` (with a `evidence` entry naming the PUBLIC repo it came from) and",
              "running `python3 tools/build.py`. Leave the rest here - the watermark means you will",
              "not be shown them again.", ""]
    return nl.join(lines)


def load_state(path: str = STATE_PATH) -> dict:
    if not os.path.exists(path):
        return {"seen": [], "last_run": None, "runs": 0}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state: dict, path: str = STATE_PATH) -> None:
    """Atomic: a crash mid-write must not leave a truncated watermark, which would
    re-report every lesson in the corpus on the next run."""
    import tempfile
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(state, fh)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("corpus_dir", nargs="?", default=os.environ.get("AFM_CORPUS", ""),
                    help="directory holding <product>/LEARNINGS.md (or set AFM_CORPUS)")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    ap.add_argument("--baseline", action="store_true",
                    help="seed the watermark from the current corpus and report nothing")
    ap.add_argument("--state", default=STATE_PATH)
    ap.add_argument("--report", default=REPORT_PATH)
    args = ap.parse_args(argv)
    if not args.corpus_dir:
        ap.error("no corpus dir: pass it as an argument or set AFM_CORPUS")

    from mine_learnings import mine
    data = mine(args.corpus_dir)
    records, products = data["records"], data["products"]

    state = load_state(args.state)
    seen = set(state.get("seen", []))
    first_run = not seen
    new = select_new(records, seen, args.threshold)

    if args.baseline or first_run:
        save_state({"seen": sorted({fingerprint(r) for r in records}),
                    "last_run": time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "runs": state.get("runs", 0) + 1}, args.state)
        why = "--baseline" if args.baseline else "first run (no watermark yet)"
        print(f"baseline set from {len(records)} lessons across {len(products)} loops ({why}); "
              f"reporting nothing. Next run reports only what is new.")
        return 0

    report = render(new, corpus_coverage(), args.threshold, products, len(records))
    os.makedirs(os.path.dirname(args.report), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as fh:
        fh.write(report)
    save_state({"seen": sorted(seen | {fingerprint(r) for r in records}),
                "last_run": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "runs": state.get("runs", 0) + 1}, args.state)

    cov = corpus_coverage()
    counts = collections.Counter(priority(r, cov) for r in new)
    print(f"scanned {len(records)} lessons / {len(products)} loops; "
          f"{len(new)} new at signal >= {args.threshold:g} -> {args.report}")
    for k in ("NEW-CLASS?", "UNCOVERED", "THIN", "covered"):
        if counts[k]:
            print(f"  {k:11s} {counts[k]}")
    return 3 if any(counts[k] for k in ("NEW-CLASS?", "UNCOVERED", "THIN")) else 0


if __name__ == "__main__":
    raise SystemExit(main())
