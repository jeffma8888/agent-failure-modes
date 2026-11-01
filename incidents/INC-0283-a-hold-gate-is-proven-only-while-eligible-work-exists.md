---
id: INC-0283
title: A hold gate is proven only while eligible work exists
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0283 - A hold gate is proven only while eligible work exists

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A hold looked proven when the queue had nothing to select.

## What happened

the late-HOLD window deliberately keeps two rows eligible, because a hold gate is only proven when eligible work exists and nothing is selected; an empty queue proves nothing

## Root cause

the late-HOLD window deliberately keeps two rows eligible, because a hold gate is only proven when eligible work exists and nothing is selected; an empty queue proves nothing

## Why it was hard to see

Nothing selected is the expected result of both a working gate and an empty queue.

## Fix

Keep eligible rows in place and confirm that none was selected

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a hold gate only with eligible work present; an empty queue proves nothing

## Related

[INC-0266](./INC-0266-a-planned-round-with-stop-in-place-proves-nothing.md)
