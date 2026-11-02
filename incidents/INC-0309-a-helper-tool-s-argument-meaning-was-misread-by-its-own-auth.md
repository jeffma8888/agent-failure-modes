---
id: INC-0309
title: A helper tool's argument meaning was misread by its own author
date: 2026-11-01
classes: [vcs-destruction, tooling-paths]
severity: medium
status: fixed
---

# INC-0309 - A helper tool's argument meaning was misread by its own author

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A digest was passed where the clean step expected a commit, and a tracked file was deleted.

## What happened

the author of a landing tool passed a file digest where its clean step expects a commit to move to, and the step deleted a tracked file in a worktree that then had to be restored

## Root cause

the author of a landing tool passed a file digest where its clean step expects a commit to move to, and the step deleted a tracked file in a worktree that then had to be restored

## Why it was hard to see

Both values are long hex strings, and the author trusted memory of the tool instead of reading its usage line.

## Fix

Read the usage line before a destructive mode, even for your own tool, and keep destructive steps in tools that verify their arguments

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read a tool's usage line before a destructive mode, even your own tool; keep destructive steps in tools that verify the kind of each argument

## Related

[INC-0103](./INC-0103-a-teammate-could-not-run-a-destructive-git-command-even-when.md) [INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md)
