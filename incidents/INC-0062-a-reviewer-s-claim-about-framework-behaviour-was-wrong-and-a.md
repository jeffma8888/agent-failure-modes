---
id: INC-0062
title: A reviewer's claim about framework behaviour was wrong, and accepting it would have put a wrong assertion into the tests
date: 2026-10-29
classes: [false-green, observability]
severity: medium
status: mitigated
---

# INC-0062 - A reviewer's claim about framework behaviour was wrong, and accepting it would have put a wrong assertion into the tests

**Cost:** Near miss, caught before landing. Taken as written, the review's advisory would have made a test assert an error that the framework does not return at that attempt, so the test would fail on correct behaviour or the design would be bent to match a false fact.

## Signature - how you recognise it

A review finding states what a library or framework does, in confident terms, and the proposed change follows directly from that statement.

## What happened

A reviewer said the fifth wrong password already returns the locked-account error. The pinned framework source shows the lock is recorded on the fifth failure, which still returns the ordinary authentication error; only the sixth attempt returns the locked error.

## Root cause

A reviewer's statement about behaviour is a recollection or inference, not a measurement, but it arrives with the authority of a review. An off-by-one in when state changes versus when it is reported is exactly the kind of detail recalled wrongly.

## Why it was hard to see

The claim is specific, plausible and consistent with the feature's purpose. Accepting reviewer findings is the normal, cooperative path, so verification feels like distrust.

## Fix

The author searched the pinned framework source before landing the advisory and corrected it. The QA oracle asserts the error name per attempt instead of a single summary expectation.

## Verification

The source of the pinned version showed which attempt stores the lock and which attempt reports it.

## Transferable rule

> A reviewer's statement about framework or library behaviour is a hypothesis with the same standing as the author's. Verify it against the pinned source before it changes a test or a design.

## Related

[INC-0057](./INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md) [INC-0041](./INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) [INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)
