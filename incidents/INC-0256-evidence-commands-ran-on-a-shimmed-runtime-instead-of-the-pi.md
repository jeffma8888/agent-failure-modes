---
id: INC-0256
title: Evidence commands ran on a shimmed runtime instead of the pinned one
date: 2026-11-01
classes: [ipc-and-env, false-green]
severity: medium
status: fixed
---

# INC-0256 - Evidence commands ran on a shimmed runtime instead of the pinned one

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The version reported was not the pinned one.

## What happened

Evidence commands in the shell used a shim that reported another version, while a script child used the pinned runtime.

## Root cause

Evidence commands in the shell used a shim that reported another version, while a script child used the pinned runtime.

## Why it was hard to see

The command name resolves to a shim.

## Fix

Run evidence commands with the pinned binary by absolute path and print its version in the log

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run evidence commands with the pinned binary by absolute path and print its version in the log

## Related

[INC-0180](./INC-0180-a-readiness-check-ran-without-the-dispatcher-environment.md)
