---
id: INC-0192
title: A rehearsal mixed automatic guards with procedural stops
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0192 - A rehearsal mixed automatic guards with procedural stops

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The rehearsal could not say which guard fired.

## What happened

A negative-case rehearsal mixed automatic guards with procedural stops, and the planted state change was not set relative to the actual baseline.

## Root cause

A negative-case rehearsal mixed automatic guards with procedural stops, and the planted state change was not set relative to the actual baseline.

## Why it was hard to see

Both kinds of stop end the run.

## Fix

Separate the two kinds of stop and plant the change relative to the actual baseline

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Separate automatic guards from procedural stops in a rehearsal, and plant the state change relative to the actual baseline

## Related

[INC-0172](./INC-0172-a-clean-tree-gate-failed-on-a-fixture-synthetic-repo-before.md)
