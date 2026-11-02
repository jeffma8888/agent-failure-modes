---
id: INC-0491
title: A browser walker gathered guards over many static rounds until no allowed target could pass them
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0491 - A browser walker gathered guards over many static rounds until no allowed target could pass them

**Cost:** Six review rounds spent on a tool that never ran, and a milestone click-around duty left unmet meanwhile.

## Signature - how you recognise it

A diagnostic run packet showed the tool could not run against any allowed target.

## What happened

A browser walk harness collected a new guard in every static review round. By the sixth round it hard-coded a database name and port, required four migrations, needed a signed bindings file whose exact text nobody had sourced, and expected a fixed origin the harness could not provide. A diagnostic packet showed that no allowed target could pass its guards. The tool was parked, and its duty was split: the browser tier that runs on every full run became the regression gate, and a plain checklist click-around on a scratch server became a per-milestone report that is not a gate.

## Root cause

Each round added a guard that was reasonable alone, and nobody checked whether the guards together left any target that could pass.

## Why it was hard to see

Every guard had a good reason and every round produced a revision, so the loop looked like progress while the tool was never run.

## Fix

Park the tool, gate regressions in the tier that already runs on every full run, and do the exploratory pass against a plain sourced checklist, with every mismatch becoming a backlog row.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a test tool's guards are reviewed in more rounds than the tool is run, run it or simplify it; a guard that no allowed target can pass is a defect.

## Related

[INC-0488](./INC-0488-static-review-rounds-on-a-test-harness-left-the-same-finding.md) [INC-0382](./INC-0382-a-click-around-walk-that-always-exits-1-from-a-known-gap-can.md)
