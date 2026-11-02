---
id: INC-0409
title: A landing helper's clean step fast-forwarded a merged feature branch's ref, which would have moved a live branch
date: 2026-11-02
classes: [vcs-destruction]
severity: medium
status: fixed
---

# INC-0409 - A landing helper's clean step fast-forwarded a merged feature branch's ref, which would have moved a live branch

**Cost:** A live branch could have been moved under its owner, losing the owner's base.

## Signature - how you recognise it

A clean step changed the ref of a branch that had already been merged, and it could have been one still in use.

## What happened

the landing helper's clean step fast-forwarded a merged feature branch's ref to main; harmless after the merge, but it would have moved a branch still under work

## Root cause

the clean step moved every listed branch to main without checking whether any was still under work

## Why it was hard to see

After a merge the move is harmless, so the check was never needed until a live branch was in the list.

## Fix

A clean step must never move a branch ref that is still under work; check that the branch is merged and idle first

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A clean step must never move a branch ref that is still under work

## Related

[INC-0380](./INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md) [INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md)
