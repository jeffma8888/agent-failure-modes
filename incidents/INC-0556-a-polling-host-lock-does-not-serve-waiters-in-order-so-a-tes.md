---
id: INC-0556
title: A polling host lock does not serve waiters in order, so a test run queued after its own setup took the lock first and failed on a database setup had not created
date: 2026-11-02
classes: [concurrency]
severity: low
status: open
---

# INC-0556 - A polling host lock does not serve waiters in order, so a test run queued after its own setup took the lock first and failed on a database setup had not created

**Cost:** One wasted run, discarded as not behavioral evidence; the retry was still queued when work paused.

## Signature - how you recognise it

Two dependent steps are queued as separate acquisitions of a lock that waiters poll for, and the later one runs first.

## What happened

The host lock was a directory created atomically, and waiters retried every ten seconds, so whichever waiter retried first after a release won. An engineer queued its worktree setup and then the first test run as two separate jobs. Under heavy contention the test run took the lock before the setup and failed because its database cluster did not exist yet. The engineer recorded that red as not behavioral evidence and queued a retry after setup.

## Root cause

A polling lock gives no order among waiters, and the dependency between the two jobs lived only in the order they were started.

## Why it was hard to see

On a quiet host the earlier job almost always wins, so the order looks guaranteed until contention exposes the race.

## Fix

Run dependent steps inside one job that takes the lock once, or use a ticket lock that serves waiters in arrival order.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never rely on start order across separate acquisitions of a polling lock; run dependent steps under one acquisition or use a first-come ticket lock.

## Related

[INC-0554](./INC-0554-a-host-wide-load-gate-held-a-one-shot-time-windowed-check-un.md)
