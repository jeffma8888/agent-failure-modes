---
id: INC-0234
title: A ledger review that started from the author list could inherit its gaps
date: 2026-10-31
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0234 - A ledger review that started from the author list could inherit its gaps

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The reviewer saw only what the author listed.

## What happened

A ledger was checked by reading the author list first, which carries the author omissions into the review.

## Root cause

A ledger was checked by reading the author list first, which carries the author omissions into the review.

## Why it was hard to see

The list looks complete.

## Fix

Derive the ledger from the plan yourself, then compare

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Derive a ledger from the plan yourself before reading the author list, then compare

## Related

[INC-0198](./INC-0198-a-ledger-derived-from-a-token-range-went-stale-when-a-row-jo.md) [INC-0470](./INC-0470-a-count-change-in-an-acceptance-document-was-attributed-to-s.md)
