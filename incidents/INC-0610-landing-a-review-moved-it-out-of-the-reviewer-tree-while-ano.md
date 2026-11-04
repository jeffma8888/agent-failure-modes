---
id: INC-0610
title: Landing a review moved it out of the reviewer tree while another teammate had been told to read it there
date: 2026-11-04
classes: [delegation]
severity: low
status: mitigated
---

# INC-0610 - Landing a review moved it out of the reviewer tree while another teammate had been told to read it there

**Cost:** A teammate told to read a file at one path could not find it there once it landed on main.

## Signature - how you recognise it

A brief names a path in a worktree and the file later lives only on main.

## What happened

A review was landed on main, which moved it out of the reviewer's tree, while a second teammate had been told to read it at the old path. The teammate's brief pointed at a location that no longer held the file.

## Root cause

The brief named a tree-local path, and landing relocates files.

## Why it was hard to see

The path was correct when the brief was written.

## Fix

Name the main path in the brief, or land the file before briefing.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In a brief, name the path on main, or land the file first; a path in another tree stops being valid when the file lands.

## Related

[INC-0589](./INC-0589-the-only-copies-of-eight-reviewed-drafts-sat-untracked-in-on.md)
