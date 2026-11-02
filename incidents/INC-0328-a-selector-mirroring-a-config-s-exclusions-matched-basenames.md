---
id: INC-0328
title: A selector mirroring a config's exclusions matched basenames at any depth
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0328 - A selector mirroring a config's exclusions matched basenames at any depth

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Files in nested directories with an excluded name vanished from a selection the config would keep.

## What happened

code that re-implemented a config's file exclusions skipped every directory with an excluded name at any depth, while the config excluded only those directories directly under one root, so nested files were silently dropped

## Root cause

code that re-implemented a config's file exclusions skipped every directory with an excluded name at any depth, while the config excluded only those directories directly under one root, so nested files were silently dropped

## Why it was hard to see

The two selections agree on the current tree, and the difference shows only for nested paths.

## Fix

Compare anchored paths, not basenames, and keep an executable union check with planted nested witnesses

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When code mirrors a config's file selection, compare anchored paths, not basenames, and keep an executable union check with planted nested witnesses

## Related

[INC-0287](./INC-0287-an-oracle-that-matches-a-substring-or-a-loose-boundary-can-b.md) [INC-0311](./INC-0311-moving-tests-into-a-new-group-silently-dropped-them-from-cal.md)
