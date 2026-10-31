---
id: INC-0189
title: An override was written without reading the dependent declared range
date: 2026-10-30
classes: [spec-and-scope, tooling-paths]
severity: medium
status: fixed
---

# INC-0189 - An override was written without reading the dependent declared range

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An override landed outside the range the dependent declares.

## What happened

An override was written before the dependent declared range was read; an exact pin or a caret major puts the override outside it, and no one probed the code path.

## Root cause

An override was written before the dependent declared range was read; an exact pin or a caret major puts the override outside it, and no one probed the code path.

## Why it was hard to see

The override looked like a version bump.

## Fix

Read the declared range in the registry before writing the override, and probe the code path directly

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the dependent declared range in the registry before writing an override; an out of range override needs a direct probe of the code path

## Related

[INC-0178](./INC-0178-a-production-build-dirtied-the-tree-and-an-example-role-was.md)
