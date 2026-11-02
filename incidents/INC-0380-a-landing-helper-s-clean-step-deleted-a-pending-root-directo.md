---
id: INC-0380
title: A landing helper's clean step deleted a pending root directory and left an unchanged tracked file deleted after the fast-forward
date: 2026-11-01
classes: [vcs-destruction]
severity: medium
status: fixed
---

# INC-0380 - A landing helper's clean step deleted a pending root directory and left an unchanged tracked file deleted after the fast-forward

**Cost:** A tracked file was missing from the landed tree until the lead restored it.

## Signature - how you recognise it

A tracked file that had not changed was gone after a landing.

## What happened

a landing helper's clean step deleted the whole pending root directory in the author's worktree and then fast-forwarded, so an unchanged tracked file in an in-place revised root stayed deleted; the lead restored it

## Root cause

the clean step removed the whole directory, and the later fast-forward did not bring back files the revision left unchanged

## Why it was hard to see

Deleting then fast-forwarding looks like a normal sync, and the missing file only shows in tree status.

## Fix

The helper now restores tracked unchanged files after the fast-forward; check tree status after the landing

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A clean step must not leave a tracked unchanged file deleted; restore tracked files after a fast-forward and check tree status

## Related

[INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0371](./INC-0371-a-byte-count-compare-at-the-exact-old-length-reported-end-of.md) [INC-0389](./INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md) [INC-0400](./INC-0400-an-activation-instruction-to-delete-superseded-pending-copie.md)
