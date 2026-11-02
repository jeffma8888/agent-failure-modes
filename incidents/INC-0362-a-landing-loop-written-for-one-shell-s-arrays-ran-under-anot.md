---
id: INC-0362
title: A landing loop written for one shell's arrays ran under another and committed one of two files
date: 2026-11-01
classes: [tooling-paths, vcs-destruction]
severity: low
status: fixed
---

# INC-0362 - A landing loop written for one shell's arrays ran under another and committed one of two files

**Cost:** Minor: caught before cleanup finished; the missing file was re-landed.

## Signature - how you recognise it

A commit message claimed two files but only the first of the two was committed.

## What happened

a landing loop was written for one shell's array iteration (looping over an unquoted array variable) but ran under a different shell, which expands the unquoted variable to its first element only. One of two files was copied and committed, and the commit message claimed both. The operator caught it when the cleanup step could not find the second file on the main line; the missing file was then re-landed in its own commit

## Root cause

the loop syntax was valid in the shell it was written for and silently different in the shell that ran it, and the commit message was written from intent instead of from the committed diff

## Why it was hard to see

Both shells accept the line without an error, the first iteration looked right, and a message that listed both files read as correct.

## Fix

Re-land the missing file in its own commit with a message derived from the real diff, and iterate with an explicit form valid in the running shell (the quoted all-elements expansion)

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Iterate arrays with an explicit form valid in the running shell (the quoted all-elements expansion), and derive a commit message from the committed diff summary after the commit, not from intent

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md) [INC-0248](./INC-0248-the-env-script-could-not-be-sourced-in-zsh.md) [INC-0357](./INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md) [INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md)
