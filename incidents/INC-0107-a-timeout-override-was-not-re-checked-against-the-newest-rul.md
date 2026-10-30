---
id: INC-0107
title: A timeout override was not re-checked against the newest ruling, and fixes were verified from the coverage note
date: 2026-10-30
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0107 - A timeout override was not re-checked against the newest ruling, and fixes were verified from the coverage note

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A revision lands after a ruling and keeps an override that the ruling changed.

## What happened

A revision that landed after a ruling kept a timeout override the ruling had changed, and fixes were confirmed from the coverage note rather than from the code.

## Root cause

The ruling and the revision were checked separately, and prose was trusted over code.

## Why it was hard to see

The coverage note says fixed, which reads as evidence.

## Fix

Re-check every timeout override against the newest ruling when a revision lands after it, and verify each fix by its closing line in code.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify from the code line, not from the note that describes it.

## Related

[INC-0093](./INC-0093-a-smoke-run-deadline-shared-the-normal-step-budget-policy.md)
