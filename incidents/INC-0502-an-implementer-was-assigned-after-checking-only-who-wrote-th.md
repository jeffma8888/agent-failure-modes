---
id: INC-0502
title: An implementer was assigned after checking only who wrote the test payload, and the root also held a coverage statement the implementer had written
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0502 - An implementer was assigned after checking only who wrote the test payload, and the root also held a coverage statement the implementer had written

**Cost:** One assignment and one round trip: the implementer stopped before any work and the row was reassigned.

## Signature - how you recognise it

An author-conflict check was run on one file of a root, and a different file of the same root named the assignee as author.

## What happened

The lead assigned an implementer to an early row after checking only that the implementer had not authored the test payload. The root also contained a coverage statement that the implementer had written. The implementer ran its own check, found its name on that file, and stopped. The coverage statement was ruled to be part of the root, and the row was reassigned to another implementer with the same author and reviewer check.

## Root cause

The check was scoped to the file most obviously authored, not to every file of the root, so coverage statements and approval markers were left out.

## Why it was hard to see

The payload is the visible product of the authors, so checking it feels complete; the other files of a root are short and easy to forget as authored work.

## Fix

Check the author of every file of the root, including coverage statements and approval markers, by version-control log and a name search, before the assignment is sent. Keep the implementer own check as the second line.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An author-conflict check covers every file of the root, including coverage statements and approval markers, by log and a name search, before the assignment is sent; the implementer own check stays as the second line.

## Related

[INC-0467](./INC-0467-a-run-plan-barred-the-test-author-from-running-the-script-an.md)
