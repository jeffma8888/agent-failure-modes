---
id: INC-0386
title: A path-identity guard compared strings while a temp directory has two spellings on the host
date: 2026-11-01
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0386 - A path-identity guard compared strings while a temp directory has two spellings on the host

**Cost:** The same directory was treated as two, so an identity check gave the wrong answer.

## Signature - how you recognise it

Two spellings of one directory compared unequal.

## What happened

on this host a temp directory has two spellings, a symlinked prefix and its real path, so a path-identity guard that compared strings treated one directory as two

## Root cause

the guard compared path strings and did not resolve symbolic prefixes

## Why it was hard to see

The two spellings print differently but name one directory, and only some hosts have the alias.

## Fix

Compare real paths, never strings, in a path-identity guard

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A path-identity guard compares real paths, never strings

## Related

[INC-0126](./INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) [INC-0370](./INC-0370-a-scrub-command-was-refused-as-a-broad-home-directory-scan-b.md)
