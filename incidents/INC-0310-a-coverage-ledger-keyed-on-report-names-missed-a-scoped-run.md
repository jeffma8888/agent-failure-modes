---
id: INC-0310
title: A coverage ledger keyed on report names missed a scoped run of the exact bytes
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0310 - A coverage ledger keyed on report names missed a scoped run of the exact bytes

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The ledger called a red check stale while a reviewer had already executed the exact terminal file.

## What happened

a red-check coverage ledger was keyed on report file names, so a reviewer's scoped execution of the exact terminal bytes, recorded in a review file, was not counted and a needless extra wave was planned

## Root cause

a red-check coverage ledger was keyed on report file names, so a reviewer's scoped execution of the exact terminal bytes, recorded in a review file, was not counted and a needless extra wave was planned

## Why it was hard to see

The evidence existed, but under a report name the ledger did not look at.

## Fix

Key coverage ledgers on the exact bytes executed, from any report, instead of on report names

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Key coverage ledgers on the exact bytes executed, from any report, not on report names

## Related

[INC-0285](./INC-0285-a-tier-level-coverage-table-hides-untraced-cases.md) [INC-0234](./INC-0234-a-ledger-review-that-started-from-the-author-list-could-inhe.md) [INC-0284](./INC-0284-a-gate-result-counts-only-at-a-revision-the-gate-can-fetch-a.md) [INC-0283](./INC-0283-a-hold-gate-is-proven-only-while-eligible-work-exists.md)
