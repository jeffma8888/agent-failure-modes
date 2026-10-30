---
id: INC-0075
title: Tests and code were written against a spec before its independent review returned, and the rulings then changed
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: mitigated
---

# INC-0075 - Tests and code were written against a spec before its independent review returned, and the rulings then changed

**Cost:** 48 tests and a full implementation were built on rulings that the review then changed. The work was parked as a checkpoint and the tests were revised before the code was ported, so a rework cycle was spent.

## Signature - how you recognise it

Downstream roles start in parallel with the independent review of the document they depend on, to keep everyone busy.

## What happened

To avoid idle teammates, the coordinator started the test author and then the engineer while the spec review was still running. The review returned four blocking findings: free-text redaction can leak, nested retries can overrun a stage cap, an appended reason can flip a first-match classifier, and a callback contract was undefined.

## Root cause

The review was scheduled as a parallel track instead of a gate. Keeping every role busy was optimised ahead of the cost of building on rulings that were still open.

## Why it was hard to see

Parallelism looks like efficiency, and the early work is real and mostly reusable, so the loss shows only when the review disagrees.

## Fix

Park the engineer's work on a branch as a checkpoint, append a revision to the spec, have the test author revise before the code is ported. Give idle teammates work that does not depend on the spec's open rulings.

## Verification

Checked: the review's four findings were incorporated as a spec revision and the tests were revised first. The ported implementation then passed the revised suite of 135 new cases plus the 151 existing ones.

## Transferable rule

> An independent spec review is a gate, not a parallel track. Keep idle teammates busy with work that does not depend on the spec's open rulings.

## Related

[INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) [INC-0057](./INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md)
