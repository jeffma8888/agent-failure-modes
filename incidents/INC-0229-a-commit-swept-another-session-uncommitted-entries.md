---
id: INC-0229
title: A commit swept another session uncommitted entries
date: 2026-10-31
classes: [vcs-destruction, concurrency]
severity: medium
status: fixed
---

# INC-0229 - A commit swept another session uncommitted entries

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Entries landed under a message about a different lesson.

## What happened

Another session committed in a shared checkout and swept a teammate uncommitted entries into its own commit.

## Root cause

Another session committed in a shared checkout and swept a teammate uncommitted entries into its own commit.

## Why it was hard to see

The tree is shared and the staging was broad.

## Fix

Stage only the exact paths you own, check the log for foreign commits before writing, and note any sweep in a follow-up commit so it stays traceable

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In a shared checkout, stage only your own paths and check the log for foreign commits before writing

## Related

[INC-0162](./INC-0162-a-chained-amend-reworded-the-previous-commit-after-a-failed.md)
