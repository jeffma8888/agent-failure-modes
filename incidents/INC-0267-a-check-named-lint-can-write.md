---
id: INC-0267
title: A check named lint can write
date: 2026-11-01
classes: [spec-and-scope, tooling-paths]
severity: medium
status: fixed
---

# INC-0267 - A check named lint can write

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A check named as read only could create directories.

## What happened

a lint configuration check is not read only by construction: its loader calls mkdir, so a check named lint can write

## Root cause

a lint configuration check is not read only by construction: its loader calls mkdir, so a check named lint can write

## Why it was hard to see

The name suggests safety and the write is one line deep.

## Fix

Run it as written only where the directories already exist, and state that the call is a no-op there

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not assume a read-named check is read only; read its loader

## Related

[INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md) [INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) [INC-0439](./INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md)
