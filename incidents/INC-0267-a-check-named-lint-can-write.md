---
id: INC-0267
title: A check named lint can write
date: 2026-11-01
classes: [spec-and-scope, tooling-paths]
severity: medium
status: fixed
---

# INC-0267 - A check named lint can write

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A check named as read only could create directories.

## What happened

lint-config is not read only by construction: its loader calls mkdir, so a check named lint can write (R-EC)

## Root cause

lint-config is not read only by construction: its loader calls mkdir, so a check named lint can write (R-EC)

## Why it was hard to see

The name suggests safety and the write is one line deep.

## Fix

Run it as written only where the directories already exist, and state that the call is a no-op there

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not assume a read-named check is read only; read its loader

## Related

[INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md)
