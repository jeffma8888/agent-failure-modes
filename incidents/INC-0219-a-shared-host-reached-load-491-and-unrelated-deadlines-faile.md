---
id: INC-0219
title: A shared host reached load 491 and unrelated deadlines failed
date: 2026-10-31
classes: [concurrency, stage-timeout]
severity: medium
status: fixed
---

# INC-0219 - A shared host reached load 491 and unrelated deadlines failed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Unrelated deadlines failed under a shared load.

## What happened

The cap on heavy runs was per worker, so the team total overloaded the host to a load of 491.

## Root cause

The cap on heavy runs was per worker, so the team total overloaded the host to a load of 491.

## Why it was hard to see

Each worker kept to its own limit.

## Fix

Cap concurrent heavy runs across a team, not per worker (two), and record load at start and end with any overlap

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Cap concurrent heavy runs across the team and record load at start and end

## Related

[INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) [INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) [INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) [INC-0435](./INC-0435-a-low-load-window-needed-immediate-dispatch-of-the-gated-run.md) [INC-0445](./INC-0445-a-migration-lock-covered-the-whole-branch-when-it-needed-to.md)
