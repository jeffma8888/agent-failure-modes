---
id: INC-0207
title: Three sends failed because a packed string went out as one argument
date: 2026-10-30
classes: [tooling-paths, delegation]
severity: medium
status: fixed
---

# INC-0207 - Three sends failed because a packed string went out as one argument

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The sends failed with exit 1.

## What happened

In zsh an unquoted variable does not word split, so a loop that does set -- on a packed string sent the whole string as one argument.

## Root cause

In zsh an unquoted variable does not word split, so a loop that does set -- on a packed string sent the whole string as one argument.

## Why it was hard to see

The same code works in other shells.

## Fix

Redo with a function taking real arguments, and check the exit status of every send

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check the exit status of every send, and pass real arguments, not a packed string

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md)
