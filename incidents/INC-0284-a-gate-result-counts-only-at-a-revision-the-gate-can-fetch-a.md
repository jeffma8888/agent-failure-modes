---
id: INC-0284
title: A gate result counts only at a revision the gate can fetch and that holds its fix
date: 2026-11-01
classes: [false-green, checkpoint]
severity: medium
status: fixed
---

# INC-0284 - A gate result counts only at a revision the gate can fetch and that holds its fix

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A gate passed at a revision that did not yet hold the fix it depended on.

## What happened

a pre-release gate was planned against an early revision, but the fix it depends on landed later; only a published revision at or after that fix could be fetched and was a valid target

## Root cause

a pre-release gate was planned against an early revision, but the fix it depends on landed later; only a published revision at or after that fix could be fetched and was a valid target

## Why it was hard to see

A pass at the wrong revision looks identical to a pass at the right one.

## Fix

Run the gate at a published revision that contains the dependent fix, and record the revision and the time margin

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A gate run counts only at a revision the gate's clone can fetch and that already contains the fix the gate depends on

## Related

[INC-0145](./INC-0145-a-readiness-check-measured-the-lead-checkout-while-preship-m.md) [INC-0271](./INC-0271-a-load-induced-harness-red-is-not-headroom.md)
