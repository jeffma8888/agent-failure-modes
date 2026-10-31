---
id: INC-0155
title: A kill rehearsal met its timeout but nobody checked what the killed process left behind
date: 2026-10-30
classes: [false-green, ipc-and-env]
severity: medium
status: fixed
---

# INC-0155 - A kill rehearsal met its timeout but nobody checked what the killed process left behind

**Cost:** Minor: caught in review before it shipped.

## Signature - how you recognise it

A rehearsal passed on elapsed time while the leftovers of the killed run were unexamined.

## What happened

In a kill rehearsal the timeout was easy to meet, but what the killed process leaves behind was the real question, and a registry sweep only reaps runs that used the same temporary directory setting.

## Root cause

The rehearsal was judged on the timeout, and the temporary directory setting was not part of the operator contract.

## Why it was hard to see

The timeout is the visible number; the leftovers and the sweep scope are not.

## Fix

Check what the killed process leaves, and put the temporary directory setting in the operator contract.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In a kill rehearsal, inspect the leftovers, and state the temporary directory setting the sweep depends on.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
