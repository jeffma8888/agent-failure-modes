---
id: INC-0445
title: A migration lock covered the whole branch when it needed to cover only the generators and schema paths
date: 2026-11-02
classes: [concurrency]
severity: low
status: fixed
---

# INC-0445 - A migration lock covered the whole branch when it needed to cover only the generators and schema paths

**Cost:** Parallel work was blocked until the lock was narrowed.

## Signature - how you recognise it

A second branch idled although most of its work did not touch the locked resource.

## What happened

the migration lock was read as covering a whole branch, so a second branch could not proceed at all; the lead narrowed it to the generators, the migration and generated-types paths and any run that needs the new schema, so a second branch may author code and tests, activate files and run its red phase in parallel, then merges main, generates on that base and sorts after the holder, with a snapshot whose parent is not the latest migration on main a STOP

## Root cause

the lock was defined by the branch instead of by the resource

## Why it was hard to see

Locking the whole branch is the simplest and safest-looking rule.

## Fix

scope a lock to the shared resource it protects, not to the branch, and say what the second branch may do and how it rejoins

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scope a lock to the shared paths and commands it protects, not the whole branch, and state how a second branch rejoins after the holder merges

## Related

[INC-0219](./INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md) [INC-0419](./INC-0419-a-registry-edit-failed-its-own-sorted-order-assertion-and-th.md)
