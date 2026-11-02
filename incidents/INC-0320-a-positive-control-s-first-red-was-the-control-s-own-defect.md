---
id: INC-0320
title: A positive control's first red was the control's own defect
date: 2026-11-01
classes: [test-isolation, false-green]
severity: medium
status: fixed
---

# INC-0320 - A positive control's first red was the control's own defect

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The control failed because its captured environment overwrote a value the nested runner set.

## What happened

a new positive control failed because its captured fixture environment overwrote the nested runner's worker slot id, so a later fork checked the wrong values

## Root cause

a new positive control failed because its captured fixture environment overwrote the nested runner's worker slot id, so a later fork checked the wrong values

## Why it was hard to see

A red from a control reads as a finding about the product, so the control itself is not checked.

## Fix

Suspect the control first, fix it as a tests-only commit, and keep the red

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a new positive control fails, suspect the control first, fix it as a tests-only commit and keep the red

## Related

[INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) [INC-0307](./INC-0307-a-measurement-wrapper-inherited-the-environment-the-tests-re.md) [INC-0363](./INC-0363-a-module-presence-guard-went-through-the-test-s-own-file-sys.md)
