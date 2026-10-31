---
id: INC-0180
title: A readiness check ran without the dispatcher environment
date: 2026-10-30
classes: [ipc-and-env, false-green]
severity: medium
status: fixed
---

# INC-0180 - A readiness check ran without the dispatcher environment

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A missing variable read as a missing tool.

## What happened

A readiness check ran in the operator shell without the agent and database variables the live dispatcher has.

## Root cause

The operator shell differs from the dispatcher environment.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Run the check with the live dispatcher variables.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run readiness checks with the live dispatcher environment.

## Related

[INC-0145](./INC-0145-a-readiness-check-measured-the-lead-checkout-while-preship-m.md)
