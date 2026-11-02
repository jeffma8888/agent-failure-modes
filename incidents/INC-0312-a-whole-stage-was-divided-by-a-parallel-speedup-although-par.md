---
id: INC-0312
title: A whole stage was divided by a parallel speedup although part of it had to stay serial
date: 2026-11-01
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0312 - A whole stage was divided by a parallel speedup although part of it had to stay serial

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A projected stage time divided the serial files by the speedup too.

## What happened

a plan divided the full stage time by the measured parallel speedup, although a fixed set of files had to stay serial and cost real time alone, and new cold starts were not counted

## Root cause

a plan divided the full stage time by the measured parallel speedup, although a fixed set of files had to stay serial and cost real time alone, and new cold starts were not counted

## Why it was hard to see

The speedup was measured on the parallel part, and applying it to the total looks like ordinary arithmetic.

## Fix

Model the new time as serial work plus parallel makespan plus new cold starts, and state the serial floor

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Model a parallelised stage as serial work plus parallel makespan plus new cold starts, never as total time over N

## Related

[INC-0308](./INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md) [INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) [INC-0230](./INC-0230-a-split-of-the-dominant-test-file-saved-about-zero.md) [INC-0345](./INC-0345-a-timing-anchor-derived-by-subtraction-was-used-as-if-it-wer.md) [INC-0333](./INC-0333-a-per-commit-stage-cost-more-than-doubled-before-anyone-samp.md) [INC-0355](./INC-0355-per-item-sequential-timeouts-could-not-meet-a-global-deadlin.md)
