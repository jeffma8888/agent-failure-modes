---
id: INC-0441
title: A geometry spec's rounded intermediate broke a test tolerance, caught by independent arithmetic
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0441 - A geometry spec's rounded intermediate broke a test tolerance, caught by independent arithmetic

**Cost:** No test was loosened; the spec was corrected at review.

## Signature - how you recognise it

A spec's numbers did not meet the test tolerance they were written for.

## What happened

a reviewer recomputed the rendition geometry independently and found that a rounded intermediate would have produced an output height off by more than the oracle's tolerance of one pixel; the lead kept the rounded extract rectangle, set the output height by rounding width over the ratio, made the resize exact, accepted a sub-pixel stretch of at most one pixel, and recomputed every row without loosening the tolerance

## Root cause

a rounded intermediate value was reused downstream and the error added up

## Why it was hard to see

Each rounding step looked harmless alone.

## Fix

recompute spec arithmetic independently with the oracle's tolerance, round only at the last step, and never loosen the oracle

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Recompute spec geometry independently against the oracle tolerance, round at the last step, and never loosen the oracle

## Related

[INC-0430](./INC-0430-a-route-validator-rejected-a-width-that-the-generator-was-re.md) [INC-0339](./INC-0339-a-mutant-of-a-shared-helper-proved-sensitivity-but-not-the-r.md)
