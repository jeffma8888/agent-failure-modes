---
id: INC-0587
title: A release removed a lock link by owner text without checking that the link pointed at the caller's own stage
date: 2026-11-04
classes: [concurrency]
severity: high
status: mitigated
---

# INC-0587 - A release removed a lock link by owner text without checking that the link pointed at the caller's own stage

**Cost:** None. The review blocked the revision.

## Signature - how you recognise it

A release compares text and removes a link that may now belong to another holder.

## What happened

A release removed the lock symlink after matching owner text, without checking that the link target was the caller's own stage. A forced fixture showed that a link pointing at another stage could be removed. The ruling requires that release checks, under the guard, that the link target is the caller's recorded stage.

## Root cause

The release trusted a text field, not the link target.

## Why it was hard to see

The text matched, so the check looked complete.

## Fix

Under the guard, compare the link target with the caller's recorded stage before removing.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A release removes a lock only after proving, under the guard, that the lock target is the caller's own recorded stage.

## Related

[INC-0575](./INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md) [INC-0585](./INC-0585-a-lock-protected-by-an-advisory-lock-on-a-file-opened-by-pat.md)
