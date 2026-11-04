---
id: INC-0591
title: A triage showed a neighbouring step already at 69 percent of its limit at lower load, so the budget ruling covered it before it failed
date: 2026-11-04
classes: [stage-timeout]
severity: low
status: mitigated
---

# INC-0591 - A triage showed a neighbouring step already at 69 percent of its limit at lower load, so the budget ruling covered it before it failed

**Cost:** None. The second step was raised before it failed.

## Signature - how you recognise it

A step that passed in an earlier run used most of its hang limit at lower load than the run that failed.

## What happened

While triaging the budget change for the stopped step, the reviewer noted that a neighbouring step had taken 248.4 s in the earlier run, 69 percent of its 360 s hang limit, at lower load. With the observed 1.5 to 2 times slowdown that step would also pass its limit. The ruling raised it from 120 to 180 s (hang limit 540 s), citing the earlier measurement, and changed no other step.

## Root cause

A budget fix looked only at the step that failed, while a sibling step carried the same margin problem.

## Why it was hard to see

The sibling step had passed, so nothing signalled it.

## Fix

When one step budget is raised from measured load slowdown, check every sibling step's measured time against its limit at the observed slowdown, and raise those that would fail.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When raising one step budget for load slowdown, check each sibling step's measured share of its limit and cover any that would fail at that slowdown in the same ruling.

## Related

[INC-0590](./INC-0590-a-full-acceptance-run-stopped-at-a-step-hang-limit-with-ever.md) [INC-0551](./INC-0551-a-test-that-passed-alone-at-about-63-percent-of-its-timeout.md)
