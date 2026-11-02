---
id: INC-0394
title: A security predicate checked for truthiness failed open on an undefined or null value
date: 2026-11-02
classes: [detector-fail-open]
severity: medium
status: fixed
---

# INC-0394 - A security predicate checked for truthiness failed open on an undefined or null value

**Cost:** A missing value could have been read as permission.

## Signature - how you recognise it

A guard allowed access when its input was missing.

## What happened

a security predicate checked for truthiness, so an undefined or null value failed open; fail closed means allowing only on the exact expected value

## Root cause

the predicate tested whether the value was truthy instead of whether it was the expected one

## Why it was hard to see

A truthiness test passes every normal case and fails only on the unset one.

## Fix

Allow only when the value equals the exact expected value; treat everything else as denied

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A security predicate allows only on the exact expected value, never on truthiness

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0378](./INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md)
