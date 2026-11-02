---
id: INC-0470
title: A count change in an acceptance document was attributed to specific items without a per file check
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
---

# INC-0470 - A count change in an acceptance document was attributed to specific items without a per file check

**Cost:** None: amended before anyone used it.

## Signature - how you recognise it

A count change was credited to rows with no per file evidence.

## What happened

an acceptance document first attributed a change in test counts to specific rows without checking per file; the lead amended it before anyone used it

## Root cause

the attribution was inferred from the total, not from the files

## Why it was hard to see

A total that moved by the expected amount looks like proof of its cause.

## Fix

state a count delta with its base commit, and attribute it to a row only after a per file check

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> State a count delta with its base commit, and attribute it to a row only after a per file check

## Related

[INC-0174](./INC-0174-a-count-change-was-reconciled-by-totals-and-a-route-switch-l.md) [INC-0231](./INC-0231-a-measurement-was-at-risk-of-coming-from-an-overlay-in-a-scr.md) [INC-0234](./INC-0234-a-ledger-review-that-started-from-the-author-list-could-inhe.md)
