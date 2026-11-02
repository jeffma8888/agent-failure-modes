---
id: INC-0319
title: A sparse checkout hid a tracked file that every brief pointed at
date: 2026-11-01
classes: [tooling-paths, delegation]
severity: medium
status: fixed
---

# INC-0319 - A sparse checkout hid a tracked file that every brief pointed at

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A reviewer reported a tracked file absent from the tree.

## What happened

the working copies given to two reviewers used sparse lists that left out a tracked file every brief pointed at, so the reviewers reported it missing

## Root cause

the working copies given to two reviewers used sparse lists that left out a tracked file every brief pointed at, so the reviewers reported it missing

## Why it was hard to see

The file is tracked and present in the main checkout, so the briefer sees no gap.

## Fix

When a brief points at a repo file, confirm it exists in each reviewer's checkout, including sparse lists

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a brief points at a repo file, confirm it exists in each reviewer's checkout, including sparse lists

## Related

[INC-0288](./INC-0288-verify-a-worktree-can-run-the-required-checks-before-assigni.md) [INC-0264](./INC-0264-run-repo-checkers-from-a-tree-that-contains-them.md)
