---
id: INC-0304
title: A test was about to move to satisfy a dependency without reading what it asserts
date: 2026-11-01
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0304 - A test was about to move to satisfy a dependency without reading what it asserts

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A proposed move would have removed the only browser acceptance for two rows.

## What happened

an audit proposed moving tests for a dependency, but the specs check generated editor behavior and make no access claim, so the dependency did not exist and the move would strip the owning rows of their acceptance

## Root cause

an audit proposed moving tests for a dependency, but the specs check generated editor behavior and make no access claim, so the dependency did not exist and the move would strip the owning rows of their acceptance

## Why it was hard to see

A dependency edge in a table looks like a reason to move, and the spec body is not read.

## Fix

Read the spec's assertions and the dependency source before moving, and keep the acceptance with the owning row

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A dependency edge does not justify moving a test; check what it asserts and what acceptance the move would remove

## Related

[INC-0098](./INC-0098-an-acyclic-declared-dependency-graph-hid-producer-rows-that.md)
