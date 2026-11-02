---
id: INC-0450
title: A load gate stop was the right call and cost nothing because the runner created nothing before the check
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0450 - A load gate stop was the right call and cost nothing because the runner created nothing before the check

**Cost:** None: nothing was created, and the walk was re-dispatched later.

## Signature - how you recognise it

A run stopped at the gate while the host was overloaded.

## What happened

the runner of a milestone walk stopped at its first step because host load read 48.87 and then 38.48, above the gate, with nothing created and nothing to tear down; the load came from processes outside the team, which nobody touches; the lead called the stop correct and re-dispatches the walk when the gate reads low

## Root cause

host load rose from processes outside the team

## Why it was hard to see

Stopping felt like lost time, and it was the cheap outcome.

## Fix

put the load check before any creation in a runner, so a stop leaves nothing to tear down, and re-dispatch when the gate reads low

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put the load check before anything is created, so a gate stop costs nothing and leaves nothing to tear down

## Related

[INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) [INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) [INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0452](./INC-0452-a-ruling-cannot-override-a-teammate-tool-rules-so-the-lead-s.md)
