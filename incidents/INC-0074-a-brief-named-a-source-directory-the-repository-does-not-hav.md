---
id: INC-0074
title: A brief named a source directory the repository does not have, written from a conventional layout instead of a listing
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: low
status: fixed
---

# INC-0074 - A brief named a source directory the repository does not have, written from a conventional layout instead of a listing

**Cost:** Minor: one reviewer lost its first path lookup. Both recipients were lucky: one guessed the intent correctly, and a stricter reader could have refused the task or created the nonexistent directory.

## Signature - how you recognise it

A brief scopes work to a directory by name, and the name is the conventional one for the language or framework rather than one anyone listed.

## What happened

Two briefs told engineers to change or read files under a conventional source directory. The package actually lived at the repository root. The engineer inferred the real location, and the reviewer's first lookup failed.

## Root cause

The path rule was written from memory of a typical layout. A recipient has no way to tell a deliberate scope restriction from a stale one, so it either guesses, refuses, or builds the missing structure.

## Why it was hard to see

The conventional layout feels so obviously right that it is not checked, and a capable recipient silently repairs the error, which hides it.

## Fix

Later briefs name the real package path, copied from a listing of the repository taken when the brief is written.

## Verification

Checked: the two failing briefs against the actual repository layout. Not checked: whether later briefs are free of other stale paths.

## Transferable rule

> Write path rules in a brief from a listing taken when the brief is written, never from memory of a conventional layout.

## Related

[INC-0056](./INC-0056-test-seams-declared-from-memory-carried-wrong-field-names-an.md) [INC-0055](./INC-0055-a-scope-cut-was-mapped-against-the-previous-version-of-its-b.md)
