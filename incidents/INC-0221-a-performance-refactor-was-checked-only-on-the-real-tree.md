---
id: INC-0221
title: A performance refactor was checked only on the real tree
date: 2026-10-31
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0221 - A performance refactor was checked only on the real tree

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Equal output on the real tree hid changed failure behavior.

## What happened

A performance refactor of a checker was at risk of being accepted on equal output on the real tree alone.

## Root cause

A performance refactor of a checker was at risk of being accepted on equal output on the real tree alone.

## Why it was hard to see

The happy path matches.

## Fix

Run old and new on the same fixtures; equal output on the real tree alone is not enough

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a performance refactor with old and new on the same failure fixtures

## Related

[INC-0214](./INC-0214-a-helper-was-fixed-and-a-caller-still-passed-a-literal-empty.md)
