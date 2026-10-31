---
id: INC-0210
title: A slow suite was a candidate for cutting before it was profiled
date: 2026-10-31
classes: [stage-timeout, observability]
severity: medium
status: fixed
---

# INC-0210 - A slow suite was a candidate for cutting before it was profiled

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The slow part was not where cuts would land.

## What happened

Parallel test files and one batched object read gave back about 90 s without touching a QA byte; the unprofiled tree was red on a loaded host.

## Root cause

Parallel test files and one batched object read gave back about 90 s without touching a QA byte; the unprofiled tree was red on a loaded host.

## Why it was hard to see

Cutting tests feels like progress.

## Fix

Profile first, then parallelize and batch

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Profile before cutting tests

## Related

[INC-0187](./INC-0187-a-slow-stage-was-trimmed-by-cases-instead-of-cut-by-grouping.md)
