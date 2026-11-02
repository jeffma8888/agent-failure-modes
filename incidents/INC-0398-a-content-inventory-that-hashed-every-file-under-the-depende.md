---
id: INC-0398
title: A content inventory that hashed every file under the dependency tree stopped a clean run because the test runner rewrote its result cache there
date: 2026-11-02
classes: [test-isolation]
severity: low
status: fixed
---

# INC-0398 - A content inventory that hashed every file under the dependency tree stopped a clean run because the test runner rewrote its result cache there

**Cost:** A passing run was stopped by a file the runner itself had written.

## Signature - how you recognise it

An inventory guard failed a clean run because one cache file changed.

## What happened

a content inventory that hashes every file under the dependency tree stopped a clean run, because the test runner rewrites its own result cache inside that tree; the fix exempts exactly one named path with its digests recorded, never a directory or pattern

## Root cause

the inventory covered every file in the tree, including one the runner is expected to rewrite

## Why it was hard to see

A broad exemption would fix it but would also hide real changes.

## Fix

Exempt exactly one named path and record its digests; never exempt a directory or a pattern

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Exempt exactly one named path from a content inventory, with its digests recorded; never a directory or pattern

## Related

[INC-0381](./INC-0381-a-whole-tree-content-digest-detected-a-dependency-change-but.md) [INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md)
