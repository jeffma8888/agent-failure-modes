---
id: INC-0412
title: A whole-unit re-run showed five failures in unrelated files because a required environment variable was unset in the shell
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0412 - A whole-unit re-run showed five failures in unrelated files because a required environment variable was unset in the shell

**Cost:** Five red results could have been read as a regression or ignored as noise.

## Signature - how you recognise it

A whole-unit run failed in files unrelated to the change under acceptance.

## What happened

the lead's whole-unit re-run for an acceptance showed 5 failures in files that import none of the code under acceptance, all failing closed because the test database admin URL was unset in that shell; the acceptance document recorded them as an environment gap, never as a pass and never as a regression

## Root cause

the shell lacked a required variable, and the guards failed closed as designed

## Why it was hard to see

The failures looked like a regression in untouched code, and counting them as a pass would have hidden the gap.

## Fix

Record the failures as an environment gap with their cause; neither count them as a pass nor as a regression, and rerun with the variable set when authorized

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Record failures caused by an unset environment variable as an environment gap, never a pass and never a regression

## Related

[INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) [INC-0408](./INC-0408-an-evidence-gap-a-temporary-config-not-retained-was-closed-b.md)
