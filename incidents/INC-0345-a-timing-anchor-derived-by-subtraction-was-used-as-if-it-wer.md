---
id: INC-0345
title: A timing anchor derived by subtraction was used as if it were a measurement
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0345 - A timing anchor derived by subtraction was used as if it were a measurement

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A budget model anchored on a stage time obtained by subtraction, while quiet measured samples were higher.

## What happened

a time-budget model used a 51 s stage time derived by subtracting moved-file sums from a loaded run; three quiet measured samples were 53.9 to 60.0 s, which moved the first projected crossing of the target earlier and showed a later stage deadline would be passed

## Root cause

a time-budget model used a 51 s stage time derived by subtracting moved-file sums from a loaded run; three quiet measured samples were 53.9 to 60.0 s, which moved the first projected crossing of the target earlier and showed a later stage deadline would be passed

## Why it was hard to see

A derived number looks like data, and every other term in the model inherits its error.

## Fix

Replace the anchor with the measured maximum, label every other term inferred, and recompute every rung

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Replace a derived timing anchor with a measured one as soon as the thing exists, and recompute every threshold it feeds

## Related

[INC-0195](./INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md) [INC-0312](./INC-0312-a-whole-stage-was-divided-by-a-parallel-speedup-although-par.md) [INC-0348](./INC-0348-a-deadline-set-at-twice-the-slowest-sample-was-budgeted-agai.md)
