---
id: INC-0332
title: A tier exclusion matched only one file extension
date: 2026-11-01
classes: [spec-and-scope, tooling-paths]
severity: medium
status: fixed
---

# INC-0332 - A tier exclusion matched only one file extension

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Slow proofs moved to a differently suffixed file would have stayed in the per-commit tier.

## What happened

the fast tier's exclusion matched one file extension form but not the module form, so slow proofs moved to a file with the other extension would have stayed in the per-commit run

## Root cause

the fast tier's exclusion matched one file extension form but not the module form, so slow proofs moved to a file with the other extension would have stayed in the per-commit run

## Why it was hard to see

The exclusion works for every file that exists today, and the gap shows only when a new extension is used.

## Fix

Check the exclusion glob against every extension in use and keep a discovery witness per tier

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When tiering by filename suffix, check the exclusion glob against every extension in use and keep a discovery witness per tier (absent here, exactly once there)

## Related

[INC-0328](./INC-0328-a-selector-mirroring-a-config-s-exclusions-matched-basenames.md) [INC-0170](./INC-0170-a-tracked-file-rewritten-per-tool-mode-could-not-stay-clean.md) [INC-0336](./INC-0336-a-tier-exclusion-was-added-only-after-a-witness-failed-witho.md) [INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md)
