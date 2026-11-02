---
id: INC-0479
title: A leak scanner that walked the working directory reported an ignored local file, and the push gate blocked on a file that never ships
date: 2026-11-02
classes: [detector-fail-closed]
severity: low
status: fixed
---

# INC-0479 - A leak scanner that walked the working directory reported an ignored local file, and the push gate blocked on a file that never ships

**Cost:** Minor: a push was blocked until the finding was understood.

## Signature - how you recognise it

A scan of the working directory flagged a file outside the pushed tree.

## What happened

A leak scanner that scans the working directory reported an ignored local file as a leak. That file never ships, so the push gate blocked on something outside the pushed tree.

## Root cause

The scanner's input was the working directory, which holds ignored and untracked files, not the tree that a push publishes.

## Why it was hard to see

The finding looks like a real leak until someone checks whether the file is tracked.

## Fix

When gating a push, scan an export of the tracked tree (an archive of the head commit), which contains exactly what a push publishes.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Gate a push on a scan of an export of the tracked tree; a scan of the working directory blocks on files that never ship.

## Related

[INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md) [INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md)
