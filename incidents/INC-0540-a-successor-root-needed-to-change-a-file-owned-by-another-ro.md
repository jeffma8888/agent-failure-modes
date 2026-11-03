---
id: INC-0540
title: A successor root needed to change a file owned by another row family, and the identity checker allows replacement only within one family
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0540 - A successor root needed to change a file owned by another row family, and the identity checker allows replacement only within one family

**Cost:** No loss. The author found it before activation and the lead split the successor.

## Signature - how you recognise it

One successor root must edit a file that a different row family owns.

## What happened

A reviewer found that one extra seeded record also changed an integration test file owned by a different row family than the root being superseded. The identity checker allows a replacement marker only within one family, so a single successor could not carry both files. The lead ruled that the first successor carries only its own file, and a new successor over the other family root carries the second file, each with its own coverage file, manifest and replacement proposal, both activated on the feature branch only, with no cross-family marker and no registry change.

## Root cause

The seed change touched files that the registry assigns to two families.

## Why it was hard to see

The coupling shows up only when the second file is read, and the checker fails only at activation.

## Fix

Split the change into one successor per family with the same derived expectation source.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a change touches files owned by different row families, plan one successor per family; do not widen the checker or add a cross-family marker.

## Related

[INC-0537](./INC-0537-a-protection-root-pinned-an-exact-seed-inventory-and-a-featu.md)
