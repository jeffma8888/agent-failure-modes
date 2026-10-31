---
id: INC-0224
title: A classifier kept a legacy pattern list beside a new exact signature
date: 2026-10-31
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0224 - A classifier kept a legacy pattern list beside a new exact signature

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The legacy list still matched lookalikes.

## What happened

A classifier kept a legacy pattern list while adding an exact signature, which extends rather than narrows what it accepts.

## Root cause

A classifier kept a legacy pattern list while adding an exact signature, which extends rather than narrows what it accepts.

## Why it was hard to see

The new signature looks like the rule.

## Fix

Probe with lookalike negatives (path, code, indent, line order)

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Probe a classifier extension with lookalike negatives

## Related

[INC-0213](./INC-0213-a-network-denied-dependency-audit-was-neither-a-finding-nor.md)
