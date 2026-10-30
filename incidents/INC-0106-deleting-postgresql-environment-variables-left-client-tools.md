---
id: INC-0106
title: Deleting PostgreSQL environment variables left client tools free to fall back to default host and port
date: 2026-10-30
classes: [ipc-and-env, test-isolation]
severity: medium
status: fixed
---

# INC-0106 - Deleting PostgreSQL environment variables left client tools free to fall back to default host and port

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A test clears PG variables to avoid the shared cluster, and a client tool uses its defaults.

## What happened

Isolation was attempted by deleting PG environment variables, which let client tools fall back to default host and port instead of the owned cluster.

## Root cause

Absence of a variable was treated as safety.

## Why it was hard to see

The default points at a working database, so nothing fails.

## Fix

Pin PGHOST and PGPORT to the owned cluster.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Pin the target explicitly; do not rely on removing the alternatives.
