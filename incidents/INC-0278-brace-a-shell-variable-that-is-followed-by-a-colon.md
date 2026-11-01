---
id: INC-0278
title: Brace a shell variable that is followed by a colon
date: 2026-11-01
classes: [tooling-paths]
severity: medium
status: fixed
---

# INC-0278 - Brace a shell variable that is followed by a colon

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A shell variable followed by a colon was read as a modifier.

## What happened

in zsh, writing a variable directly before a colon (the git object form sha colon path) applied a history modifier to the variable and produced a bad object name; bracing the variable fixed it

## Root cause

in zsh, writing a variable directly before a colon (the git object form sha colon path) applied a history modifier to the variable and produced a bad object name; bracing the variable fixed it

## Why it was hard to see

The command line looks correct.

## Fix

Brace the variable

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Always brace a shell variable that is followed by a colon

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md) [INC-0207](./INC-0207-three-sends-failed-because-a-packed-string-went-out-as-one-a.md)
