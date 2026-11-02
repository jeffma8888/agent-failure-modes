---
id: INC-0464
title: Color escape codes in a report broke an extraction assertion, and only the zero match assertion caught it
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0464 - Color escape codes in a report broke an extraction assertion, and only the zero match assertion caught it

**Cost:** None: nothing was written.

## Signature - how you recognise it

An extraction found no matches in a report that held the text.

## What happened

a script that extracted counts from a report failed because the report carried terminal color escape codes; no bytes were written, because the zero match assertion stopped it before the write

## Root cause

escape codes sat inside the text being matched

## Why it was hard to see

The text looked right on screen, and the codes are invisible.

## Fix

strip escape codes before extracting, and keep an assertion that fails when nothing matched

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Strip terminal escape codes before parsing a report, and keep a zero match assertion so a failed extraction writes nothing

## Related

[INC-0084](./INC-0084-test-summary-assertions-broke-on-ansi-color-codes-and-compil.md) [INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md) [INC-0321](./INC-0321-a-green-parallel-run-was-cited-although-the-parallel-group-h.md)
