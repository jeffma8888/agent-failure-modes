---
id: INC-0212
title: A relative path was resolved against the wrong root
date: 2026-10-31
classes: [tooling-paths]
severity: medium
status: fixed
---

# INC-0212 - A relative path was resolved against the wrong root

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The command was refused for a path it did not name.

## What happened

A relative path that climbs into a sibling worktree was resolved by the permission checker against the workspace root and landed outside it.

## Root cause

A relative path that climbs into a sibling worktree was resolved by the permission checker against the workspace root and landed outside it.

## Why it was hard to see

The path is right from the current directory.

## Fix

Use absolute paths

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Use absolute paths when working across worktrees

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md)
