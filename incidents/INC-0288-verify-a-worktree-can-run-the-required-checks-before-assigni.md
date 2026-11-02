---
id: INC-0288
title: Verify a worktree can run the required checks before assigning work there
date: 2026-11-01
classes: [tooling-paths, test-isolation]
severity: medium
status: fixed
---

# INC-0288 - Verify a worktree can run the required checks before assigning work there

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Every required check failed before running because the assigned worktree lacked a script.

## What happened

a sparse checkout omitted a shared environment script, so each required check exited early; a full disposable checkout at the same baseline passed

## Root cause

a sparse checkout omitted a shared environment script, so each required check exited early; a full disposable checkout at the same baseline passed

## Why it was hard to see

An early exit looks like a check failure, and a skipped check can be mistaken for a pass.

## Fix

Run the required checks once in the worktree before assigning work, use a full disposable checkout if needed, and record the failure instead of claiming a pass

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Confirm a worktree can run the required checks before work is assigned there

## Related

[INC-0264](./INC-0264-run-repo-checkers-from-a-tree-that-contains-them.md) [INC-0286](./INC-0286-fix-module-resolution-once-at-the-root-not-per-test.md)
