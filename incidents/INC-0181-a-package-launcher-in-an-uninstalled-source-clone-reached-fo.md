---
id: INC-0181
title: A package launcher in an uninstalled source clone reached for the registry
date: 2026-10-30
classes: [tooling-paths, ipc-and-env]
severity: medium
status: fixed
---

# INC-0181 - A package launcher in an uninstalled source clone reached for the registry

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A dispatch hung or failed on a network lookup.

## What happened

A package launcher run in an uninstalled source clone reached for the registry before it dispatched the script.

## Root cause

The launcher resolves the package before running it.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Install offline first.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Install offline before running a package launcher in a source clone.

## Related

[INC-0155](./INC-0155-a-kill-rehearsal-met-its-timeout-but-nobody-checked-what-the.md)
