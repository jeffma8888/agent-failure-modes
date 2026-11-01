---
id: INC-0255
title: One batch finding hid 45 files with the same dependency
date: 2026-11-01
classes: [spec-and-scope, test-isolation]
severity: medium
status: fixed
---

# INC-0255 - One batch finding hid 45 files with the same dependency

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The defect was a conflict between two documents, not a batch fault.

## What happened

A per-batch finding was one instance of 45 files caused by a conflict between the design cut and the step order.

## Root cause

A per-batch finding was one instance of 45 files caused by a conflict between the design cut and the step order.

## Why it was hard to see

The finding named one batch.

## Fix

Resolve the design conflict at its source, a harness row, instead of rewriting dozens of tests

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a finding names a mechanism, sweep the suite for it before fixing one batch, and resolve a design conflict at its source

## Related

[INC-0225](./INC-0225-a-fix-was-named-for-one-card-while-four-siblings-carried-the.md)
