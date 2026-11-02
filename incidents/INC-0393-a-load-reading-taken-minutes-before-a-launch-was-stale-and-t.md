---
id: INC-0393
title: A load reading taken minutes before a launch was stale, and the launch read much higher
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0393 - A load reading taken minutes before a launch was stale, and the launch read much higher

**Cost:** A heavy run nearly started on a host whose load had risen well past the gate.

## Signature - how you recognise it

A load gate passed from a reading that no longer described the host.

## What happened

a load reading taken minutes before a launch is stale: the lead's gate read low, the launch read far higher shortly after, and the engineer correctly refused the lead's reading as a substitute

## Root cause

the reading was taken minutes earlier and by someone else, and load changes within minutes

## Why it was hard to see

A low reading from a trusted source looks like a valid gate.

## Fix

Gate at the point of launch, immediately before it; do not accept another party's earlier reading

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Gate on load where you launch, immediately before; an earlier or second-hand reading is stale

## Related

[INC-0219](./INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md) [INC-0271](./INC-0271-a-load-induced-harness-red-is-not-headroom.md) [INC-0406](./INC-0406-two-load-readings-around-a-sub-second-run-were-equal-because.md) [INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) [INC-0435](./INC-0435-a-low-load-window-needed-immediate-dispatch-of-the-gated-run.md) [INC-0450](./INC-0450-a-load-gate-stop-was-the-right-call-and-cost-nothing-because.md)
