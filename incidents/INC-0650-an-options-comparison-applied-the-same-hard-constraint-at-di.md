---
id: INC-0650
title: An options comparison applied the same hard constraint at different severities
date: 2026-11-23
classes: [spec-and-scope]
severity: medium
status: fixed
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 4
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

## Recurrences

Occurrences: 4. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-26 - A requirements document's option set listed a con shared by every option under only one of them; a second-model reviewer flagged it.
- 2026-11-26 - Retagging an elimination to cite a requirement left two options citing one requirement with different tags; the author flagged the pair to the reviewer. Same-condition-same-tag applies to requirements as well as invariants, with the differing condition stated in both cons.
- 2026-11-26 - While downgrading over-aggressive eliminations in a design document, one option that an approved top-priority requirement rules out was left viable: the requirement was not re-applied to every viable option after the retag. A reviewer's re-verification caught it.

## Related

[INC-0572](./INC-0572-a-brief-said-one-sorted-line-for-a-root-with-two-specs-which.md) [INC-0035](./INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md)
