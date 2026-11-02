---
id: INC-0355
title: Per-item sequential timeouts could not meet a global deadline stated in the spec
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0355 - Per-item sequential timeouts could not meet a global deadline stated in the spec

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A spec required all process groups reaped within 10 s while the harness stopped them one after another, about 10 s each.

## What happened

the spec required both process groups and their descendants reaped within 10 s of the first failure, while the harness stops groups one after another with about 5 s to terminate and 5 s to reap each

## Root cause

a global bound was written without checking the arithmetic of the existing per-item loop, where sequential waits add up

## Why it was hard to see

Each per-item wait looks short; the sum only shows when the loop is multiplied by the number of items.

## Fix

Abort immediately, terminate all groups concurrently under one global deadline, and block database drops until every owned descendant is confirmed reaped

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a spec sets a global bound, check the existing per-item loop arithmetic; sequential waits add up

## Related

[INC-0348](./INC-0348-a-deadline-set-at-twice-the-slowest-sample-was-budgeted-agai.md) [INC-0312](./INC-0312-a-whole-stage-was-divided-by-a-parallel-speedup-although-par.md) [INC-0308](./INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md)
