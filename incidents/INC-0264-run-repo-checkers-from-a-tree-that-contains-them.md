---
id: INC-0264
title: Run repo checkers from a tree that contains them
date: 2026-11-01
classes: [tooling-paths, stale-module]
severity: medium
status: fixed
---

# INC-0264 - Run repo checkers from a tree that contains them

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A checker failed because the tree it ran in lacked its modules.

## What happened

a checker script run from a worktree on an older base failed with module not found; the lead ran it from main after copying the files

## Root cause

a checker script run from a worktree on an older base failed with module not found; the lead ran it from main after copying the files

## Why it was hard to see

Copying files around the failure hides the stale base.

## Fix

Run repo checkers from a tree that contains them, or fast-forward first

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run a repo checker from a tree that contains it, or fast-forward the tree first

## Related

[INC-0150](./INC-0150-a-missing-independently-callable-guard-lacked-protocol-cases.md)
