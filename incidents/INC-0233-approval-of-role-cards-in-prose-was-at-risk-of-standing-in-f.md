---
id: INC-0233
title: Approval of role cards in prose was at risk of standing in for a runtime check
date: 2026-10-31
classes: [false-green, delegation]
severity: medium
status: fixed
---

# INC-0233 - Approval of role cards in prose was at risk of standing in for a runtime check

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

No run backed the approval.

## What happened

Prose approval of role cards is not runtime evidence of how they behave.

## Root cause

Prose approval of role cards is not runtime evidence of how they behave.

## Why it was hard to see

Reading the card feels like checking it.

## Fix

Run both rehearsals at the exit commit

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the planted-dispute rehearsal and the incomplete-verdict dry run at the exit commit; prose approval is not runtime evidence

## Related

[INC-0192](./INC-0192-a-rehearsal-mixed-automatic-guards-with-procedural-stops.md)
