---
id: INC-0302
title: A plan revision left stale operative text that only an independent review caught
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0302 - A plan revision left stale operative text that only an independent review caught

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A revised plan still directed work to a superseded file and carried wrong counts.

## What happened

a revision replaced a file but left an operative sentence naming the superseded one, and a heading count no longer matched its table; both lay outside the lines the revision touched

## Root cause

a revision replaced a file but left an operative sentence naming the superseded one, and a heading count no longer matched its table; both lay outside the lines the revision touched

## Why it was hard to see

The edited lines are right, so the stale lines are not looked at.

## Fix

Have a different reviewer check every operative sentence and count against the replacement

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> After a revision, check every operative sentence and count against the replacement, using a reviewer who did not write it

## Related

[INC-0217](./INC-0217-a-fixed-test-count-in-an-exit-criterion-went-stale.md)
