---
id: INC-0392
title: A declaration request that split sourced values from decisions let the lead rule eleven items in one pass
date: 2026-11-01
classes: [delegation]
severity: low
status: fixed
---

# INC-0392 - A declaration request that split sourced values from decisions let the lead rule eleven items in one pass

**Cost:** Eleven items were ruled in one pass instead of several rounds.

## Signature - how you recognise it

A request mixed facts and open choices, which would have needed several rounds.

## What happened

a declaration request split sourced values from decisions, each with its gap, and the lead ruled eleven items in one pass

## Root cause

facts and decisions were not separated, so each item needed triage before a ruling

## Why it was hard to see

A mixed list reads as one task, and the open items hide among the sourced ones.

## Fix

Ask for declarations as two lists: sourced values, and decisions with the gap for each

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Request declarations as sourced values and decisions, each with its gap

## Related

[INC-0385](./INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md) [INC-0379](./INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md)
