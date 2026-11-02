---
id: INC-0415
title: A ruling timestamp was written from an estimate and corrected minutes later, twice in one round
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
---

# INC-0415 - A ruling timestamp was written from an estimate and corrected minutes later, twice in one round

**Cost:** Minor: two timestamps were corrected minutes after they were written.

## Signature - how you recognise it

A ruling carried a time that did not match the clock.

## What happened

the lead wrote two ruling timestamps from an estimate rather than the clock and corrected them minutes later

## Root cause

the time was written from an estimate instead of from a fresh clock read

## Why it was hard to see

The correction rule already existed, and fast work makes an estimate feel accurate.

## Fix

read the clock immediately before each timestamp, every time, even when the previous one was just corrected

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock immediately before writing each timestamp; never write one from an estimate

## Related

[INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) [INC-0384](./INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md)
