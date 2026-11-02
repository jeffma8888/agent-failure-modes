---
id: INC-0427
title: A host load spike came from operating system daemons, not the team, and the load wait held
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0427 - A host load spike came from operating system daemons, not the team, and the load wait held

**Cost:** Runs waited; no run started on an overloaded host.

## Signature - how you recognise it

Host load was far above the gate while no team run was active.

## What happened

host load1 read 131.65, driven by operating system background daemons and not by any teammate run; the load wait applied to every run, static work continued, and the lead did not touch the system daemons

## Root cause

operating system daemons raised the load without any team action

## Why it was hard to see

There was nothing of the team's to stop, and the temptation was to start anyway.

## Fix

hold every run behind the load gate whatever the source of the load, keep static work going, and leave system processes alone

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A load gate holds regardless of who causes the load; continue static work and do not touch system daemons

## Related

[INC-0271](./INC-0271-a-load-induced-harness-red-is-not-headroom.md) [INC-0219](./INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md) [INC-0195](./INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md) [INC-0450](./INC-0450-a-load-gate-stop-was-the-right-call-and-cost-nothing-because.md)
