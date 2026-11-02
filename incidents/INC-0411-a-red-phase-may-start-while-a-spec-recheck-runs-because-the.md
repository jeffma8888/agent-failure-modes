---
id: INC-0411
title: A red phase may start while a spec recheck runs because the reviewed bytes fix the behavior
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0411 - A red phase may start while a spec recheck runs because the reviewed bytes fix the behavior

**Cost:** The engineer's work proceeded in parallel with the recheck.

## Signature - how you recognise it

Work waited for a recheck that could not change the reviewed behavior.

## What happened

a red phase of activation, an inert stub and engineer tests may start while a spec recheck runs, because the reviewed test bytes fix the behavior; only the production commit waits

## Root cause

the dependency was treated as all or nothing instead of by what the recheck could change

## Why it was hard to see

A sequential order feels safe, and the exception needs the reviewed bytes to be fixed.

## Fix

Start the red phase in parallel with the recheck; hold the production commit until the recheck returns

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Start the red phase while a spec recheck runs; only the production commit waits

## Related

[INC-0379](./INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md) [INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md)
