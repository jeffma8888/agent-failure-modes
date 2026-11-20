#!/usr/bin/env python3
"""Leave-one-out retrieval measurement for tools/afm.py. Stdlib only; reads the built data.

route: hold out a sampled canonical incident together with its recurrence records,
query its signature, and report how often the node it lives in ranks first and in the
top 3, and how often its home class (the class node or one of its topics) is in the top 3.

check: hold out each recurrence record in turn, query its title + signature + root cause,
and report how often its canonical ranks first, in the top 3 and in the top 5.

Held-out records are removed from the index, which is rebuilt for every query. These are
measurements, not verdicts: lexical retrieval cannot prove a recurrence.

    python3 tools/eval_afm.py [--seed 20261119] [-n 120] [--node-weight W]
"""
from __future__ import annotations
import argparse, os, random, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import afm  # noqa: E402


def held_out(data: dict, drop: set[str]) -> dict:
    """A copy of the loaded data without the dropped records (no cached index)."""
    incs = [i for i in data["incidents"] if i["id"] not in drop]
    return {**{k: v for k, v in data.items() if k != "_idx"},
            "incidents": incs, "byid": {i["id"]: i for i in incs}}


def route_loo(data: dict, sample: list[dict]) -> dict[str, int]:
    out = {"n": len(sample), "node_top1": 0, "node_top3": 0, "class_top3": 0}
    for inc in sample:
        drop = {inc["id"]} | {i["id"] for i in data["incidents"] if i.get("recurrence_of") == inc["id"]}
        nodes = afm.route(held_out(data, drop), inc["signature"], k=3)
        names = [n["node"] for n in nodes]
        home = inc["classes"][0]
        out["node_top1"] += bool(names) and names[0] == inc["node"]
        out["node_top3"] += inc["node"] in names
        out["class_top3"] += any(n["where"] == home or n["where"].startswith(home + "/") for n in nodes)
    return out


def check_loo(data: dict, stubs: list[dict]) -> dict[str, int]:
    out = {"n": len(stubs), "top1": 0, "top3": 0, "top5": 0}
    for stub in stubs:
        draft = f"{stub['title']} {stub['signature']} {stub['root_cause']}"
        ids = [c["incident"]["id"] for c in afm.check(held_out(data, {stub["id"]}), draft, k=5)]
        for k in (1, 3, 5):
            out[f"top{k}"] += stub["recurrence_of"] in ids[:k]
    return out


def route_sample(data: dict, n: int, seed: int) -> list[dict]:
    canon = sorted((i for i in data["incidents"] if not i.get("recurrence_of")), key=lambda i: i["id"])
    return random.Random(seed).sample(canon, min(n, len(canon)))


def _pct(hit: int, n: int) -> str:
    return f"{hit}/{n} ({100 * hit / n:.1f}%)" if n else "0/0"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--seed", type=int, default=20261119)
    ap.add_argument("-n", type=int, default=120, help="route sample size (canonical incidents)")
    ap.add_argument("--node-weight", type=float, help="override afm.ROUTE_NODE_WEIGHT for this run")
    a = ap.parse_args(argv)
    if a.node_weight is not None:
        afm.ROUTE_NODE_WEIGHT = a.node_weight
    data = afm.load()
    t0 = time.perf_counter()
    r = route_loo(data, route_sample(data, a.n, a.seed))
    t1 = time.perf_counter()
    c = check_loo(data, [i for i in data["incidents"] if i.get("recurrence_of")])
    t2 = time.perf_counter()
    print(f"route LOO  seed {a.seed}, node weight {getattr(afm, 'ROUTE_NODE_WEIGHT', 1.0)}: "
          f"node top-1 {_pct(r['node_top1'], r['n'])}, node top-3 {_pct(r['node_top3'], r['n'])}, "
          f"home-class top-3 {_pct(r['class_top3'], r['n'])}  [{t1 - t0:.1f}s]")
    print(f"check LOO  every recurrence record: canonical top-1 {_pct(c['top1'], c['n'])}, "
          f"top-3 {_pct(c['top3'], c['n'])}, top-5 {_pct(c['top5'], c['n'])}  [{t2 - t1:.1f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
