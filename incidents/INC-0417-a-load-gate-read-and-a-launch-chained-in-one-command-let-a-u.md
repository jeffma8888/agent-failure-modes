---
id: INC-0417
title: A load gate read and a launch chained in one command let a unit probe start at a load above the gate
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0417 - A load gate read and a launch chained in one command let a unit probe start at a load above the gate

**Cost:** One short probe ran above the gate and was recorded as a breach.

## Signature - how you recognise it

A probe started on a host whose load was far above the gate.

## What happened

a load gate read and a launch chained in one command let a unit probe start at load1 42.87, above the unit gate of 24; the breach was recorded, not hidden, and the result stood only as a suite-level module error

## Root cause

the gate read and the launch were chained, so the chained launch ran whatever the read showed

## Why it was hard to see

A chained command looks like a gate but cannot stop itself on the reading it just took.

## Fix

run the load read as its own command and the launch as a separate command; a reading at or above the gate stops the launch

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the load read and the launch as two separate commands; a reading at or above the gate stops the launch

## Related

[INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0406](./INC-0406-two-load-readings-around-a-sub-second-run-were-equal-because.md) [INC-0219](./INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md)
