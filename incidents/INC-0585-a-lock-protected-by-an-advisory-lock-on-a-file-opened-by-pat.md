---
id: INC-0585
title: A lock protected by an advisory lock on a file opened by path let two holders run when the file was replaced
date: 2026-11-04
classes: [concurrency]
severity: high
status: mitigated
---

# INC-0585 - A lock protected by an advisory lock on a file opened by path let two holders run when the file was replaced

**Cost:** None. The review blocked the revision and the earlier version stayed installed.

## Signature - how you recognise it

A guard file is unlinked and recreated, and the next caller locks a new file object.

## What happened

A revised queue lock took an advisory lock on a guard file that it opened by path. A reviewer forced an outside cleanup that removed the guard. The next caller created a new file, locked that new object, and two live holders ran. The fix is the standard check for a lock taken by path: after taking the lock, compare the identity of the open file with the identity of the path and retry on mismatch. A missing or replaced guard becomes a manual step with a not-run exit, never a silent new guard.

## Root cause

The lock was tied to a path, not to the file object that was locked.

## Why it was hard to see

The two holders ran with no error; each saw a lock it had taken.

## Fix

After locking, compare the open file identity with the path identity and retry on mismatch; treat a missing guard as a manual step.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> After taking a lock on a file opened by path, compare the open file identity with the path identity and retry on mismatch; never create a silent new guard.

## Related

[INC-0575](./INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md)
