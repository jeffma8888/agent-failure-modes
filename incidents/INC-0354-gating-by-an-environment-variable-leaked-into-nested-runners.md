---
id: INC-0354
title: Gating by an environment variable leaked into nested runners that copy the environment
date: 2026-11-01
classes: [ipc-and-env, test-isolation]
severity: medium
status: fixed
---

# INC-0354 - Gating by an environment variable leaked into nested runners that copy the environment

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A spec claimed an opt-in feature was inert in nested child runs, but a nested helper copied the whole environment and started a fresh runner directly.

## What happened

a spec claimed detailed timing was inert in nested child runs, but a nested test helper copies the whole environment and launches a fresh runner directly, bypassing the entry point that would have stripped the enabling switches

## Root cause

authority was carried by an inherited environment variable, and a child that copies the environment inherits the authority with it

## Why it was hard to see

The claim holds for the normal entry, so it was checked only through the path that strips the switches.

## Fix

Scope the authorization to the specific runner process (checked through its parent-process chain), so a copied environment grants nothing

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never treat an inherited environment variable as authority; bind it to the process that was authorized

## Related

[INC-0106](./INC-0106-deleting-postgresql-environment-variables-left-client-tools.md) [INC-0307](./INC-0307-a-measurement-wrapper-inherited-the-environment-the-tests-re.md) [INC-0342](./INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) [INC-0353](./INC-0353-an-authorization-point-was-placed-after-the-first-event-that.md)
