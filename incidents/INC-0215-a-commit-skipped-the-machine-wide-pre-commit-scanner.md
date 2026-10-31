---
id: INC-0215
title: A commit skipped the machine-wide pre-commit scanner
date: 2026-10-31
classes: [detector-fail-open, vcs-destruction]
severity: medium
status: fixed
---

# INC-0215 - A commit skipped the machine-wide pre-commit scanner

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The scanner never ran.

## What happened

A commit was made with the hook path overridden, which skipped a machine-wide pre-commit scanner.

## Root cause

A commit was made with the hook path overridden, which skipped a machine-wide pre-commit scanner.

## Why it was hard to see

The commit succeeds without the scanner.

## Fix

Amend with hooks on right away if it happens

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never override the hook path; if it happens, amend with hooks on right away

## Related

[INC-0162](./INC-0162-a-chained-amend-reworded-the-previous-commit-after-a-failed.md)
