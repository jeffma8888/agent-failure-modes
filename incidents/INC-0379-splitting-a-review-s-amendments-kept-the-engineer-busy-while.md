---
id: INC-0379
title: Splitting a review's amendments kept the engineer busy while decisions were pending
date: 2026-11-01
classes: [delegation]
severity: low
status: fixed
---

# INC-0379 - Splitting a review's amendments kept the engineer busy while decisions were pending

**Cost:** Idle time while waiting on decisions was avoided without writing tests that a later decision would invalidate.

## Signature - how you recognise it

An engineer would have waited for all amendments of one review to be decided.

## What happened

a review's amendments were split between those the engineer applies now and those the spec author decides; the engineer stayed busy while decisions were pending, provided tests for undecided items were not written early

## Root cause

amendments were treated as one batch rather than by who can decide them

## Why it was hard to see

Starting work on a mixed batch risks tests written for items that later change.

## Fix

Split amendments into apply-now and spec-author-decides; write no tests for the undecided items until they are decided

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Split a review's amendments into apply-now and author-decides, and write no tests for undecided items early

## Related

[INC-0128](./INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) [INC-0385](./INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md)
