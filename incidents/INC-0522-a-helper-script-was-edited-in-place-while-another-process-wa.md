---
id: INC-0522
title: A helper script was edited in place while another process was executing it, and that run died with a syntax error at a shifted line
date: 2026-11-02
classes: [concurrency]
severity: medium
status: mitigated
---

# INC-0522 - A helper script was edited in place while another process was executing it, and that run died with a syntax error at a shifted line

**Cost:** One comparison run was lost and rerun; an earlier near miss was caught by restoring the bytes within seconds.

## Signature - how you recognise it

A script that other threads run is rewritten in place, and a running shell fails at a line number that no longer matches.

## What happened

A comparison script was edited in place while a process was executing it. The shell reads a script by file offset as it runs, so an inserted line shifts the rest. The first time the exact bytes were restored within seconds, before the process read past its current command. The second time another thread comparison died with a syntax error at a shifted line and was not evidence. The helpers are now read-only, a change is a new file name announced in a ruling, and reports quote the helper hash.

## Root cause

A shared helper was treated as editable like any file, though other threads execute it while it is edited.

## Why it was hard to see

The edit is correct and small, and the failure appears in another thread, at a line that looks like a bug in the script.

## Fix

Make shared helpers read-only, version a change by a new file name, and quote the helper hash in the evidence.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never rewrite a script in place while any process may run it; write a new file and switch names, and quote the helper hash in the evidence that used it.

## Related

[INC-0518](./INC-0518-a-landing-tool-read-a-bare-file-name-as-a-test-root-name-so.md) [INC-0497](./INC-0497-a-flag-that-hides-the-token-from-responses-left-first-user-r.md)
