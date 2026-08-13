#!/usr/bin/env python3
"""Mine role-tagged lessons out of an autonomous-loop LEARNINGS.md corpus.

Deterministic, no model calls. Classifies every lesson into failure-mode
buckets by keyword cluster, then ranks within each bucket so a human or agent
reads only the highest-signal exemplars instead of the whole 6MB corpus.
"""
from __future__ import annotations
import json, os, re, sys, collections

# Ordered: earlier classes win a tie, so put the specific ones first.
CLASSES: list[tuple[str, list[str]]] = [
    ("reward-hacking", ["reward hack", "goodhart", "novelty", "gaming the", "game the gate",
                        "clone", "duplicate command", "near-identical", "self-report",
                        "optimiz", "busywork", "manufactur"]),
    ("false-green", ["false green", "false-green", "weak test", "constant assert", "tautolog",
                     "skipped test", "test-quality", "test quality", "vacuous", "always passes",
                     "asserts nothing", "green but"]),
    ("stage-timeout", ["600s", "120s", "connection stalled", "no data received", "timed out",
                       "timeout", "stage cap", "hard cap", "wall clock", "wall-clock", "killed",
                       "stage kill"]),
    ("verdict-token", ["pushed or reverted", "action line", "parse_ship_action", "placeholder",
                       "verdict", "no token", "pending"]),
    ("steering-channel", ["learnings_digest", "digest", "patterns head", "pinned", "char budget",
                          "character budget", "truncat", "steering", "role card", "prompt injected"]),
    ("ipc-and-env", ["ipc", "endpoint", "socket", "cookie", "credential", "auth", "stale env",
                     "inherited env", "nohup", "sleep", "caffeinate", "battery", "ac power"]),
    ("concurrency", ["two loops", "two brains", "concurrent", "starve", "quota", "throttl",
                     "race", "multi-writer", "same account", "single-brain", "contention"]),
    ("vcs-destruction", ["reset --hard", "git add -a", "stash", "gitignore", "ship diff",
                         "origin/main", "force push", "discard", "clobber", "overwrote"]),
    ("delegation", ["re-delegate", "delegat", "nested", "subagent", "orphan", "hand off",
                    "handoff", "scaffold a loop"]),
    ("detector-fail-open", ["fail-open", "fail open", "grep", "ripgrep", "alternation",
                            "smart-case", "smart case", "matcher", "false negative", "regex",
                            "detector", "never fires"]),
    ("stale-module", ["reload", "importlib", "restart", "frozen", "live-lag", "live lag",
                      "inert", "imported at launch", "uptime"]),
    ("checkpoint", ["write early", "write-early", "checkpoint", "minimal output", "partial",
                    "first 3 minutes", "output file exists"]),
    ("tooling-paths", ["workspace root", "absolute path", "backtick", "command substitution",
                       "heredoc", "cd ", "path resolv"]),
    ("test-isolation", ["fresh clone", "throwaway", "precondition", "repo root", "leaks into",
                        "isolation", "hardcoded", "basename"]),
    ("observability", ["median", "duration distribution", "telemetry", "cputime", "%cpu",
                       "sampling", "measure", "instrument"]),
    ("spec-and-scope", ["spec", "scope", "roadmap", "story", "acceptance", "dormant",
                        "additive-dormant", "bite"]),
]

ROLE_RE = re.compile(r"^\s*-\s*\[([A-Z][A-Z-]*)\s*([a-zA-Z]*\d*)\]\s*(.*)$")
OPHEAD_RE = re.compile(r"^\s*-\s*\*\*(OPERATOR[^*]*)\*\*\s*(.*)$")
OPSEC_RE = re.compile(r"^##+\s*\[?(OPERATOR[^\]]*)\]?\s*(.*)$")


def classify(text: str) -> list[str]:
    low = text.lower()
    return [name for name, kws in CLASSES if any(k in low for k in kws)]


def signal(text: str, tags: list[str], is_operator: bool) -> float:
    """Heuristic: operator directives and explicit root-cause language rank highest."""
    low = text.lower()
    s = 0.0
    if is_operator:
        s += 60
    for k in ("root cause", "the fix", "never ", "must ", "rule:", "lesson",
              "silently", "destroyed", "lost", "wrong", "proven", "confirmed",
              "incident", "why ", "because"):
        if k in low:
            s += 6
    s += min(len(text) / 90.0, 40)          # detail, capped
    s += 8 * (len(tags) - 1 if tags else 0)  # cross-cutting lessons are richer
    if low.count(".") >= 3:
        s += 6
    return s


def mine(base: str) -> dict:
    prods = [d for d in sorted(os.listdir(base))
             if os.path.isfile(os.path.join(base, d, "LEARNINGS.md"))]
    records = []
    for prod in prods:
        fp = os.path.join(base, prod, "LEARNINGS.md")
        lines = open(fp, encoding="utf-8", errors="replace").read().split(chr(10))
        section = ""
        for i, line in enumerate(lines, 1):
            if line.startswith("#"):
                section = line.lstrip("#").strip()
            m = ROLE_RE.match(line)
            is_op = False
            if m:
                role, it, body = m.group(1), m.group(2), m.group(3)
            else:
                m2 = OPHEAD_RE.match(line) or OPSEC_RE.match(line)
                if not m2:
                    continue
                role, it, body, is_op = "OPERATOR", "", (m2.group(1) + " " + m2.group(2)), True
            body = body.strip()
            if len(body) < 40:
                continue
            tags = classify(body)
            records.append({
                "product": prod, "file": fp, "line": i, "role": role, "iter": it,
                "section": section, "operator": is_op, "tags": tags or ["unclassified"],
                "chars": len(body), "signal": round(signal(body, tags, is_op), 1),
                "text": body,
            })
    return {"products": prods, "records": records}


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("AFM_CORPUS", "")
    if not base:
        print("usage: mine_learnings.py <corpus-dir> [out.json]   (or set AFM_CORPUS)")
        print("corpus-dir holds <product>/LEARNINGS.md files. Paths are intentionally")
        print("not hardcoded: the source corpus is private and machine-local.")
        return 2
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(".local", "mined.json")
    data = mine(base)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)

    recs = data["records"]
    per = collections.Counter(t for r in recs for t in r["tags"])
    print(f"records={len(recs)}  products={len(data['products'])}  -> {out}")
    print()
    print(f"{'class':22s} {'n':>5s}  {'top signal':>10s}")
    for name, _ in CLASSES + [("unclassified", [])]:
        sub = [r for r in recs if name in r["tags"]]
        if not sub:
            continue
        print(f"{name:22s} {per[name]:5d}  {max(r['signal'] for r in sub):10.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
