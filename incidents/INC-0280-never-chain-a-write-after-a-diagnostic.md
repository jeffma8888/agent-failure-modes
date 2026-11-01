---
id: INC-0280
title: Never chain a write after a diagnostic
date: 2026-11-01
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0280 - Never chain a write after a diagnostic

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A write skipped by a failed diagnostic left every later check green.

## What happened

a file write chained with && after a diagnostic command that failed (a digest of a path that no longer existed) silently never ran, and the later checks still passed because none of them looked for the written file

## Root cause

a file write chained with && after a diagnostic command that failed (a digest of a path that no longer existed) silently never ran, and the later checks still passed because none of them looked for the written file

## Why it was hard to see

No later check looked for the file that was never written.

## Fix

Run the write on its own, and assert the written file exists before trusting later checks

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never chain a write after a diagnostic with &&; assert the written file exists before trusting later checks

## Related

[INC-0162](./INC-0162-a-chained-amend-reworded-the-previous-commit-after-a-failed.md)
