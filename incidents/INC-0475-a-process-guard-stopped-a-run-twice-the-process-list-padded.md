---
id: INC-0475
title: A process guard stopped a run twice: the process list padded the command with trailing spaces, and the guard's own shell line contained the searched name
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0475 - A process guard stopped a run twice: the process list padded the command with trailing spaces, and the guard's own shell line contained the searched name

**Cost:** Minor: two stops, each correct, before the run could start.

## Signature - how you recognise it

A guard that searches the process list failed on padding and on matching itself.

## What happened

A process guard that searches the process list for a name stopped a run twice. The process list pads a command string with trailing spaces and the comparison was byte exact. The second time, the guard's own shell line contained the searched name and matched itself. Stopping was correct both times because a guard that cannot tell must fail closed.

## Root cause

The comparison treated padding as content, and the search pattern appeared in the line that ran it.

## Why it was hard to see

Each failure looks like a real conflicting process, so it is hard to tell a false match from a true one.

## Fix

Compare process command strings after removing trailing whitespace only, keep everything else exact, and search with a self excluding pattern (a bracketed first letter) in a call that contains nothing else.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A process guard normalises only trailing whitespace in process list output and searches with a self excluding pattern in a call that contains nothing else; it keeps failing closed.

## Related

[INC-0386](./INC-0386-a-path-identity-guard-compared-strings-while-a-temp-director.md) [INC-0305](./INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md)
