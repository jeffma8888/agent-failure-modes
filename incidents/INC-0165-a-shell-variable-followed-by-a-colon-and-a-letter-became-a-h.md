---
id: INC-0165
title: A shell variable followed by a colon and a letter became a history modifier
date: 2026-10-30
classes: [tooling-paths]
severity: medium
status: fixed
---

# INC-0165 - A shell variable followed by a colon and a letter became a history modifier

**Cost:** Minor: a wrong string until noticed.

## Signature - how you recognise it

A shell string produced a truncated value without an error.

## What happened

In zsh a variable followed by a colon and a letter is a history modifier (the :t tail), so the expanded string was silently changed.

## Root cause

The unbraced form is harmless in other shells and in most strings.

## Why it was hard to see

The output is plausible and no error is raised.

## Fix

Write the braces form before a colon in shell strings.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In zsh, write the braces form of a variable before a colon.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
