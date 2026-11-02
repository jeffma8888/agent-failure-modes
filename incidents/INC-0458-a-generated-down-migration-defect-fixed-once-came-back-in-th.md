---
id: INC-0458
title: A generated down migration defect fixed once came back in the next row because the fix was never turned into a check
date: 2026-11-02
classes: [detector-fail-open]
severity: low
status: fixed
---

# INC-0458 - A generated down migration defect fixed once came back in the next row because the fix was never turned into a check

**Cost:** A repeat of a known defect, caught by a static review before any run.

## Signature - how you recognise it

A defect already fixed once appeared again with no check to catch it.

## What happened

the generated down migration dropped a table with cascade and then dropped the removed constraint without if exists, which fails; it was found and fixed by a sanctioned edit in one row, and the same defect appeared again in the next row and was found only by a static review, because the fix had not been turned into a check that every generated migration runs

## Root cause

a one time fix was recorded as a ruling but not added to a list of checks

## Why it was hard to see

A ruling about one row reads as finished work, so nobody turns it into a standing check.

## Fix

turn each fixed generator defect into a named check with a symptom, a place to look, a command and a sanctioned edit, and run the whole list on every generated migration before the next generation step

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Turn a fixed generator defect into a check on the list that every later generated migration runs

## Related

[INC-0439](./INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md) [INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) [INC-0448](./INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md)
