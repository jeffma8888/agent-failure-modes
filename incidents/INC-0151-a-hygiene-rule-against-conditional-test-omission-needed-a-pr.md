---
id: INC-0151
title: A hygiene rule against conditional test omission needed a precise flagged and allowed set
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0151 - A hygiene rule against conditional test omission needed a precise flagged and allowed set

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A conditional skip or registration hides a test from the suite.

## What happened

Conditional omission through skipIf, runIf or registration inside a condition could hide tests. The ruling flags those and conditional registration at module or describe scope, and allows a conditional inside a test body and each tables.

## Root cause

No rule covered omission by condition.

## Why it was hard to see

A conditional registration looks like ordinary code.

## Fix

Flag skipIf, runIf and registrations inside conditions; allow assertion branches and each tables.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> State both the flagged and the allowed set of a hygiene rule.

## Related

[INC-0141](./INC-0141-a-static-watchdog-rule-accepting-only-an-inline-await-of-a-n.md)
