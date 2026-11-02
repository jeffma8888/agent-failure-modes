---
id: INC-0349
title: A revision was overwritten in place and its recorded digest named bytes that no longer existed
date: 2026-11-01
classes: [checkpoint, false-green]
severity: medium
status: fixed
---

# INC-0349 - A revision was overwritten in place and its recorded digest named bytes that no longer existed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A rechecker could not run the new tests against the prior revision because only its size and digest survived.

## What happened

a checker fix was revised in place from revision 2 to revision 3; the rechecker was asked to show the new tests fail on the revision 2 bytes, but those bytes (size and digest recorded in a review) existed nowhere: not in any worktree, temporary folder or the repository object store, so the red witness had to fall back to the pre-fix original plus a historical review

## Root cause

a checker fix was revised in place from revision 2 to revision 3; the rechecker was asked to show the new tests fail on the revision 2 bytes, but those bytes (size and digest recorded in a review) existed nowhere: not in any worktree, temporary folder or the repository object store, so the red witness had to fall back to the pre-fix original plus a historical review

## Why it was hard to see

A recorded digest feels like a preserved revision, but it proves only which bytes were meant.

## Fix

Before revising in place, copy the prior revision to a named file or commit it on a work branch, and record its path with its digest

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A digest proves which bytes you meant, not that you can still run them; keep every reviewed revision's bytes until the fix lands

## Related

[INC-0293](./INC-0293-the-before-state-was-not-preserved-before-an-operator-edit.md) [INC-0216](./INC-0216-a-scratch-swap-of-revision-bytes-failed-the-identity-gate-as.md)
