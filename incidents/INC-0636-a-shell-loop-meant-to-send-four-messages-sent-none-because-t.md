---
id: INC-0636
title: A shell loop meant to send four messages sent none, because the shell does not split an unquoted variable into words
date: 2026-11-10
classes: [tooling-paths]
severity: low
status: mitigated
topic: tooling-paths/zsh-expansion-surprises
occurrences: 1
recurrence_of: INC-0207
---

# INC-0636 - A shell loop meant to send four messages sent none, because the shell does not split an unquoted variable into words

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [zsh reads your variable differently: colon modifier, word split, array](../catalog/tooling-paths/zsh-expansion-surprises.md)

> **Recurrence of [INC-0207](./INC-0207-three-sends-failed-because-a-packed-string-went-out-as-one-a.md).** This record repeats an earlier failure and is kept for history; INC-0207 is the canonical record (3 occurrences in total) and carries the rule to apply.

**Cost:** All four sends failed and were redone by hand; caught from that call's own output, with no work lost.

## Signature - how you recognise it

A loop over pair strings reports an empty argument or a not-found target for every item.

## What happened

A lead sent four briefs with one loop that took each quoted string holding a target id and a file name, split it with the positional-parameter builtin, then sent the second word to the first. The shell was zsh, which does not word-split an unquoted parameter expansion, so the first parameter held the whole string and the second was empty. The file read became a read of a directory, the send had no message, and the follow-up step reported the target not found. The lead saw this in the output and resent with one explicit command per target.

## Root cause

The loop relied on word splitting, and the shell in use does not do that by default.

## Why it was hard to see

The same loop works in bash, and a side-effecting loop gives no error until its output is read.

## Fix

Write one explicit command per item, or split explicitly with the shell's own syntax, and check each send's output for its success line before moving on.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not drive side-effecting actions through a loop that depends on word splitting without knowing the shell's splitting rule; prefer one explicit command per send and confirm each success line.

## Related

[INC-0634](./INC-0634-a-record-naming-a-commit-id-was-written-in-the-same-parallel.md) [INC-0599](./INC-0599-a-checklist-expected-a-slug-first-link-and-excused-absent-he.md)
