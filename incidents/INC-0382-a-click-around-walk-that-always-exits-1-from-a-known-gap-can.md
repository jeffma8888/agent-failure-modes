---
id: INC-0382
title: A click-around walk that always exits 1 from a known gap cannot gate regressions
date: 2026-11-01
classes: [false-green]
severity: low
status: fixed
---

# INC-0382 - A click-around walk that always exits 1 from a known gap cannot gate regressions

**Cost:** A regression could hide behind a failure that was already expected.

## Signature - how you recognise it

A walk reported failure on every run, so a new failure was indistinguishable.

## What happened

a click-around walk whose exit code is always 1 because of a declared, known gap could not gate regressions, since a new failure looked the same as the known one

## Root cause

the gate used the exit code alone while a known gap kept it permanently failing

## Why it was hard to see

A constant signal carries no information, and the baseline was never named.

## Fix

Compare the walk result against a named baseline result instead of the exit code

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compare a walk with a known gap against a named baseline result; an exit code that is always failing cannot gate

## Related

[INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) [INC-0388](./INC-0388-a-baseline-comparison-graded-only-rows-present-in-the-baseli.md)
