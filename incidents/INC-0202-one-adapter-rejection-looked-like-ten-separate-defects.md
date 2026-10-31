---
id: INC-0202
title: One adapter rejection looked like ten separate defects
date: 2026-10-30
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0202 - One adapter rejection looked like ten separate defects

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Ten failures shared one cause.

## What happened

An adapter rejection at the first FULL phase fanned out into intended-fault failures and smoke-wait poll timeouts that looked like separate defects.

## Root cause

An adapter rejection at the first FULL phase fanned out into intended-fault failures and smoke-wait poll timeouts that looked like separate defects.

## Why it was hard to see

The later failures are assertions never reached, not findings.

## Fix

Use direct child output diagnostics to separate the one shared cause from the assertions never reached

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before triaging many reds, read the child output to find the one shared cause

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
