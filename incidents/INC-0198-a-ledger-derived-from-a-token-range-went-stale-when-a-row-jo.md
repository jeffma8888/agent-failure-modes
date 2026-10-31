---
id: INC-0198
title: A ledger derived from a token range went stale when a row joined the range
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0198 - A ledger derived from a token range went stale when a row joined the range

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The ledger no longer matched the plan.

## What happened

A staging ledger derived from a token range went stale whenever a row joined that range.

## Root cause

A staging ledger derived from a token range went stale whenever a row joined that range.

## Why it was hard to see

The derivation was done once and then trusted.

## Fix

Regenerate it from the current plan at each revision and state the derived count

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Regenerate a ledger derived from a range at each revision and state the derived count

## Related

[INC-0183](./INC-0183-sibling-fixture-factories-lacked-the-metadata-that-makes-a-c.md)
