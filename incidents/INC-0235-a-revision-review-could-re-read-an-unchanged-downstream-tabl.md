---
id: INC-0235
title: A revision review could re-read an unchanged downstream table
date: 2026-10-31
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0235 - A revision review could re-read an unchanged downstream table

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The unchanged part cost review time and hid the real delta.

## What happened

A plan revision only added upstream rows, and the downstream table was byte identical.

## Root cause

A plan revision only added upstream rows, and the downstream table was byte identical.

## Why it was hard to see

The whole plan looks changed.

## Fix

Diff the downstream table first; if identical only the ledger and the pinned header change, and the carried-over hashes double as a check

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Diff the downstream table first when a revision only adds upstream rows

## Related

[INC-0198](./INC-0198-a-ledger-derived-from-a-token-range-went-stale-when-a-row-jo.md)
