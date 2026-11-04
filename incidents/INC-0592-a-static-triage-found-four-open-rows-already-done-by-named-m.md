---
id: INC-0592
title: A static triage found four open rows already done by named merges, and the freeze rule kept them open with the merge commit in the status text
date: 2026-11-04
classes: [checkpoint]
severity: low
status: mitigated
---

# INC-0592 - A static triage found four open rows already done by named merges, and the freeze rule kept them open with the merge commit in the status text

**Cost:** None. The rows would otherwise have been rescheduled or reported as unfinished.

## Signature - how you recognise it

Plan rows read as open although merged work already delivered them.

## What happened

A static triage found four open rows each already done by a named merge commit. A freeze rule keeps their state open, so each stays open and its merge commit is recorded in its status text. One follow-up, a set of weak assertions that only check a rejection is defined, was noted as a candidate successor and not scheduled.

## Root cause

Row state and merged work were tracked separately, and a freeze rule stops the state from being closed.

## Why it was hard to see

Without the commit in the text, an open row cannot be told apart from unfinished work.

## Fix

Triage open rows against main, keep the state the freeze rule requires, and record the delivering merge commit in each row's status text.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a freeze keeps a finished row open, record the delivering merge commit in its status text.

## Related

[INC-0160](./INC-0160-an-activation-was-tied-to-an-unreviewed-successor-and-had-to.md)
