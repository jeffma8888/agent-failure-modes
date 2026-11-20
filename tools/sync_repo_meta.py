#!/usr/bin/env python3
"""Keep the GitHub repository description in step with the corpus.

The description is the first thing a visitor (or an agent listing repositories)
reads, and it quotes counts. Hand-edited counts go stale the day the next incident
lands, so this computes the text from tools/corpus.py instead.

    python3 tools/sync_repo_meta.py           # print the description (default, no side effect)
    python3 tools/sync_repo_meta.py --apply   # also run: gh repo edit --description ...
"""
from __future__ import annotations
import argparse, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import INCIDENTS, CLASSES, PRACTICES, TOPICS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_LEN = 350  # GitHub caps the description at 350 characters


def counts(incidents=None, classes=None, topics=None, practices=None) -> dict[str, int]:
    """stubs: recurrence records (a repeat filed under its own id); entries: dated
    `recurrences` entries (a repeat recorded on its canonical, with no record of its own)."""
    incidents = INCIDENTS if incidents is None else incidents
    stubs = sum(1 for i in incidents if i.get("recurrence_of"))
    entries = sum(len(i.get("recurrences", [])) for i in incidents)
    return {"incidents": len(incidents),
            "classes": len(CLASSES if classes is None else classes),
            "topics": len(TOPICS if topics is None else topics),
            "practices": len(PRACTICES if practices is None else practices),
            "distinct": len(incidents) - stubs,
            "stubs": stubs,
            "entries": entries,
            "occurrences": len(incidents) + entries}


def description(c: dict[str, int] | None = None) -> str:
    """Every incident record is one occurrence, so a separate occurrence count is quoted only
    once dated entries make the two differ."""
    c = c or counts()
    split = f" ({c['distinct']} distinct failures plus {c['stubs']} recorded repeats)" if c["stubs"] else ""
    occ = f", {c['occurrences']} occurrences in all," if c["occurrences"] != c["incidents"] else ""
    topics = f" and {c['topics']} topics" if c["topics"] else ""
    text = (f"Post-mortems from autonomous multi-agent build loops in production: {c['incidents']} real "
            f"incidents{split}{occ} across {c['classes']} failure classes{topics}, each with a signature, "
            "root cause, fix and a one-line rule an agent can apply. Agents: start at AGENTS.md.")
    if len(text) > MAX_LEN:
        text = (f"{c['incidents']} post-mortems of autonomous agent-loop failures across "
                f"{c['classes']} failure classes, each with a fix and a one-line rule. "
                "Agents: start at AGENTS.md.")
    assert len(text) <= MAX_LEN, len(text)
    return text


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true", help="run gh repo edit with the description")
    a = ap.parse_args(argv)
    text = description()
    print(text)
    if a.apply:
        subprocess.run(["gh", "repo", "edit", "--description", text], cwd=ROOT, check=True)
        print("applied: gh repo edit --description", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
