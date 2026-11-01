---
id: INC-0299
title: A row-only overlay left out the helpers of a dependency row, so consumers looked blocked
date: 2026-11-01
classes: [test-isolation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0299 - A row-only overlay left out the helpers of a dependency row, so consumers looked blocked

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Consumer files failed to import helpers that a declared dependency owns.

## What happened

a red check overlaid only the assigned rows, so two consumer files could not import helpers owned by a declared dependency row that was not yet active in the base; the files looked blocked though the dependency was declared

## Root cause

a red check overlaid only the assigned rows, so two consumer files could not import helpers owned by a declared dependency row that was not yet active in the base; the files looked blocked though the dependency was declared

## Why it was hard to see

The import error reads like a defect in the consumer or an undeclared dependency.

## Fix

Activate the dependency row helpers first, preserving digests and lineage, then rerun the consumers; do not copy older helpers, edit imports or add stubs

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Confirm the helpers owned by dependency rows are active in the base before judging a consumer blocked or red

## Related

[INC-0297](./INC-0297-a-test-needed-a-second-account-that-the-minimal-seed-did-not.md) [INC-0100](./INC-0100-a-new-test-file-was-placed-in-a-row-whose-activation-order-d.md)
