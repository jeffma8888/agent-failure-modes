---
id: INC-0242
title: Four of five test authors stopped at the same undeclared seam
date: 2026-11-01
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0242 - Four of five test authors stopped at the same undeclared seam

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Authors stopped at the same boundary.

## What happened

A tier audit judged proposed unit cases by behavior instead of by declared seam, so four of five authors stopped at the same boundary.

## Root cause

A tier audit judged proposed unit cases by behavior instead of by declared seam, so four of five authors stopped at the same boundary.

## Why it was hard to see

The behavior looked testable.

## Fix

A ruling adds a seam addendum; interface and edge roots proceed now, and the checkpoint is per root, not per batch

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Audit a proposed test by the seam it declares, and checkpoint per root rather than per batch

## Related

[INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md) [INC-0460](./INC-0460-an-order-sensitive-comparison-of-two-tool-listings-failed-on.md)
