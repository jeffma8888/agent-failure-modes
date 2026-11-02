---
id: INC-0437
title: Evidence receipts leaked absolute paths into branch history, and the lead landed by squash instead of rewriting history
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0437 - Evidence receipts leaked absolute paths into branch history, and the lead landed by squash instead of rewriting history

**Cost:** The leaking history stayed out of main; the squash step was added.

## Signature - how you recognise it

The leak guard reported absolute paths and a tool name inside evidence files.

## What happened

thirteen leak-guard hits were absolute home paths and a tool name in the recorded commands of an evidence file; the lead had the engineer rewrite the file without them, noting that earlier receipts carry literal paths in branch history, and landed through a squash so the leaking history is not merged, keeping the original branch local as the audit trail, never pushed or deleted

## Root cause

receipts recorded the literal command lines of the run

## Why it was hard to see

Literal command lines are exactly what an evidence file is for.

## Fix

write evidence commands with defined placeholders for the pinned binary and temp locations, and handle leaked history by a squash landing, not a history rewrite

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write evidence commands with placeholders for paths and tools; handle leaked history by a squash landing that keeps the original branch as the local audit trail

## Related

[INC-0081](./INC-0081-reviewers-and-qa-wrote-absolute-home-paths-and-notes-paths-i.md) [INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md)
