---
id: INC-0157
title: A split-ownership root could not activate because identity had no registry support
date: 2026-10-30
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0157 - A split-ownership root could not activate because identity had no registry support

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The identity checker rejected a root whose file had been reassigned to another row.

## What happened

A root holding both a superseded suite and a path reassigned by the registry failed the partial activation check, because the registry half of the identity checker belonged to a later row.

## Root cause

Registry-aware identity was scheduled after the row that first needed it.

## Why it was hard to see

The failure looked like a bad activation, not a missing capability in the checker.

## Fix

Accept the identity half of the registry rule into the row: a registered path is judged on its own and left out of its source root partial-activation test.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A root split by the registry needs registry-aware identity before its source row can activate.

## Related

[INC-0154](./INC-0154-a-marker-for-an-already-activated-revision-used-the-pending.md)
