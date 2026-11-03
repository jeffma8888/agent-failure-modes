---
id: INC-0545
title: A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0545 - A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root

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
