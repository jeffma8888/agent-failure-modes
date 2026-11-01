---
id: INC-0253
title: Two of four selected projects executed no case
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0253 - Two of four selected projects executed no case

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The selection looked like coverage.

## What happened

FULL selected four browser projects but two executed no case at L1.

## Root cause

FULL selected four browser projects but two executed no case at L1.

## Why it was hard to see

Selection is reported; execution is not.

## Fix

Record executed cases per project

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Record executed cases per project; a selected project is not coverage

## Related

[INC-0222](./INC-0222-a-clean-tree-positive-did-not-exercise-the-working-file-cont.md)
