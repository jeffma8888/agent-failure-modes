---
id: INC-0051
title: A fallible edit script followed by a semicolon let the commit run on a partial result
date: 2026-10-28
classes: [tooling-paths, false-green]
severity: low
status: fixed
---

# INC-0051 - A fallible edit script followed by a semicolon let the commit run on a partial result

**Cost:** One commit whose message named three files while its content held two. Fixed forward in the next commit; no data lost.

## Signature - how you recognise it

A script that writes several files is followed by a commit joined with a semicolon, and the script's output contains a traceback.

## What happened

An edit script made three anchored replacements across three files, followed by a semicolon and then add and commit. The third assertion failed because its anchor appeared twice, but the first two files had already been written, and the semicolon let the commit run anyway. A partial edit was committed under a message describing all three.

## Root cause

Two compounding gaps. The script wrote each file as soon as its own check passed instead of checking every precondition first, so failure left a partial state. And a semicolon runs the next command regardless of the previous exit status, so the failure did not stop the publish step.

## Why it was hard to see

The commit succeeds and its message is confident. The only signal is a traceback earlier in the same output, easy to skim past when the last lines look like a normal commit.

## Fix

Chain every step after a fallible script with a short-circuit and (or use errexit). Have multi-file edit scripts verify every anchor before writing any file.

## Verification

The traceback was seen in the output and a stat of the commit showed only two of three files; the next commit completed the third.

## Transferable rule

> Validate all preconditions before the first write, and never let a later step run after an earlier one failed: join dependent steps with a short-circuit and, not a semicolon.

## Related

[INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) [INC-0046](./INC-0046-a-script-with-external-writes-was-only-dry-run-for-its-first.md)
