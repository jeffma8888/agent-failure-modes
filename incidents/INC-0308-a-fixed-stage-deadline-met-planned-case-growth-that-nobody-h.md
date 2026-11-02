---
id: INC-0308
title: A fixed stage deadline met planned case growth that nobody had projected
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0308 - A fixed stage deadline met planned case growth that nobody had projected

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A stage deadline measured at 24 cases was about to carry 105.

## What happened

a stage deadline measured at one case count was kept while the acceptance checklist planned to more than quadruple the cases in that stage, so the breach would have shown up only as the first timeout

## Root cause

a stage deadline measured at one case count was kept while the acceptance checklist planned to more than quadruple the cases in that stage, so the breach would have shown up only as the first timeout

## Why it was hard to see

The deadline passes today and the growth arrives row by row in other people's work, so no single row looks responsible.

## Fix

Project the stage time per rung from the acceptance checklist and decide who re-measures before the load, not after the first timeout

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When an acceptance checklist adds cases to a bounded stage, project the stage time per rung and decide who re-measures before the load, not after the first timeout

## Related

[INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) [INC-0290](./INC-0290-a-setup-hook-was-sized-from-file-time-or-from-a-refused-atte.md) [INC-0291](./INC-0291-a-known-unrelated-load-timeout-blocked-a-row-until-one-combi.md) [INC-0312](./INC-0312-a-whole-stage-was-divided-by-a-parallel-speedup-although-par.md)
