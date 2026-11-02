---
id: INC-0516
title: Backlog rows stayed open after their fixes merged, so the backlog no longer showed what was done
date: 2026-11-02
classes: [checkpoint]
severity: low
status: mitigated
---

# INC-0516 - Backlog rows stayed open after their fixes merged, so the backlog no longer showed what was done

**Cost:** Six rows needed a catch-up status update, with a backlog check that must pass.

## Signature - how you recognise it

The backlog lists as open rows whose fixes are already on the main line.

## What happened

Six backlog rows whose fixes had already merged were still open. A plan update was assigned to set each status with its merge commit, and the backlog check must pass. The backlog is the record of what is done, and it stops being that record when merged work is not marked.

## Root cause

Marking a row done was a separate step from the merge, with no check tying the two together.

## Why it was hard to see

Each open row looks like pending work, so the staleness is visible only to someone comparing the backlog with the history.

## Fix

Update a row status with the merge commit when its fix merges, and run the backlog check.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Update a backlog row status with the merge commit at the time its fix merges, so the backlog stays the record of what is done.

## Related

[INC-0449](./INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md)
