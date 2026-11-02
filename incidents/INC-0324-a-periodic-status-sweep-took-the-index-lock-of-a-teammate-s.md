---
id: INC-0324
title: A periodic status sweep took the index lock of a teammate's worktree
date: 2026-11-01
classes: [concurrency, vcs-destruction]
severity: medium
status: fixed
---

# INC-0324 - A periodic status sweep took the index lock of a teammate's worktree

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A teammate's staging step failed on a lock created by the coordinator's monitor.

## What happened

a coordinator's periodic sweep ran a status command in a worker's worktree, the refresh took the index lock, and the worker's staging step hit that lock; the worker rightly refused to delete a lock it did not create

## Root cause

a coordinator's periodic sweep ran a status command in a worker's worktree, the refresh took the index lock, and the worker's staging step hit that lock; the worker rightly refused to delete a lock it did not create

## Why it was hard to see

A read-only looking status command quietly writes, and the sweep and the worker never meet.

## Fix

Make the monitor lock free by skipping the index refresh, or do not touch that worktree, and never delete a lock you did not create

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A monitor of someone else's worktree must be lock free (no index refresh) or not touch that worktree at all; never delete a lock you did not create

## Related

[INC-0066](./INC-0066-a-worker-s-end-of-run-cleanup-deleted-a-shared-scratch-direc.md) [INC-0305](./INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md)
