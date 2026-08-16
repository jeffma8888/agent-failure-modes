---
id: INC-0021
title: Stale module import: 'shipped' is not 'live'
date: 2026-08-10
classes: [stale-module, observability]
severity: high
status: mitigated
---

# INC-0021 - Stale module import: 'shipped' is not 'live'

**Cost:** Twenty-six commits to a shared module were reported as SHIPPED by git and the changelog while all of them were inert in the running process for four days.

## Signature - how you recognise it

A long-running dispatcher's uptime is measured in days. `git log --since=<start>` on the module it imported shows dozens of commits since. The behavior on disk does not match what the process seems to be running.

## What happened

In the public agent-foundry loop framework, the dispatcher process did a plain `import foundry` once at launch, with no `importlib.reload` and no self-restart. Over four days, 26 commits to `foundry.py` landed. All 26 were inert - the process was still running the code it imported at launch. Git, the roadmap and the decision log all reported them SHIPPED.

## Root cause

Python's import machinery caches modules by name. Without an explicit reload or a process restart, `import foundry` returns the object bound at first import forever. Even a self-modifying loop that ships fixes to its own code does not run those fixes.

## Why it was hard to see

Everything upstream reports success. The commits merged; the tests were green; the changelog says SHIPPED. Only a comparison of process start-time against git log for the imported module reveals the gap.

## Fix

For any long-running process that imports code it may also modify, ship a live-lag check: compare `psutil.Process(pid).create_time()` against `git log --since` for the imported module. Distinguish disk-level changes from live-behavior changes explicitly - role or prompt CARDS read from disk per run ARE live even when the module is frozen. Design self-updating loops with a scheduled restart or an in-process reload primitive, not on the assumption that the next iteration picks up new code.

## Verification

The live-lag check surfaced the four-day gap and warned before further inert commits accumulated. Post-restart, the same 26 commits took effect.

## Transferable rule

> A long-running process runs the code it imported AT LAUNCH. Merged is not shipped is not live: git can say 'landed' while the process is still on the old bytecode. Ship a live-lag check that compares process start-time against `git log --since` on the imported module. Role/prompt files read per-run ARE live even when the module is frozen - distinguish them.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the dispatcher does a plain `import foundry` once at launch, with no reload primitive and no self-restart.
- Second confirmation, 2026-08-15: a live dispatcher with 1d22h uptime was still running the module revision it imported at launch while the repository head had moved on by many commits. Every prompt-budget constant measured from the working tree was therefore the wrong number for the running loop - so a stale module silently invalidates measurements taken about it, not just fixes shipped to it.

## Related

[INC-0007](./INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md)
