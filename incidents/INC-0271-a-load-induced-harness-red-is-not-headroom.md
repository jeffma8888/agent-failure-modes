---
id: INC-0271
title: A load-induced harness red is not headroom
date: 2026-11-01
classes: [stage-timeout, false-green]
severity: medium
status: fixed
---

# INC-0271 - A load-induced harness red is not headroom

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A run stopped early under load and its remaining time looked like spare budget.

## What happened

the rehearsal stopped on a real harness red under host load 41 to 71 (a process snapshot with a 3000 ms timeout returned ETIMEDOUT) and correctly refused to count the 95 s distance to the budget as headroom, because the later runners never ran

## Root cause

the rehearsal stopped on a real harness red under host load 41 to 71 (a process snapshot with a 3000 ms timeout returned ETIMEDOUT) and correctly refused to count the 95 s distance to the budget as headroom, because the later runners never ran

## Why it was hard to see

The arithmetic distance is true but not usable.

## Fix

Report the run as not passing and name the stage that never ran

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not count the arithmetic distance to a budget as headroom when later stages never ran

## Related

[INC-0236](./INC-0236-a-blocked-result-came-from-a-deadline-before-the-plant-ran.md) [INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0406](./INC-0406-two-load-readings-around-a-sub-second-run-were-equal-because.md) [INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md)
