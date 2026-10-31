---
id: INC-0143
title: Two branches implementing the same stage split were merged without re-measuring, although merged tests can change a project time several times over
date: 2026-10-30
classes: [stage-timeout, delegation]
severity: medium
status: fixed
---

# INC-0143 - Two branches implementing the same stage split were merged without re-measuring, although merged tests can change a project time several times over

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A merged stage split keeps timings measured before the merge.

## What happened

When two branches implemented the same stage split, merged tests changed a project time several times over, so earlier measurements no longer applied.

## Root cause

The base shape and timings came from the wrong branch.

## Why it was hard to see

Both branches were correct alone.

## Fix

Take the merged-in branch shape as the base and re-measure.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Re-measure after a merge that changes the tests in a stage.

## Related

[INC-0131](./INC-0131-a-stage-hang-deadline-copied-from-a-planning-estimate-killed.md)
