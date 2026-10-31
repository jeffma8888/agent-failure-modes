---
id: INC-0174
title: A count change was reconciled by totals and a route switch leaked into the default path
date: 2026-10-30
classes: [false-green, ipc-and-env]
severity: medium
status: fixed
---

# INC-0174 - A count change was reconciled by totals and a route switch leaked into the default path

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Totals matched while the contents differed.

## What happened

A count change was explained by totals, not by file identity, and a route-specific environment switch could leak into the default path.

## Root cause

Totals hide which files moved.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Reconcile by exact file identity, re-run the original surviving mutant, clear route switches on the default path.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Explain a count change by file identity, not by totals.

## Related

[INC-0146](./INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md)
