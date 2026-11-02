---
id: INC-0350
title: Time stamps written from an estimate ran ahead of the clock
date: 2026-11-01
classes: [observability, spec-and-scope]
severity: low
status: fixed
---

# INC-0350 - Time stamps written from an estimate ran ahead of the clock

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Four rulings were labelled 19:35 to 19:50 while the clock read 19:26 at the next check.

## What happened

during a burst of rulings the lead labelled four of them 19:35 to 19:50 by estimate; the clock read at the next check said 19:26, and an earlier label was nine minutes ahead too

## Root cause

time stamps were estimated instead of read, and estimates drift ahead in fast work

## Why it was hard to see

An estimated time looks like a reading, and in a burst of work each label is only checked against the previous label, not against the clock.

## Fix

Corrected the labels in place, stating the correction and that the clock was not read

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock immediately before writing any time stamp; when you did not, write a bounded range from the last real reads, never an estimate

## Related

[INC-0128](./INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) [INC-0346](./INC-0346-a-ruling-sent-in-a-message-was-never-written-to-the-ruling-l.md) [INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md)
