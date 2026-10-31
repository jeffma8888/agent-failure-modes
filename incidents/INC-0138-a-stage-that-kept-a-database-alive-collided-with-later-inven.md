---
id: INC-0138
title: A stage that kept a database alive collided with later inventory and frozen-clock gc cases
date: 2026-10-30
classes: [test-isolation, concurrency]
severity: medium
status: fixed
---

# INC-0138 - A stage that kept a database alive collided with later inventory and frozen-clock gc cases

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A leftover database from one stage changes the result of a later stage.

## What happened

A stage kept a database alive, which collided with later inventory or frozen-clock gc cases.

## Root cause

Database lifetime was not tied to the stage that created it.

## Why it was hard to see

Each stage passes alone.

## Fix

No database outlives the stage that created it.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Tie resource lifetime to its creating stage.

## Related

[INC-0136](./INC-0136-a-cross-agent-inventory-flake-came-from-sharing-one-harness.md)
