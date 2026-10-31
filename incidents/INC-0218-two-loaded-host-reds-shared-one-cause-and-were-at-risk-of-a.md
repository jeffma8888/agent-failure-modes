---
id: INC-0218
title: Two loaded-host reds shared one cause and were at risk of a timeout bump
date: 2026-10-31
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0218 - Two loaded-host reds shared one cause and were at risk of a timeout bump

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The cheap fix hid the shared cause.

## What happened

Two loaded-host reds shared one cause class that a pending row removes, and raising a timeout or retrying a case would hide it.

## Root cause

Two loaded-host reds shared one cause class that a pending row removes, and raising a timeout or retrying a case would hide it.

## Why it was hard to see

A retry makes the red disappear.

## Fix

Carry the acceptance to that row tip rather than raising a timeout or retrying a case

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When reds share a cause class that a pending row removes, carry the acceptance to that row, not a timeout or a retry

## Related

[INC-0210](./INC-0210-a-slow-suite-was-a-candidate-for-cutting-before-it-was-profi.md)
