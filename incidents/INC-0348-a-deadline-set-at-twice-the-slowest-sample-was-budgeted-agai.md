---
id: INC-0348
title: A deadline set at twice the slowest sample was budgeted against the whole deadline
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0348 - A deadline set at twice the slowest sample was budgeted against the whole deadline

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A stage was projected safe until it reached its deadline, while one sample already broke the real binding line.

## What happened

a stage with a twice-the-slowest calibration rule was projected safe until it reached its 60 s deadline; the binding line was 30 s, crossed several rungs earlier, and one 31.8 s sample already failed it at the current delivery

## Root cause

a stage with a twice-the-slowest calibration rule was projected safe until it reached its 60 s deadline; the binding line was 30 s, crossed several rungs earlier, and one 31.8 s sample already failed it at the current delivery

## Why it was hard to see

The deadline is the number everyone quotes, and the margin rule moves the real limit to half of it.

## Fix

Track the slowest sample against the deadline divided by the margin, re-time the first crossing, and plan throughput work before it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a rule demands margin k, the budget is the deadline divided by k; track the slowest sample against that, not the deadline

## Related

[INC-0345](./INC-0345-a-timing-anchor-derived-by-subtraction-was-used-as-if-it-wer.md) [INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) [INC-0308](./INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md) [INC-0355](./INC-0355-per-item-sequential-timeouts-could-not-meet-a-global-deadlin.md)
