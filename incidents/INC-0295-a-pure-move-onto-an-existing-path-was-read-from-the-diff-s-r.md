---
id: INC-0295
title: A pure move onto an existing path was read from the diff's rename display
date: 2026-11-01
classes: [false-green, vcs-destruction]
severity: medium
status: fixed
---

# INC-0295 - A pure move onto an existing path was read from the diff's rename display

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A move showed as modify plus delete, so the diff could not confirm it.

## What happened

when the destination already exists in the parent, an ordinary diff shows a modification and a deletion, never a rename; a commit subject can still claim pure renames

## Root cause

when the destination already exists in the parent, an ordinary diff shows a modification and a deletion, never a rename; a commit subject can still claim pure renames

## Why it was hard to see

The diff looks like an unplanned change even when it is the planned move.

## Fix

Compare the bytes and digests of the moved file with its source

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a move by byte equality and digests, not by the rename display

## Related

[INC-0185](./INC-0185-rename-detection-reported-a-false-rename-in-a-merge.md)
