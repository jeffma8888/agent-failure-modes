---
id: INC-0650
title: An options comparison applied the same hard constraint at different severities
date: 2026-11-23
classes: [spec-and-scope]
severity: medium
status: fixed
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 1
---

# INC-0650 - An options comparison applied the same hard constraint at different severities

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Requirements, units, or hard limits cannot hold together](../catalog/spec-and-scope/requirements-and-limits-collide.md)

**Cost:** A cross-model review and comparison revision were required; the ultimate option verdicts did not change, and elapsed rework was not recorded.

## Signature - how you recognise it

The same disqualifying condition is blocking for one alternative and advisory for others; a limitation shared by all alternatives is presented as uniquely blocking.

## What happened

In an options analysis, one licence condition barred an activity under an explicit invariant. The comparison marked that condition blocking for one option but merely advisory for two other options with the same clause. It also called a capability missing from every option a blocking con of only one. A second-model reviewer identified both asymmetries.

## Root cause

The analysis assigned severity labels while discussing options one at a time instead of defining each invariant once and mapping it consistently to every option it affects.

## Why it was hard to see

Each individual option section looked plausible when read alone. The contradiction only emerged when the reviewer aligned identical clauses and common limitations across the option matrix.

## Fix

List each invariant before scoring, apply its consequences to every affected option, and separate universally shared disadvantages from true option-specific blockers; recompute verdicts after relabeling.

## Verification

The reviewer found the inconsistent labels; the labels were revised and the option verdicts remained the same. Not checked in the input: whether later comparisons maintain this cross-option discipline.

## Transferable rule

> Write each decision invariant once, apply the same severity to every option that shares its condition, and never label a disadvantage common to all options as uniquely blocking; recompute verdicts after corrections.

## Related

[INC-0572](./INC-0572-a-brief-said-one-sorted-line-for-a-root-with-two-specs-which.md) [INC-0035](./INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md)
