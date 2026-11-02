---
id: INC-0402
title: An author who received a ruling mid-run superseded its own earlier status with a dated addendum without rewriting the historical bytes
date: 2026-11-02
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0402 - An author who received a ruling mid-run superseded its own earlier status with a dated addendum without rewriting the historical bytes

**Cost:** The record kept both the earlier status and the change, so the history stayed readable.

## Signature - how you recognise it

A status written before a ruling needed to change after it.

## What happened

an author who received a ruling mid-run appended a dated addendum that supersedes its own earlier status, and left the historical bytes unchanged

## Root cause

the old status could only be changed by rewriting it, which would erase what was known at the time

## Why it was hard to see

Editing in place is the shortest path and looks the same as a correct note.

## Fix

Append a dated addendum that states what supersedes what, and keep the earlier text as written

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a ruling changes a status, append a dated addendum that supersedes it; never rewrite the historical bytes

## Related

[INC-0375](./INC-0375-an-engineer-overwrote-its-own-unit-ledger-with-a-later-run.md) [INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md)
