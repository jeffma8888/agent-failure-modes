---
id: INC-0211
title: A regex literal was read as a file path by the permission checker
date: 2026-10-31
classes: [tooling-paths]
severity: medium
status: fixed
---

# INC-0211 - A regex literal was read as a file path by the permission checker

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A harmless probe was blocked as a path access.

## What happened

A permission checker read a slash delimited regular expression literal on a command line as a file path.

## Root cause

A permission checker read a slash delimited regular expression literal on a command line as a file path.

## Why it was hard to see

The command is valid and the block looks unrelated.

## Fix

Put probe code in a file inside the scratch tree and prefer plain string tests

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put probe code in a file inside the scratch tree; prefer plain string tests over regex literals on a command line

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md)
