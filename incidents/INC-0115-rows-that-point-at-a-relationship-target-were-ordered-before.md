---
id: INC-0115
title: Rows that point at a relationship target were ordered before the target was registered, tempting stubs or optional fields
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0115 - Rows that point at a relationship target were ordered before the target was registered, tempting stubs or optional fields

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

A row needs a related record that a later row creates.

## What happened

Rows were ordered so that a relationship target was registered after the row pointing at it, which pushed toward stubbed or optional fields.

## Root cause

Row order followed topic, not the relationship graph.

## Why it was hard to see

Making the field optional silently weakens the contract.

## Fix

Order rows so every relationship target is registered before the row that points at it.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Fix the order, not the contract.

## Related

[INC-0098](./INC-0098-an-acyclic-declared-dependency-graph-hid-producer-rows-that.md)
