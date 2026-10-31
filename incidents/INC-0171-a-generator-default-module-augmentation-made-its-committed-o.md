---
id: INC-0171
title: A generator default module augmentation made its committed output fail the type check
date: 2026-10-30
classes: [tooling-paths, spec-and-scope]
severity: medium
status: fixed
---

# INC-0171 - A generator default module augmentation made its committed output fail the type check

**Cost:** Minor: a red type check.

## Signature - how you recognise it

Generated output failed to type check in the package where it landed.

## What happened

A generator default module augmentation made its committed output fail the type check in the package where it landed.

## Root cause

The augmentation referred to a module the package did not own.

## Why it was hard to see

Dropping it would also silence the typing the consumer needs.

## Fix

Move the augmentation to the consuming app instead of dropping it.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Place generated type augmentation where the augmented module lives.

## Related

[INC-0166](./INC-0166-a-conditional-omission-could-hide-behind-a-helper-an-alias-o.md)
