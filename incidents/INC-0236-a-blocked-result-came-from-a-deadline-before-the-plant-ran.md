---
id: INC-0236
title: A BLOCKED result came from a deadline before the plant ran
date: 2026-10-31
classes: [false-green, stage-timeout]
severity: medium
status: fixed
---

# INC-0236 - A BLOCKED result came from a deadline before the plant ran

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The negative never reached the plant.

## What happened

Earlier BLOCKED attempts stopped at a loaded-host deadline before the plant ran, so the block was not caused by the plant.

## Root cause

Earlier BLOCKED attempts stopped at a loaded-host deadline before the plant ran, so the block was not caused by the plant.

## Why it was hard to see

A red looks like a refusal.

## Fix

Count a negative only with a passing control, the plant own execution marker and the named failed step

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A negative proof counts only with a passing control, the plant own execution marker and the named failed step

## Related

[INC-0218](./INC-0218-two-loaded-host-reds-shared-one-cause-and-were-at-risk-of-a.md)
