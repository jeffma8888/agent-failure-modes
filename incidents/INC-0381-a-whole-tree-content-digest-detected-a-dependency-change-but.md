---
id: INC-0381
title: A whole-tree content digest detected a dependency change but could not say which file
date: 2026-11-01
classes: [observability]
severity: low
status: fixed
---

# INC-0381 - A whole-tree content digest detected a dependency change but could not say which file

**Cost:** A change was detected but its source file had to be rediscovered.

## Signature - how you recognise it

A digest differed from the marker value and gave no hint which file changed.

## What happened

a whole-tree content digest detected a dependency-tree change but could not say which file changed, because per-file before records were not kept

## Root cause

only an aggregate digest was recorded at marker time, with no per-file before records

## Why it was hard to see

An aggregate digest answers whether, not which.

## Fix

Record a file list at marker time as well as the digest

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Record a marker-time file list as well as the whole-tree digest, so a change can be attributed to a file

## Related

[INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0398](./INC-0398-a-content-inventory-that-hashed-every-file-under-the-depende.md)
