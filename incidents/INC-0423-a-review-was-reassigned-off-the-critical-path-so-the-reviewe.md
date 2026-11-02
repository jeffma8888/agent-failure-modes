---
id: INC-0423
title: A review was reassigned off the critical path so the reviewer who owned the blocking recheck stayed on it
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0423 - A review was reassigned off the critical path so the reviewer who owned the blocking recheck stayed on it

**Cost:** No work was lost; the reassignment kept the critical recheck from queueing behind a second review.

## Signature - how you recognise it

One reviewer held two reviews while a blocking recheck waited.

## What happened

a production diff review was reassigned from the reviewer who held the blocking design recheck to a different reviewer, so the critical path stayed with its owner and the diff was still reviewed by a non-author

## Root cause

the first assignment ignored which reviewer owned the blocking recheck

## Why it was hard to see

Both assignments were individually reasonable.

## Fix

before assigning a review, check whether the named reviewer is on the critical path, and give the non-critical review to another non-author

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Keep the reviewer on the critical path on that path and reassign off-path reviews to another non-author

## Related

[INC-0399](./INC-0399-a-final-review-was-reassigned-from-a-busy-reviewer-to-an-idl.md) [INC-0337](./INC-0337-reviewers-named-at-ruling-time-were-busy-when-the-artifact-l.md) [INC-0467](./INC-0467-a-run-plan-barred-the-test-author-from-running-the-script-an.md)
