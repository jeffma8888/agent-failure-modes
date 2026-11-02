---
id: INC-0373
title: Two replies were stamped with times ahead of the clock
date: 2026-11-01
classes: [observability]
severity: low
status: fixed
---

# INC-0373 - Two replies were stamped with times ahead of the clock

**Cost:** Minor: two replies carried times later than the real send time; the correction was recorded in the next ruling.

## Signature - how you recognise it

Replies carried a time stamp later than the moment they were sent.

## What happened

the lead stamped two replies with times ahead of the clock: both stamps were later than the real send time. The correction was recorded in the next ruling, and the content of the replies stood

## Root cause

the time stamps were estimated instead of read from the clock at the moment of writing

## Why it was hard to see

An estimate in fast work drifts ahead, and a plausible time stamp does not look wrong on its own.

## Fix

Record the correction in the next ruling and read the clock immediately before writing any time stamp

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock immediately before writing any timestamp, never estimate it

## Related

[INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) [INC-0128](./INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) [INC-0384](./INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md)
