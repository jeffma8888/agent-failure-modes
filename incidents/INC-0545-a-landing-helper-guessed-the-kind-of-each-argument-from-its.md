---
id: INC-0545
title: A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: mitigated
topic: tooling-paths/argument-read-as-other-kind
occurrences: 1
recurrence_of: INC-0518
---

# INC-0545 - A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [A helper or runner reads your argument as a different kind or name](../catalog/tooling-paths/argument-read-as-other-kind.md)

> **Recurrence of [INC-0518](./INC-0518-a-landing-tool-read-a-bare-file-name-as-a-test-root-name-so.md).** This record repeats an earlier failure and is kept for history; INC-0518 is the canonical record (3 occurrences in total) and carries the rule to apply.

**Cost:** One landing attempt failed its backlog check; the file was copied by hand and committed again.

## Signature - how you recognise it

A helper treats any word without a slash or a leading underscore as a name of a kind, not as a file.

## What happened

The landing helper decided each argument by shape: one starting with an underscore or containing a slash was a path, and any other word was a pending root name. The backlog file, passed as a bare name, was taken as a root, the helper copied the files of a root of that name, and the backlog check failed. The lead copied the file by hand and recommitted.

## Root cause

The argument kind was inferred from its spelling instead of being stated.

## Why it was hard to see

A bare file name looks like a name of a root, and the failure appears only in the later check.

## Fix

State the kind of each argument explicitly, or reject a bare word that is not a known root.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A helper must not guess whether an argument is a path or a name; take an explicit kind or fail closed on an unknown bare word.

## Related

[INC-0518](./INC-0518-a-landing-tool-read-a-bare-file-name-as-a-test-root-name-so.md) [INC-0519](./INC-0519-a-root-was-passed-to-a-landing-helper-by-name-and-by-path-an.md)
