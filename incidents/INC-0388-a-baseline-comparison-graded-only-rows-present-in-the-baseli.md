---
id: INC-0388
title: A baseline comparison graded only rows present in the baseline, so a new failing row passed
date: 2026-11-01
classes: [false-green]
severity: medium
status: fixed
---

# INC-0388 - A baseline comparison graded only rows present in the baseline, so a new failing row passed

**Cost:** A new failing row could have passed as unchanged against the baseline.

## Signature - how you recognise it

A run with a new failing row compared equal to its baseline.

## What happened

a baseline comparison graded only the rows present in the baseline, so a row new in the run that failed was not graded and the run passed

## Root cause

the comparison iterated over the baseline rows only, so rows absent from it were never graded

## Why it was hard to see

Every row that was compared matched, so the result looked complete.

## Fix

Grade a row that is new in the run on its own outcome

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A baseline comparison must grade a row new in the run on its own outcome

## Related

[INC-0382](./INC-0382-a-click-around-walk-that-always-exits-1-from-a-known-gap-can.md) [INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md)
