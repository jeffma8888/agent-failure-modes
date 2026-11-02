---
id: INC-0333
title: A per-commit stage cost more than doubled before anyone sampled it
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0333 - A per-commit stage cost more than doubled before anyone sampled it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The first stage sample came after several review rounds and showed far more than the design assumed.

## What happened

a shared per-commit stage grew from a baseline under a minute to more than double that against a design assumption of a small addition, and the overrun surfaced only at the first sample after several review rounds

## Root cause

a shared per-commit stage grew from a baseline under a minute to more than double that against a design assumption of a small addition, and the overrun surfaced only at the first sample after several review rounds

## Why it was hard to see

Each added test looks small, and the review rounds proceed on the assumed cost.

## Fix

Sample the stage early, compare with the design assumption before reviews pile up, and move heavy proofs to the slower tier rather than raising the cap

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a row adds tests to a shared per-commit gate, sample the stage early and compare with the design assumption; move heavy proofs to the slower tier rather than raising the cap

## Related

[INC-0308](./INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md) [INC-0230](./INC-0230-a-split-of-the-dominant-test-file-saved-about-zero.md)
