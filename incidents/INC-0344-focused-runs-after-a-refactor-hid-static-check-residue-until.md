---
id: INC-0344
title: Focused runs after a refactor hid static-check residue until the first canonical run
date: 2026-11-01
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0344 - Focused runs after a refactor hid static-check residue until the first canonical run

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Many commits were verified with focused runs, and the first canonical runs failed at lint and a hygiene check before any suite ran.

## What happened

after moving tests between tiers, the engineer verified with focused runs for many commits; the first canonical runs then failed at lint (unused bindings and errors rethrown without their cause) and at a unit hygiene check (a config spread the hygiene rule cannot classify), all left by the refactor, before any suite ran

## Root cause

after moving tests between tiers, the engineer verified with focused runs for many commits; the first canonical runs then failed at lint (unused bindings and errors rethrown without their cause) and at a unit hygiene check (a config spread the hygiene rule cannot classify), all left by the refactor, before any suite ran

## Why it was hard to see

Focused runs are green and fast, and they skip lint, typecheck and hygiene checks entirely.

## Fix

Fix the residue in the author's own files, run the static steps directly, then run the canonical gate once

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> After a refactor, run the canonical gate once, static steps included, before more focused work; focused runs skip lint, typecheck and hygiene checks

## Related

[INC-0342](./INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) [INC-0221](./INC-0221-a-performance-refactor-was-checked-only-on-the-real-tree.md) [INC-0422](./INC-0422-a-scoped-compiler-config-flagged-an-import-style-that-the-ca.md)
