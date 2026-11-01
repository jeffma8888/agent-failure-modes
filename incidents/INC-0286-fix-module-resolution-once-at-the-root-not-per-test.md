---
id: INC-0286
title: Fix module resolution once at the root, not per test
date: 2026-11-01
classes: [test-isolation, tooling-paths]
severity: medium
status: fixed
---

# INC-0286 - Fix module resolution once at the root, not per test

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Each test root worked around the same missing dependency in its own way.

## What happened

test roots needed a library that only a workspace package declared; one root loaded it with a loader workaround, which every new root would have had to copy

## Root cause

test roots needed a library that only a workspace package declared; one root loaded it with a loader workaround, which every new root would have had to copy

## Why it was hard to see

The workaround makes each test pass, so the missing root dependency never shows.

## Fix

Declare the shared dependency once as a root dev dependency, keep test roots on plain imports, and waive rather than copy the old workaround

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Resolve a shared dependency once at the root and keep test roots on plain imports

## Related

[INC-0158](./INC-0158-a-spec-used-import-meta-under-a-package-that-loads-specs-as.md)
