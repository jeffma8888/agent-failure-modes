---
id: INC-0383
title: A ruling was stamped four minutes ahead of the clock because the time was written before the clock was read
date: 2026-11-01
classes: [observability]
severity: low
status: fixed
---

# INC-0383 - A ruling was stamped four minutes ahead of the clock because the time was written before the clock was read

**Cost:** One ruling carried a time later than the real one; corrected in the next ruling.

## Signature - how you recognise it

A ruling carried a time stamp later than the moment it was written.

## What happened

a ruling was stamped four minutes ahead of the clock because, in the same step, the time was written before the clock was read

## Root cause

the time was composed before the clock was read, even within one step

## Why it was hard to see

Reading the clock in the same step looks safe, but order matters.

## Fix

Read the clock first, then write the time stamp; correct the stamp in the next ruling

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock first, then write the time, in that order within the step

## Related

[INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) [INC-0384](./INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md)
