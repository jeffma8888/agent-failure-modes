---
id: INC-0459
title: A new required argument broke an older direct caller that the change did not list
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0459 - A new required argument broke an older direct caller that the change did not list

**Cost:** A repair commit and a rerun.

## Signature - how you recognise it

A whole unit run showed one more failure after a signature change.

## What happened

a change made a finite clock argument required; a seed test that called the function directly the older way failed as a sixth whole unit failure, because the change had been checked against the new callers only; the repair kept the legacy call path working

## Root cause

the new argument was checked against new callers only

## Why it was hard to see

The old caller was a test in another area that nobody searched.

## Fix

when an argument becomes required, list every direct caller including tests, and keep the legacy call path or update each caller in the same change

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When an argument becomes required, list every direct caller, tests included, and keep the old call path or update every caller in the same change

## Related

[INC-0255](./INC-0255-one-batch-finding-hid-45-files-with-the-same-dependency.md) [INC-0225](./INC-0225-a-fix-was-named-for-one-card-while-four-siblings-carried-the.md) [INC-0214](./INC-0214-a-helper-was-fixed-and-a-caller-still-passed-a-literal-empty.md)
