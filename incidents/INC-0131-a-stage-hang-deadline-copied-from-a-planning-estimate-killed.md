---
id: INC-0131
title: A stage hang deadline copied from a planning estimate killed a correct run once heavier tests joined
date: 2026-10-30
classes: [stage-timeout]
severity: medium
status: fixed
---

# INC-0131 - A stage hang deadline copied from a planning estimate killed a correct run once heavier tests joined

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

A stage that passed earlier is killed after more tests are added.

## What happened

A stage hang deadline copied from a planning estimate killed a correct run once heavier tests joined the stage.

## Root cause

The deadline came from an estimate, not from measurement.

## Why it was hard to see

The run is correct and only slower than the estimate.

## Fix

Derive deadlines from measured clone runs.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure, then set deadlines.

## Related

[INC-0093](./INC-0093-a-smoke-run-deadline-shared-the-normal-step-budget-policy.md) [INC-0107](./INC-0107-a-timeout-override-was-not-re-checked-against-the-newest-rul.md)
