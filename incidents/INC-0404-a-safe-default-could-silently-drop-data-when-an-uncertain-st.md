---
id: INC-0404
title: A safe default could silently drop data when an uncertain state was read as gone
date: 2026-11-02
classes: [detector-fail-open]
severity: medium
status: fixed
---

# INC-0404 - A safe default could silently drop data when an uncertain state was read as gone

**Cost:** A permission error could have been read as proof an item was gone, and data dropped.

## Signature - how you recognise it

A safe default treated a refused read as an absent item.

## What happened

a reviewer named a lead decision, that a permission error reads as the item being gone, on which a safe default could silently drop data; the lead ruled fail closed, so uncertain equals survivor

## Root cause

the decision on what an unreadable state means was not written down, so the default chose the destructive reading

## Why it was hard to see

The default looked safe because it matched the common case where an absent item is really gone.

## Fix

Treat an uncertain state as present: uncertain equals survivor, and fail closed

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a state is uncertain, treat the item as surviving; fail closed, never read a refusal as gone

## Related

[INC-0378](./INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md) [INC-0394](./INC-0394-a-security-predicate-checked-for-truthiness-failed-open-on-a.md) [INC-0380](./INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md)
