---
id: INC-0305
title: A process the sandbox could not see was judged dead and its live run was removed
date: 2026-11-01
classes: [concurrency, ipc-and-env]
severity: medium
status: fixed
---

# INC-0305 - A process the sandbox could not see was judged dead and its live run was removed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A run directory vanished mid run after another agent removed a registration it judged dead.

## What happened

a gate run lost its run directory with file-not-found errors across several suites; another agent had removed the run's registration and temp directory by hand, judging them dead because its sandbox process listing did not show the owner and the database was absent from its own cluster, and the recursive removal took a nested run with it; the cleanup tool itself would have skipped the live process

## Root cause

a gate run lost its run directory with file-not-found errors across several suites; another agent had removed the run's registration and temp directory by hand, judging them dead because its sandbox process listing did not show the owner and the database was absent from its own cluster, and the recursive removal took a nested run with it; the cleanup tool itself would have skipped the live process

## Why it was hard to see

Sandboxes do not see each other's processes, so a live owner looks dead from outside.

## Fix

Remove a temp directory, registration or process only when its exact name or identifier is recorded in your own run output; leave anything stale and unrecorded in place and report it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A process your sandbox cannot see is not a dead process; ownership comes from your own run record, not from visibility or timing

## Related

[INC-0066](./INC-0066-a-worker-s-end-of-run-cleanup-deleted-a-shared-scratch-direc.md) [INC-0306](./INC-0306-a-conditional-diagnosis-was-closed-from-the-actor-s-account.md) [INC-0307](./INC-0307-a-measurement-wrapper-inherited-the-environment-the-tests-re.md) [INC-0313](./INC-0313-tests-in-a-parallel-group-raced-a-test-that-drops-the-shared.md) [INC-0324](./INC-0324-a-periodic-status-sweep-took-the-index-lock-of-a-teammate-s.md) [INC-0471](./INC-0471-drafts-proposed-test-database-ports-by-reading-tracked-text.md)
