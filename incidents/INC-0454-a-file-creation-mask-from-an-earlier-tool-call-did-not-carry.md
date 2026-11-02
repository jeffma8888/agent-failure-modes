---
id: INC-0454
title: A file creation mask from an earlier tool call did not carry over, and the database dump came out world readable
date: 2026-11-02
classes: [ipc-and-env]
severity: low
status: fixed
---

# INC-0454 - A file creation mask from an earlier tool call did not carry over, and the database dump came out world readable

**Cost:** None: caught by an assertion before use, and fixed at once.

## Signature - how you recognise it

A dump file was readable by others for a short time.

## What happened

a file creation mask set in an earlier tool call did not carry into a fresh shell, so the database dump tool wrote the custom format dump with mode 644 inside a 700 root; the runner mode assertion at its fourth step caught it, stopped correctly, created no database, and tightened the mode to 600 at once

## Root cause

shell state from an earlier call was assumed to persist

## Why it was hard to see

Each tool call starts a fresh shell, and the missing mask shows only in the file mode.

## Fix

create the dump in one command that sets the mask 077, runs the dump to the recorded path, captures the exit status, asserts mode 600 and a non zero size, and prints all three; a non zero exit or a mode other than 600 is a stop

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Set the mask, run, and assert the result in one command, because shell state does not carry across tool calls

## Related

[INC-0418](./INC-0418-the-milestone-runbook-shell-sourced-an-environment-file-and.md) [INC-0248](./INC-0248-the-env-script-could-not-be-sourced-in-zsh.md)
