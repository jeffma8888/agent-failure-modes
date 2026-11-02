---
id: INC-0334
title: A bare number beside a time threshold invited a unit misread
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0334 - A bare number beside a time threshold invited a unit misread

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A count was readable as seconds because the cell had no unit.

## What happened

a table column held a bare number that was a cumulative case count, placed near time thresholds, so a reader could take it for seconds

## Root cause

a table column held a bare number that was a cumulative case count, placed near time thresholds, so a reader could take it for seconds

## Why it was hard to see

The number is right, and its meaning depends on a unit the cell leaves out.

## Fix

Put units in every numeric cell that sits near a time threshold

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put units in every numeric cell that sits near a time threshold

## Related

[INC-0071](./INC-0071-a-plan-claimed-minutes-denominated-stage-times-fit-inside-a.md) [INC-0358](./INC-0358-a-restated-rule-gained-a-qualifier-the-original-ruling-never.md)
