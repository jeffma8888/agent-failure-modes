---
id: INC-0435
title: A low-load window needed immediate dispatch of the gated runs
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0435 - A low-load window needed immediate dispatch of the gated runs

**Cost:** Minor: an unused window delays every held run.

## Signature - how you recognise it

Gated runs waited while a short low-load window was open.

## What happened

a low-load window opened for the runs held behind the load gate, and the lead dispatched them immediately because the window is short and the gate must be read immediately before each launch

## Root cause

the window is brief and unpredictable, and the gated runs are not started on their own

## Why it was hard to see

The window closes without notice.

## Fix

when the load drops below the gate, dispatch the gated runs at once, reading the load in its own command before each launch

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a low-load window opens, dispatch the gated runs at once, reading the load in its own command before each launch

## Related

[INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0219](./INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md)
