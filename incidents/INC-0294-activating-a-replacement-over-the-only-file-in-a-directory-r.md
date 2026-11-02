---
id: INC-0294
title: Activating a replacement over the only file in a directory removed the directory
date: 2026-11-01
classes: [tooling-paths, checkpoint]
severity: medium
status: fixed
---

# INC-0294 - Activating a replacement over the only file in a directory removed the directory

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A move failed halfway because removing the sole file removed its parent.

## What happened

removing the active file also removed its now empty parent directory, so the following move had no destination; pending checks also fail after activation by design

## Root cause

removing the active file also removed its now empty parent directory, so the following move had no destination; pending checks also fail after activation by design

## Why it was hard to see

The remove step succeeds, and the failure appears only on the next command.

## Fix

Stop, recreate the parent, finish the unchanged move, run pending checks before activation, and record the post-activation refusal as expected

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before a remove-and-move, check whether the file is alone in its directory, and run pending checks first

## Related

[INC-0279](./INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md) [INC-0293](./INC-0293-the-before-state-was-not-preserved-before-an-operator-edit.md)
