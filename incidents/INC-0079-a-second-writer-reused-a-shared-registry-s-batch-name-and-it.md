---
id: INC-0079
title: A second writer reused a shared registry's batch name and its entries silently vanished
date: 2026-10-30
classes: [identity-and-keying, concurrency]
severity: low
status: fixed
---

# INC-0079 - A second writer reused a shared registry's batch name and its entries silently vanished

**Cost:** Minor: the writer's incidents dropped out of the composed list until the build's validation flagged the corpus as invalid.

## Signature - how you recognise it

Two writers extend one registry and pick the next batch name from their own expectation of what is next.

## What happened

A writer named its new batch with the number it expected next. Another writer had already used that name, so the later definition replaced the earlier one and the first writer's entries disappeared from the composition. The build's own validation reported the corpus invalid.

## Root cause

The writer read the last record ID but not the last batch name, and the language allowed a silent rebind of a module-level name.

## Why it was hard to see

Only one of several identifiers was checked, and the overwrite raised no error at definition time.

## Fix

Rename the batch to the next unused name and rebuild; the build then listed every incident.

## Verification

Checked: the rebuilt composition contains all entries and the validation passes. Not checked: a guard that rejects a duplicate batch name directly.

## Transferable rule

> Before adding to a shared registry, read the current last value of every identifier kind you will create (record IDs, batch names, keys), not only the record ID.

## Related

[INC-0077](./INC-0077-keeping-an-error-prefix-did-not-keep-the-downstream-classifi.md)
