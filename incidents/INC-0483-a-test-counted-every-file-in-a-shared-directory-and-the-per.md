---
id: INC-0483
title: A test counted every file in a shared directory, and the per-test reset reseeded into it, so the count was one too high
date: 2026-11-02
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0483 - A test counted every file in a shared directory, and the per-test reset reseeded into it, so the count was one too high

**Cost:** Minor: a red full run on the merged branch; the case failed even when run alone.

## Signature - how you recognise it

A total taken over a shared directory included files the case did not create.

## What happened

A test snapshotted a whole shared directory and expected only the two files it created. The per-test reset reseeds a minimal record that carries its own cover file, so the directory held a third file and the case failed even when run alone. An earlier guess that a refused create left a stray file was withdrawn, because the refused create leaves nothing behind.

## Root cause

The assertion measured the total of shared state, which the reset and seed change, instead of what the case itself created.

## Why it was hard to see

The count was right in the author's head and only wrong once the reset was understood, and a guess about a stray file from another test pointed the wrong way.

## Fix

Take a baseline after the reset and seed and assert the delta, or assert the created names, and keep the refusal controls unweakened.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that counts a shared directory or table must count only what the case creates, by baseline delta or by name, because the per-test reset and seed change the total.

## Related

[INC-0313](./INC-0313-tests-in-a-parallel-group-raced-a-test-that-drops-the-shared.md) [INC-0361](./INC-0361-a-test-s-teardown-emptied-a-shared-server-database-and-a-gat.md) [INC-0482](./INC-0482-tests-added-by-a-branch-were-never-run-before-the-merge-and.md)
