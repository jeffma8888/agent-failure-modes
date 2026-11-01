---
id: INC-0273
title: A status check must take every client reading
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0273 - A status check must take every client reading

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

One client reading of a status disagreed with the others.

## What happened

a session-cookie raw request answered 200 while browser navigation and in-page fetch answered 404 for the same path

## Root cause

a session-cookie raw request answered 200 while browser navigation and in-page fetch answered 404 for the same path

## Why it was hard to see

The browser view alone looks correct.

## Fix

Check the status with every client reading and do not accept a fix on one

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Take every client reading of a status before calling it fixed

## Related

[INC-0265](./INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md)
