---
id: INC-0598
title: A go decision was tied to a stale commit that later rulings had overtaken, and the ruling moved it to a named condition
date: 2026-11-04
classes: [checkpoint]
severity: low
status: mitigated
---

# INC-0598 - A go decision was tied to a stale commit that later rulings had overtaken, and the ruling moved it to a named condition

**Cost:** None. The packet was corrected before GO.

## Signature - how you recognise it

A go packet names a fixed commit that predates later rulings.

## What happened

The packet named an older commit as the GO baseline. Later rulings made the baseline the main commit at the next green full run, on or after the merge of the budget change, and the integration time of that run is the baseline quoted at GO. The reviewer's note was accepted and the packet was rewritten.

## Root cause

A fixed commit was written down early and later rulings changed what the baseline should be.

## Why it was hard to see

The old commit was once correct, so it did not look wrong.

## Fix

State the GO baseline as a condition (main at the next green full run) and quote that run's measured time.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Name a GO baseline by its condition, and recheck it against rulings made since the packet was written.

## Related

[INC-0160](./INC-0160-an-activation-was-tied-to-an-unreviewed-successor-and-had-to.md)
