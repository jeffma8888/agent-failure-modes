---
id: INC-0208
title: Two rows were green alone and red together
date: 2026-10-31
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0208 - Two rows were green alone and red together

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The combination failed and neither branch did.

## What happened

A scoped lint rule from one row and a generated file with a disable banner from another were red only in combination.

## Root cause

A scoped lint rule from one row and a generated file with a disable banner from another were red only in combination.

## Why it was hard to see

Each branch passes its own checks.

## Fix

Rehearse the merged stack

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Rehearse the merged stack, not the branches

## Related

[INC-0175](./INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md)
