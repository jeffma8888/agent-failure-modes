---
id: INC-0132
title: Vitest 4 ran projects in parallel and file serialization inside a project did not order whole-cluster checks
date: 2026-10-30
classes: [test-isolation, concurrency]
severity: medium
status: fixed
---

# INC-0132 - Vitest 4 ran projects in parallel and file serialization inside a project did not order whole-cluster checks

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

Inventory checks across a shared cluster race between projects.

## What happened

Vitest 4 runs projects in parallel unless a group order is set, and disabling file parallelism serializes only inside a project, so whole-cluster inventory checks raced.

## Root cause

File serialization was assumed to apply across projects.

## Why it was hard to see

The race shows only when projects overlap in time.

## Fix

Set sequence group order for projects that share a cluster.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Serialize across projects explicitly when they share state.

## Related

[INC-0096](./INC-0096-browser-context-isolation-was-mistaken-for-seed-state-isolat.md)
