---
id: INC-0399
title: A final review was reassigned from a busy reviewer to an idle one of a different model instead of queueing
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0399 - A final review was reassigned from a busy reviewer to an idle one of a different model instead of queueing

**Cost:** The review started without waiting for the busy reviewer to finish.

## Signature - how you recognise it

A review waiting for a busy reviewer would have stalled the acceptance step.

## What happened

a final review was reassigned from a busy reviewer to an idle reviewer of a different model rather than queued behind the busy one; the author-independence rule still held

## Root cause

the review was assigned to a named reviewer who was occupied

## Why it was hard to see

Queueing behind the named reviewer looks safe, and the cost of waiting is not visible.

## Fix

Route a review to an idle qualified reviewer of a different model than the author; do not queue it behind a busy one

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Reassign a review to an idle qualified reviewer of a different model rather than queueing it, keeping the non-author rule

## Related

[INC-0392](./INC-0392-a-declaration-request-that-split-sourced-values-from-decisio.md) [INC-0385](./INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md) [INC-0410](./INC-0410-the-lead-re-merged-the-full-candidate-itself-rather-than-que.md)
