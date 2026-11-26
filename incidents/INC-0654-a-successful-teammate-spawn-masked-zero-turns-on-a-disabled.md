---
id: INC-0654
title: A successful teammate spawn masked zero turns on a disabled model
date: 2026-11-23
classes: [delegation, observability]
severity: medium
status: mitigated
topic: delegation/order-collides-with-rule-or-guard
occurrences: 1
---

# INC-0654 - A successful teammate spawn masked zero turns on a disabled model

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md) / [Your order collided with a tool rule, permission ceiling, guard or pin](../catalog/delegation/order-collides-with-rule-or-guard.md)

**Cost:** Two delegated slices lost about two days before the missing checkpoint files revealed that neither teammate had started.

## Signature - how you recognise it

A spawn command returns a thread identifier for a model the operator's standing rule marks as disabled, but no teammate turn or first checkpoint file appears.

## What happened

The lead accepted a user request naming a model the operator's standing rule marks as disabled and spawned two teammates on it. The spawn calls reported success and supplied thread identifiers, but authorization prevented any turn from running. The absence of the required skeleton output files was noticed only two days later, delaying an author slice and a review slice.

## Root cause

The lead did not reconcile the requested resource with the standing availability restriction before dispatch, then mistook thread creation for proof that execution had begun instead of checking the first required artifact.

## Why it was hard to see

A success response and thread identifier resemble a live worker even when resource authorization blocks the first turn. Silence can look like slow work if the first checkpoint file is not checked promptly.

## Fix

Before spawning, state the conflict between a user-named resource and a standing disabled-resource rule and select an available resource only after reconciliation; after dispatch, confirm a first checkpoint artifact or actual turn start within minutes.

## Verification

A later state check found both expected files absent after about two days, establishing that the assigned work had not produced its required checkpoint. Not checked in the input: a successful replacement run or that an early-start check now prevents recurrence.

## Transferable rule

> Before assigning work, reconcile any user-named resource against standing disabled-resource rules; after spawn, verify an actual first turn or required checkpoint artifact within minutes. A returned thread ID is not evidence of execution.

## Related

[INC-0489](./INC-0489-a-rule-written-in-teammate-briefs-was-broken-by-the-lead-in.md) [INC-0128](./INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) [INC-0635](./INC-0635-a-review-was-assigned-to-a-reviewer-by-role-name-but-the-rev.md)
