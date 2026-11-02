---
id: INC-0371
title: A byte-count compare at the exact old length reported end of file on a prefix that matched
date: 2026-11-01
classes: [detector-fail-closed]
severity: low
status: fixed
---

# INC-0371 - A byte-count compare at the exact old length reported end of file on a prefix that matched

**Cost:** Minor: a false mismatch on an append-only file until a second compare showed it identical.

## Signature - how you recognise it

A prefix check on an append-only file exited non-zero although the old bytes were unchanged.

## What happened

a prefix check for an append-only file used the system compare tool limited to exactly the old file length. The BSD compare reported end of file and exited 1 even though the prefix matched, and an independent byte-prefix compare in a script showed the bytes identical

## Root cause

the check relied on a limited-length compare at the exact boundary, where the tool treats reaching the limit and end of file as a difference

## Why it was hard to see

A non-zero exit on an append-only file looks like a real modification, and the natural reaction is to doubt or repair the file.

## Fix

Compare the first N bytes of the new file with the whole old file in an explicit byte-prefix compare, and treat the limited-length result as unproven

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify append-only files with an explicit byte-prefix compare, not a limited-length compare at the exact length

## Related

[INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) [INC-0126](./INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) [INC-0375](./INC-0375-an-engineer-overwrote-its-own-unit-ledger-with-a-later-run.md)
