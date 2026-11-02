---
id: INC-0321
title: A green parallel run was cited although the parallel group held no files
date: 2026-11-01
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0321 - A green parallel run was cited although the parallel group held no files

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The parallel pass was green over zero files.

## What happened

at baseline the parallel group contained zero files, so a green parallel run could not show isolation, scheduling or speedup

## Root cause

at baseline the parallel group contained zero files, so a green parallel run could not show isolation, scheduling or speedup

## Why it was hard to see

A green run looks like a result whatever it ran.

## Fix

Count the population a mode actually runs before citing its green, and use forced-overlap probes until it is non-empty

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Count the population a mode actually runs before citing its green; while it is empty, proof comes from forced-overlap probes

## Related

[INC-0313](./INC-0313-tests-in-a-parallel-group-raced-a-test-that-drops-the-shared.md) [INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) [INC-0461](./INC-0461-a-hook-ran-a-query-on-create-with-an-undefined-id-once-a-reg.md) [INC-0464](./INC-0464-color-escape-codes-in-a-report-broke-an-extraction-assertion.md)
