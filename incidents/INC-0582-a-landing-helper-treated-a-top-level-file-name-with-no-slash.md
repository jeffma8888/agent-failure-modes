---
id: INC-0582
title: A landing helper treated a top-level file name with no slash as a test root, so it copied nothing for it
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0582 - A landing helper treated a top-level file name with no slash as a test root, so it copied nothing for it

**Cost:** The commit stopped, nothing wrong landed; the file was copied by hand and committed after identity and backlog checks.

## Signature - how you recognise it

A helper classifies an argument by its shape, and a plain file name falls into the wrong class.

## What happened

The lead landing helper treated a top-level file name with no slash as a pending root, copied nothing for it, and the commit stopped. The lead copied the file, reran the identity and backlog checks, and committed. The helper now treats any name with a dot or a slash as a file. The same shape guess had failed on the same file at an earlier landing.

## Root cause

The class of an argument was inferred from its spelling.

## Why it was hard to see

A bare file name looks like a name of a root.

## Fix

Treat a name with a dot or a slash as a file, and stop when nothing is copied.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A helper that classifies arguments by shape must treat a name with a dot or a slash as a file and must stop when an argument copies nothing.

## Related

[INC-0545](./INC-0545-a-landing-helper-guessed-the-kind-of-each-argument-from-its.md)
