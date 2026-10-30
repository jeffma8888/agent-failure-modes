---
id: INC-0119
title: A sandboxed HOME hid tool caches such as package-manager shims
date: 2026-10-30
classes: [ipc-and-env, test-isolation]
severity: medium
status: fixed
---

# INC-0119 - A sandboxed HOME hid tool caches such as package-manager shims

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

A tool works normally and fails once HOME points at a temp directory.

## What happened

A sandboxed HOME hid tool caches, such as package-manager shims, so tools failed or tried to fetch.

## Root cause

The cache location was derived from HOME and was not forwarded.

## Why it was hard to see

The failure looks like a missing tool.

## Fix

Forward the cache location explicitly and disable network fetches.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When replacing HOME, forward every cache the tools need and block fetching.

## Related

[INC-0106](./INC-0106-deleting-postgresql-environment-variables-left-client-tools.md)
