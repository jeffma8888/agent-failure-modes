---
id: INC-0247
title: Ancestry was at risk of standing in for a clean tree or a checker run
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0247 - Ancestry was at risk of standing in for a clean tree or a checker run

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The commit was there and the facts were not proved.

## What happened

Ancestry proves a published commit is present but not a historical clean working tree, a checker execution, or two observations bracketing a rehearsal.

## Root cause

Ancestry proves a published commit is present but not a historical clean working tree, a checker execution, or two observations bracketing a rehearsal.

## Why it was hard to see

Presence looks like proof of the whole run.

## Fix

Prove each of those separately

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not use ancestry as evidence of a clean tree, a checker run or bracketing observations

## Related

[INC-0239](./INC-0239-a-hold-outcome-had-no-proof-that-nothing-changed.md)
