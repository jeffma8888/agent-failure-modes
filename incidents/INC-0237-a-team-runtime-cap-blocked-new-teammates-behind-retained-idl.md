---
id: INC-0237
title: A team runtime cap blocked new teammates behind retained idle ones
date: 2026-10-31
classes: [delegation, concurrency]
severity: medium
status: fixed
topic: delegation/stalled-behind-one-owner-or-decision
occurrences: 1
---

# INC-0237 - A team runtime cap blocked new teammates behind retained idle ones

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md) / [Parallel work stalls behind one busy owner, open decision or slot cap](../catalog/delegation/stalled-behind-one-owner-or-decision.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The cap was reached with idle teammates that could not be closed.

## What happened

A team runtime caps active teammates at ten, and a retained teammate cannot be closed until it is released.

## Root cause

A team runtime caps active teammates at ten, and a retained teammate cannot be closed until it is released.

## Why it was hard to see

The close command fails without saying release first.

## Fix

Free a slot by release then close of the longest idle teammate, and give each teammate larger batches instead of spawning more

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Release then close the longest idle teammate to free a slot; prefer larger batches over more teammates

## Related

[INC-0229](./INC-0229-a-commit-swept-another-session-uncommitted-entries.md)
