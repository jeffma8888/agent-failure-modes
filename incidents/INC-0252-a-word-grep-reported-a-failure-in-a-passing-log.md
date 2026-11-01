---
id: INC-0252
title: A word grep reported a failure in a passing log
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0252 - A word grep reported a failure in a passing log

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A test title contained the word.

## What happened

A word grep for failed over a passing log matched a passing test title.

## Root cause

A word grep for failed over a passing log matched a passing test title.

## Why it was hard to see

The word appears in names as well as in results.

## Fix

Count failures from the runner summary lines

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Count failures from runner summary lines, never from a word match

## Related

[INC-0182](./INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md)
