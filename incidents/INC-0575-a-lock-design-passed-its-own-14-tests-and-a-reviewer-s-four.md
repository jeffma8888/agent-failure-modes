---
id: INC-0575
title: A lock design passed its own 14 tests, and a reviewer's four forced interleavings each broke it
date: 2026-11-04
classes: [concurrency]
severity: medium
status: mitigated
---

# INC-0575 - A lock design passed its own 14 tests, and a reviewer's four forced interleavings each broke it

**Cost:** None. The first version stayed installed, and the revision was built before installing.

## Signature - how you recognise it

Tests of the happy paths pass, and timing between two steps of publication is untested.

## What happened

A revised queue and lock design passed its own 14 tests, and a reviewer reproduced the suites and then forced four interleavings that failed deterministically: a termination between creating a ticket and publishing its information left a ticket that blocks every later waiter; a termination between creating the lock and publishing its owner left a lock that nobody could reap; a cancel created during the final load check was ignored and the payload ran; and the deadline was checked on an old timestamp. The review blocked the design. The revision publishes in stages by exact identity, makes the lock an atomic symlink to a complete owner stage under a kernel file lock, checks ancestry, cancel and the clock again immediately before admission, compares the full owner on release, and was written red first.

## Root cause

The author tests covered the sequences the author imagined, not signals between two publication steps.

## Why it was hard to see

A pair of non-atomic steps looks safe until a signal lands between them.

## Fix

Force each interleaving between two publication steps, and publish only a complete, identified owner.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A lock or queue needs tests that force a signal or cancel between every pair of publication steps; publish ownership atomically and only when complete.

## Related

[INC-0558](./INC-0558-two-agents-cancelled-their-queued-heavy-jobs-by-task-id-duri.md)
