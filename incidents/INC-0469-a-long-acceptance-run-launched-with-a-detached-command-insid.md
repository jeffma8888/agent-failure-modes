---
id: INC-0469
title: A long acceptance run launched with a detached command inside a subshell from a tool shell never started, and no output file existed minutes later
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0469 - A long acceptance run launched with a detached command inside a subshell from a tool shell never started, and no output file existed minutes later

**Cost:** A delay of several minutes before the missing run was noticed.

## Signature - how you recognise it

A launched run left no output and no process.

## What happened

the lead launched an acceptance run with a detached command inside a subshell from a tool shell; the run never started and no output file existed minutes later, because nothing checked that the launch had produced a first output file

## Root cause

the launch form was not one the tool shell supports, and no check followed it

## Why it was hard to see

A detached launch returns at once, so it looks successful.

## Fix

launch long runs as a tracked background task, and check that the run own first output file exists right after the launch

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Launch a long run as a tracked background task, and check that its first output file exists right after the launch

## Related

[INC-0325](./INC-0325-a-background-watcher-lacked-the-session-credentials-and-fail.md) [INC-0060](./INC-0060-a-probe-hung-on-a-background-child-that-held-the-pipe-and-th.md) [INC-0091](./INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md)
