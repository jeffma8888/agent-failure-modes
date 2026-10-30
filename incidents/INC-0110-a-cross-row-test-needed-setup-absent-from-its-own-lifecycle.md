---
id: INC-0110
title: A cross-row test needed setup absent from its own lifecycle, and green was claimed without a fresh-clone setup or a canonical temp directory
date: 2026-10-30
classes: [test-isolation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0110 - A cross-row test needed setup absent from its own lifecycle, and green was claimed without a fresh-clone setup or a canonical temp directory

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

A test passes in a warm checkout and needs a database or path that the fresh lifecycle never creates.

## What happened

A cross-row test needed a run database the harness should have created, and its setup was missing from its own lifecycle. Green was claimed before checking a fresh clone and a canonical temp directory with symlinks resolved.

## Root cause

The test relied on state left by earlier work, and temp paths were compared unresolved.

## Why it was hard to see

A warm checkout hides the missing setup, and a symlinked temp directory only breaks path comparisons on some machines.

## Fix

Check fresh-clone setup and a canonical (symlink-resolved) temp directory before claiming green.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run from a clean state and compare resolved paths before reporting a pass.

## Related

[INC-0087](./INC-0087-an-import-level-audit-missed-helper-calls-that-needed-a-late.md)
