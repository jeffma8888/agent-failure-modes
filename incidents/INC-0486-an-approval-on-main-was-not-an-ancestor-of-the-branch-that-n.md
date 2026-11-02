---
id: INC-0486
title: An approval on main was not an ancestor of the branch that needed it
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: mitigated
---

# INC-0486 - An approval on main was not an ancestor of the branch that needed it

**Cost:** None incurred: caught by review before the activation commit, at the price of an extra branch-side merge step.

## Signature - how you recognise it

A checker required the approval commit to be an ancestor of the branch head, and the branch had forked before the approval landed.

## What happened

A review approval was committed to main after a feature branch had forked from it. The identity checker ties an activation commit to its approval and requires the approval commit to be an ancestor of the activation head. The approval was not an ancestor of the branch, so an activation commit made on the branch as it stood would have been refused. The route is to merge main into the branch first, with no fast-forward, rehearsed with a merge-tree dry run, and only then make the one activation commit.

## Root cause

The approval and the branch were on diverged lines of history, and the check is about ancestry, not about the approval simply existing somewhere in the repository.

## Why it was hard to see

The approval exists, is correct and is reachable by name, so it looks usable; ancestry only matters to the checker, and the refusal comes at the last step.

## Fix

Merge main into the branch (a branch-side merge, not a merge to main), rehearse it with a merge-tree dry run, then make the activation commit that cites the approval, and run the identity check.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An approval that landed on main after a branch forked is not an ancestor of that branch; merge main into the branch before any activation commit that a checker ties to that approval.

## Related

[INC-0164](./INC-0164-a-reverted-and-re-landed-qa-revision-got-its-marker-approved.md) [INC-0204](./INC-0204-a-precommit-check-reported-a-merge-brought-approval-as-unrea.md)
