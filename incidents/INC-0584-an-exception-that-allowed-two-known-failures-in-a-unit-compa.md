---
id: INC-0584
title: An exception that allowed two known failures in a unit comparison was closed the moment their fix merged
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0584 - An exception that allowed two known failures in a unit comparison was closed the moment their fix merged

**Cost:** None. The exception could not mask a new failure after the fix.

## Signature - how you recognise it

A comparison exception outlives the failures it was written for.

## What happened

A merge rule excused two known failing unit names in the comparison against the frozen baseline. When the fix for them reached the main branch, the lead ruled that the exception ends: every product or harness branch merges only on a unit comparison equal to the frozen set, on a tree that contains the fix, and the two names excuse nothing from then on.

## Root cause

An exception had no end condition.

## Why it was hard to see

A standing exception reads as part of the baseline.

## Fix

Tie the exception to its fix, close it when the fix merges, and require the tree to contain the fix.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An exception for known failures must end when its fix merges; require the tree to contain the fix and compare to the frozen set.

## Related

[INC-0568](./INC-0568-a-feature-branch-merged-on-static-gates-only-and-a-unit-test.md)
