---
id: INC-0230
title: A split of the dominant test file saved about zero
date: 2026-10-31
classes: [stage-timeout, test-isolation]
severity: medium
status: fixed
---

# INC-0230 - A split of the dominant test file saved about zero

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The split was on the shorter branch of the critical path.

## What happened

A dominant test file was assumed parallelizable, but splitting it in the shorter concurrent branch saves about zero.

## Root cause

A dominant test file was assumed parallelizable, but splitting it in the shorter concurrent branch saves about zero.

## Why it was hard to see

The biggest file looks like the lever.

## Fix

Profile its cases and check shared inventory assertions and the stage critical path first

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Profile a dominant file and check shared inventory assertions and the critical path before splitting it

## Related

[INC-0210](./INC-0210-a-slow-suite-was-a-candidate-for-cutting-before-it-was-profi.md)
