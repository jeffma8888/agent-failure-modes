---
id: INC-0476
title: Unit mutation testing on a merged change found two survivors while every named test passed
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0476 - Unit mutation testing on a merged change found two survivors while every named test passed

**Cost:** Minor: found after the merge, before it could hide a regression; a follow-up change was opened.

## Signature - how you recognise it

Mutated code passed the whole suite.

## What happened

Unit tier mutation testing killed seven mutations and left two alive although every named test passed. Replacing one validator with true went unseen because no unit case asserted the baseline metadata it enforces. One case could not tell root status from sibling status because its fixture supplied no sibling value. Two earlier runs were setup only and were excluded from the counts.

## Root cause

The tests asserted outcomes but not the baseline values, and a fixture lacked the value that separates two cases.

## Why it was hard to see

A green suite looks discriminating, and the gap only shows when the code is deliberately broken.

## Fix

Run cheap mutations before merge, give each case a fixture that separates the values it must tell apart, assert baseline metadata, and open a follow-up change for survivors instead of reopening the merge.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A passing suite is not a discriminating suite; run cheap mutations before merge, count only runs that executed the tests, and open a follow-up change for survivors instead of reopening the merge.

## Related

[INC-0133](./INC-0133-a-local-guard-behind-a-shared-environment-pin-was-masked-and.md) [INC-0444](./INC-0444-a-static-closure-packet-that-did-not-converge-in-three-round.md)
