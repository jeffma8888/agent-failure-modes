---
id: INC-0190
title: FAST stayed green while a command-adapter fixture missed a new execution project
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0190 - FAST stayed green while a command-adapter fixture missed a new execution project

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Only the FULL path caught the missing project.

## What happened

A new execution project was added and not every command-adapter fixture recognized it; the fast tier does not exercise that fixture.

## Root cause

A new execution project was added and not every command-adapter fixture recognized it; the fast tier does not exercise that fixture.

## Why it was hard to see

The cheap tier looked complete.

## Fix

Teach every command-adapter fixture the new project

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Update every command-adapter fixture when an execution project is added, and do not trust FAST alone

## Related

[INC-0168](./INC-0168-disjoint-project-discovery-did-not-stop-a-suite-from-running.md)
