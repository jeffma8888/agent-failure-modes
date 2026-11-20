---
id: INC-0165
title: A shell variable followed by a colon and a letter became a history modifier
date: 2026-10-30
classes: [tooling-paths]
severity: medium
status: fixed
topic: tooling-paths/zsh-expansion-surprises
occurrences: 3
---

# INC-0165 - A shell variable followed by a colon and a letter became a history modifier

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [zsh reads your variable differently: colon modifier, word split, array](../catalog/tooling-paths/zsh-expansion-surprises.md)

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

## Recurrences

Occurrences: 3. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0278](./INC-0278-brace-a-shell-variable-that-is-followed-by-a-colon.md) - 2026-11-01 - Brace a shell variable that is followed by a colon
- [INC-0622](./INC-0622-an-unbraced-shell-variable-followed-by-a-colon-and-a-letter.md) - 2026-11-04 - An unbraced shell variable followed by a colon and a letter was read as a history modifier, so a revision was mangled and the hash printed was of empty input

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md) [INC-0362](./INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md)
