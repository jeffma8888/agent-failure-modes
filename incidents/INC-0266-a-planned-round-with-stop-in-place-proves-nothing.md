---
id: INC-0266
title: A planned round with STOP in place proves nothing
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
topic: false-green/green-but-cases-never-ran
occurrences: 1
---

# INC-0266 - A planned round with STOP in place proves nothing

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [The gate was green but the cases it vouches for never executed](../catalog/false-green/green-but-cases-never-ran.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A planned round would have been skipped silently by a stop gate.

## What happened

a stopped team is skipped silently with no log line, so a round planned while STOP is in place runs nothing

## Root cause

a stopped team is skipped silently with no log line, so a round planned while STOP is in place runs nothing

## Why it was hard to see

The skip leaves no log line to notice.

## Fix

Lift STOP for exactly one round after the header is back to HOLD, and record that the round ran

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never count a round as proof while a silent skip gate is in place; verify it actually ran

## Related

[INC-0239](./INC-0239-a-hold-outcome-had-no-proof-that-nothing-changed.md)
