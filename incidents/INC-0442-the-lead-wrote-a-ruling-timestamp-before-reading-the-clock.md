---
id: INC-0442
title: The lead wrote a ruling timestamp before reading the clock
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
---

# INC-0442 - The lead wrote a ruling timestamp before reading the clock

**Cost:** Minor: a timestamp needed correction.

## Signature - how you recognise it

A ruling carried a time written before the clock was read.

## What happened

the lead wrote a ruling timestamp before reading the clock

## Root cause

the time was written before the clock read, the same cause as earlier cases

## Why it was hard to see

The earlier rule existed and the order of the two steps still slipped.

## Fix

read the clock immediately before writing each timestamp, every time

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock immediately before writing each timestamp; write the time after the read, not before

## Related

[INC-0415](./INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md) [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) [INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0456](./INC-0456-the-lead-wrote-ruling-timestamps-from-memory-three-times-and.md)
