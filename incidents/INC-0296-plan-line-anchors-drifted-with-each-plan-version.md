---
id: INC-0296
title: Plan line anchors drifted with each plan version
date: 2026-11-01
classes: [spec-and-scope, stale-module]
severity: medium
status: fixed
---

# INC-0296 - Plan line anchors drifted with each plan version

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Correct line citations became off by one after a later plan revision.

## What happened

coverage cited plan rows by line number, and a later plan revision shifted the lines while the requirement stayed the same

## Root cause

coverage cited plan rows by line number, and a later plan revision shifted the lines while the requirement stayed the same

## Why it was hard to see

The anchor was right when written, so the drift is nobody's error.

## Fix

Cite the row ID, with section and step where needed; use a line number only with the baseline revision it was read at

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Cite plan rows by identity; line drift alone is not a finding

## Related

[INC-0054](./INC-0054-a-display-name-drifted-from-the-model-identifier-it-was-supp.md)
