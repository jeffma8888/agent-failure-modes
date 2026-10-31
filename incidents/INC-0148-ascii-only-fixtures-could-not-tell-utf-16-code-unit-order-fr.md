---
id: INC-0148
title: ASCII-only fixtures could not tell UTF-16 code unit order from UTF-8 byte order
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0148 - ASCII-only fixtures could not tell UTF-16 code unit order from UTF-8 byte order

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A sort or compare test passes under either ordering because all data is ASCII.

## What happened

Fixtures were ASCII only, so a comparison by UTF-16 order and one by UTF-8 byte order gave the same result.

## Root cause

The test data could not distinguish the two orderings.

## Why it was hard to see

The code is correct for ASCII and wrong for other text.

## Fix

Add fixtures where UTF-16 and UTF-8 order differ.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Choose data that separates the alternatives under test.

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md)
