---
id: INC-0513
title: An activation moved a superseded root's spec while main carried the approved successor edge, and identity failed only after the merge
date: 2026-11-02
classes: [identity-and-keying]
severity: medium
status: mitigated
---

# INC-0513 - An activation moved a superseded root's spec while main carried the approved successor edge, and identity failed only after the merge

**Cost:** The identity check failed on the branch after merging main; the activation had to be redone on the terminal revision.

## Signature - how you recognise it

An identity check reports a missing deletion of a pending copy after a branch merges a main that supersedes the activated revision.

## What happened

An activation moved the spec of one revision of a test root to its active destination. Main then carried the approved edge from that revision to a later one, so the activated revision was no longer the terminal. The identity check on the branch tip after merging main failed on the superseded pending copy and was found only after the merge. The branch now activates the terminal revision, with no root bytes or manifest edited.

## Root cause

The activation checked the revision against the branch view, not against the supersession chain on current main.

## Why it was hard to see

Both the activation and the supersession edge were valid when made, and only their combination fails.

## Fix

Before an activation, confirm on current main that the revision is the terminal of its chain, and run the identity check after merging main into the branch.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before activating a root, confirm on current main that it is still the terminal of its supersession chain; run the identity check after merging main into the branch, not only before.

## Related

[INC-0473](./INC-0473-a-test-file-was-edited-on-order-although-its-digest-was-pinn.md) [INC-0284](./INC-0284-a-gate-result-counts-only-at-a-revision-the-gate-can-fetch-a.md)
