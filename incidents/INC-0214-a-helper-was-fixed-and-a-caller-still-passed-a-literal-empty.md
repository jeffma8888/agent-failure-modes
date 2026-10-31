---
id: INC-0214
title: A helper was fixed and a caller still passed a literal empty object
date: 2026-10-31
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0214 - A helper was fixed and a caller still passed a literal empty object

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The helper fix left a caller broken.

## What happened

Fixing a shared helper internals did not fix a caller that passes a literal empty object to its typed parameter.

## Root cause

Fixing a shared helper internals did not fix a caller that passes a literal empty object to its typed parameter.

## Why it was hard to see

The helper tests pass.

## Fix

Check every caller with a strict destination compile

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check every caller of a fixed helper with a strict destination compile

## Related

[INC-0197](./INC-0197-a-typecheck-failed-in-a-shared-helper-the-revision-did-not-o.md)
