---
id: INC-0209
title: A FULL step deadline was shorter than the measured stage time
date: 2026-10-31
classes: [stage-timeout, false-green]
severity: medium
status: fixed
---

# INC-0209 - A FULL step deadline was shorter than the measured stage time

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The deadline sat below the measured time.

## What happened

The FULL unit deadline was 90 s while unit took 93 to 103 s in FAST.

## Root cause

The FULL unit deadline was 90 s while unit took 93 to 103 s in FAST.

## Why it was hard to see

The budget was right when it was written.

## Fix

Recheck each FULL budget against measured FAST stage times whenever the suite grows

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Recheck FULL step budgets against measured FAST stage times whenever the suite grows

## Related

[INC-0146](./INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md)
