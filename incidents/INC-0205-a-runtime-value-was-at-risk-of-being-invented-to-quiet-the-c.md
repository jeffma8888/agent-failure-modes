---
id: INC-0205
title: A runtime value was at risk of being invented to quiet the compiler
date: 2026-10-30
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0205 - A runtime value was at risk of being invented to quiet the compiler

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The compiler asked for a value the code should not have.

## What happened

An ambient type augmentation made a field required, and the easy fix was to fabricate a runtime value such as NODE_ENV.

## Root cause

An ambient type augmentation made a field required, and the easy fix was to fabricate a runtime value such as NODE_ENV.

## Why it was hard to see

The fabricated value compiles and changes behavior.

## Fix

Copy the typed input and delete from the copy

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Copy the typed input and delete from the copy; never fabricate a runtime value to quiet the compiler

## Related

[INC-0171](./INC-0171-a-generator-default-module-augmentation-made-its-committed-o.md)
