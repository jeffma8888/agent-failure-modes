---
id: INC-0254
title: Raw evidence was deleted with the scratch area
date: 2026-11-01
classes: [observability, checkpoint]
severity: medium
status: fixed
---

# INC-0254 - Raw evidence was deleted with the scratch area

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Only extracted tables survived.

## What happened

A negative-proof runner deleted its scratch area with the raw evidence JSON inside it.

## Root cause

A negative-proof runner deleted its scratch area with the raw evidence JSON inside it.

## Why it was hard to see

Cleanup is the last step and the evidence was in its path.

## Fix

Copy evidence and logs out before cleanup

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Copy raw evidence and logs out of a scratch area before the cleanup runs

## Related

[INC-0258](./INC-0258-a-failed-closing-run-could-leave-a-signed-record-public.md) [INC-0357](./INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md)
