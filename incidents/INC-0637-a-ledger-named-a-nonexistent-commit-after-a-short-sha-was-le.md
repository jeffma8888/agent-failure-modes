---
id: INC-0637
title: A ledger named a nonexistent commit after a short SHA was lengthened by hand
date: 2026-11-12
classes: [false-green]
severity: low
status: mitigated
---

# INC-0637 - A ledger named a nonexistent commit after a short SHA was lengthened by hand

**Cost:** Two ledger lines named a nonexistent commit; both were corrected before any teammate read them.

## Signature - how you recognise it

A recorded SHA has the tool-produced prefix but a hand-added suffix that does not match the real commit.

## What happened

A landing command printed the new commit as an eight-character SHA. While writing two ledger lines, the lead typed a ninth hexadecimal digit rather than copying a longer SHA from git. A subsequent git rev-parse --short=9 in the same call printed a different ninth digit. The lead caught the mismatch in that call's output and corrected both lines to the original eight-character value before any teammate read them.

## Root cause

An opaque identifier already available from tool output was treated as editable text, and a longer form was invented by hand rather than obtained from git.

## Why it was hard to see

The prefix was correct and the extra character was valid hexadecimal, so the longer value looked like a more precise citation. Waiting for the landing output alone does not prevent corrupting a value while copying it.

## Fix

Copy the SHA verbatim at the length the tool printed it. If a different length is needed, run git rev-parse first and copy that output; correct each affected ledger line from the observed value.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never lengthen, shorten or retype a SHA by hand; every SHA in a record is a verbatim copy of tool output at the length shown. For a different length, obtain that form from git before writing the record.

## Related

[INC-0634](./INC-0634-a-record-naming-a-commit-id-was-written-in-the-same-parallel.md)
