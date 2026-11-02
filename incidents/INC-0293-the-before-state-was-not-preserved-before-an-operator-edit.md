---
id: INC-0293
title: The before-state was not preserved before an operator edit
date: 2026-11-01
classes: [checkpoint, vcs-destruction]
severity: medium
status: fixed
---

# INC-0293 - The before-state was not preserved before an operator edit

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A later snapshot could not recreate the state from before an operator edit.

## What happened

only a few fields of the before-state were printed, so changes to other fields of old entries would go unseen, and the original bytes were gone once the edit was made

## Root cause

only a few fields of the before-state were printed, so changes to other fields of old entries would go unseen, and the original bytes were gone once the edit was made

## Why it was hard to see

The before-state looks recoverable until the edit overwrites it.

## Fix

Copy the before-state bytes outside the repository before the edit and compare complete old entries afterwards

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Preserve before-state bytes before an operator edit; a later snapshot cannot recreate them

## Related

[INC-0254](./INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md) [INC-0292](./INC-0292-a-snapshot-recorder-that-finished-was-taken-as-proof-it-had.md) [INC-0349](./INC-0349-a-revision-was-overwritten-in-place-and-its-recorded-digest.md)
