---
id: INC-0322
title: A search helper ended a gather loop at the first file without a match
date: 2026-11-01
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0322 - A search helper ended a gather loop at the first file without a match

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A loop printed results for some inputs and silently skipped the rest.

## What happened

a gather loop used a search helper whose no-match status stopped the loop at the first file without a match, so the output looked complete but was partial

## Root cause

a gather loop used a search helper whose no-match status stopped the loop at the first file without a match, so the output looked complete but was partial

## Why it was hard to see

The printed rows are correct, and the missing rows leave no trace.

## Fix

Use a tool whose no-match status you control by appending a guard, and check that every iteration printed

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In loops, use a tool whose no-match status you control (append a guard) and check that every iteration printed

## Related

[INC-0051](./INC-0051-a-fallible-edit-script-followed-by-a-semicolon-let-the-commi.md) [INC-0310](./INC-0310-a-coverage-ledger-keyed-on-report-names-missed-a-scoped-run.md)
