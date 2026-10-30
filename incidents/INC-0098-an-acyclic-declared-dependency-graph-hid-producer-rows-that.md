---
id: INC-0098
title: An acyclic declared dependency graph hid producer rows that an acceptance file needed
date: 2026-10-30
classes: [delegation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0098 - An acyclic declared dependency graph hid producer rows that an acceptance file needed

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

The dependency graph validates, yet an acceptance file needs a row that is not listed.

## What happened

A declared dependency graph was acyclic, but an acceptance file still needed producer rows that were not declared.

## Root cause

Acyclicity was treated as completeness.

## Why it was hard to see

A graph check passes cleanly and says nothing about missing edges.

## Fix

Expand each acceptance file into the producer rows it needs and compare with declared dependencies.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An acyclic graph is necessary but not sufficient; derive edges from what each file requires.

## Related

[INC-0085](./INC-0085-a-helper-owned-by-one-test-root-was-imported-by-later-roots.md)
