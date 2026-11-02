---
id: INC-0231
title: A measurement was at risk of coming from an overlay in a scratch tree
date: 2026-10-31
classes: [observability, false-green]
severity: medium
status: fixed
---

# INC-0231 - A measurement was at risk of coming from an overlay in a scratch tree

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The figures had no tree behind them.

## What happened

The assigned base lacked a file the measurer was asked to measure, which invited overlaying bytes into a scratch tree.

## Root cause

The assigned base lacked a file the measurer was asked to measure, which invited overlaying bytes into a scratch tree.

## Why it was hard to see

The overlay is quick and looks equivalent.

## Fix

Measure on the exact tree that carries it and label each figure with its SHA, instead of overlaying bytes into a scratch tree

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure on the exact tree that carries the file and label every figure with its SHA

## Related

[INC-0146](./INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md) [INC-0470](./INC-0470-a-count-delta-in-an-acceptance-document-was-first-attributed.md)
