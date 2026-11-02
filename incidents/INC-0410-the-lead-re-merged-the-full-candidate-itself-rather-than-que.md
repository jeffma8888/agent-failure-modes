---
id: INC-0410
title: The lead re-merged the full candidate itself rather than queue behind the busy owner, and proved the delta path by path
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0410 - The lead re-merged the full candidate itself rather than queue behind the busy owner, and proved the delta path by path

**Cost:** The candidate was ready without waiting, and the equal delta was shown rather than assumed.

## Signature - how you recognise it

A mechanical merge was waiting for a busy owner.

## What happened

the lead re-merged the full candidate itself rather than queue behind the busy owner, and proved that the new candidate's delta equals the old one path by path

## Root cause

the work was assigned to its original owner by default

## Why it was hard to see

Queueing looks like the safe choice, and doing it yourself needs a proof of equality to be trusted.

## Fix

Do the merge directly when the owner is busy, and prove the new delta equals the old path by path

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When the owner is busy, redo a mechanical merge directly and prove the new delta equals the old path by path

## Related

[INC-0399](./INC-0399-a-final-review-was-reassigned-from-a-busy-reviewer-to-an-idl.md) [INC-0385](./INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md)
