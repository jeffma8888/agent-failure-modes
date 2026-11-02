---
id: INC-0339
title: A mutant of a shared helper proved sensitivity but not the real resource's end state
date: 2026-11-01
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0339 - A mutant of a shared helper proved sensitivity but not the real resource's end state

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Cheap fake-client controls went red, yet nothing showed the real pool ended in the right state after a failure.

## What happened

two cheap fake-client controls through a shared acquisition helper closed the sensitivity question, but did not show exactly-once release, the pool baseline or reuse on a real pool after a failure

## Root cause

two cheap fake-client controls through a shared acquisition helper closed the sensitivity question, but did not show exactly-once release, the pool baseline or reuse on a real pool after a failure

## Why it was hard to see

A red mutant looks like full proof, while the real resource's end state is a different claim.

## Fix

Ask for both: a behavioural mutant of the shared code that goes red at the intended assertion, and a real-resource witness with controlled fault injection and end-state checks

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A helper mutant proves the test can see the bug; a real-resource witness proves the resource ends in the right state; when both are claimed, require both

## Related

[INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) [INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md) [INC-0343](./INC-0343-a-weakened-final-check-survived-a-contract-suite-that-lacked.md) [INC-0441](./INC-0441-a-geometry-spec-s-rounded-intermediate-broke-a-test-toleranc.md)
