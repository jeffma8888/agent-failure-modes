---
id: INC-0240
title: An auto-merge of a helper could lose an activation or coverage unnoticed
date: 2026-10-31
classes: [identity-and-keying, false-green]
severity: medium
status: fixed
---

# INC-0240 - An auto-merge of a helper could lose an activation or coverage unnoticed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The bytes were right and a project could still drop out.

## What happened

Approved successor bytes plus an explicit predecessor edge make a helper auto-merge safe, but do not show that no activation or coverage was lost.

## Root cause

Approved successor bytes plus an explicit predecessor edge make a helper auto-merge safe, but do not show that no activation or coverage was lost.

## Why it was hard to see

The bytes are the visible part.

## Fix

Run an ordered two-parent history check and an exact-run project inventory to show no activation or coverage was lost

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove an auto-merge by an ordered two-parent history check and an exact-run project inventory

## Related

[INC-0175](./INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md)
