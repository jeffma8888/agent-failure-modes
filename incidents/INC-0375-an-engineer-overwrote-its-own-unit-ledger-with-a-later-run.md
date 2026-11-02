---
id: INC-0375
title: An engineer overwrote its own unit ledger with a later run
date: 2026-11-01
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0375 - An engineer overwrote its own unit ledger with a later run

**Cost:** The earlier run record was lost until it was restored from version control.

## Signature - how you recognise it

A ledger file held only the latest run after an engineer wrote a new run over it.

## What happened

an engineer overwrote its own unit ledger with the result of a later run, losing the earlier record

## Root cause

the ledger was written as a single current-state file instead of dated sections added at the end

## Why it was hard to see

The overwrite looks like a normal update, and the earlier content is only visible in history.

## Fix

Restore the ledger from the earlier commit; keep ledgers append-only with a dated section per run

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Keep a ledger append-only with a dated section per run; never overwrite it with a later run

## Related

[INC-0371](./INC-0371-a-byte-count-compare-at-the-exact-old-length-reported-end-of.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0402](./INC-0402-an-author-who-received-a-ruling-mid-run-superseded-its-own-e.md)
