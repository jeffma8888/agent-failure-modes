---
id: INC-0223
title: An empty environment caller was at risk of being repaired with inherited values
date: 2026-10-31
classes: [ipc-and-env, false-green]
severity: medium
status: fixed
---

# INC-0223 - An empty environment caller was at risk of being repaired with inherited values

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The inherited values hid the empty case.

## What happened

An empty environment caller can be repaired by passing inherited values, and the test then no longer proves the empty case.

## Root cause

An empty environment caller can be repaired by passing inherited values, and the test then no longer proves the empty case.

## Why it was hard to see

Inherited values make the test pass.

## Fix

Repair it without passing inherited values, and prove both that the input is really empty and that a refusal fails when its guard is removed

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove the input is empty and that the refusal fails without its guard

## Related

[INC-0180](./INC-0180-a-readiness-check-ran-without-the-dispatcher-environment.md)
