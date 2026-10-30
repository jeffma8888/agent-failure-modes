---
id: INC-0116
title: Two validators enforcing the same rule masked single-file mutations
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0116 - Two validators enforcing the same rule masked single-file mutations

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

Removing one of two redundant checks leaves the suite green.

## What happened

Two validators enforced the same rule, so mutating either one alone was caught by the other and the gap was hidden. Entry points also lacked their own refusal rows.

## Root cause

Redundancy was treated as extra safety and tested only as a pair.

## Why it was hard to see

Every mutation looks detected, and a broken layer is never seen alone.

## Fix

Mutate each layer alone and both together, and give each entry point its own refusal row.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Test every layer of a redundant check independently.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
