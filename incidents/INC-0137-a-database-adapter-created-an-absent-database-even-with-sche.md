---
id: INC-0137
title: A database adapter created an absent database even with schema push disabled
date: 2026-10-30
classes: [tooling-paths, test-isolation]
severity: medium
status: fixed
---

# INC-0137 - A database adapter created an absent database even with schema push disabled

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A misspelled or missing database name silently becomes a new empty database.

## What happened

Payload 3 db-postgres created an absent database even with push false, so a missing database was not a failure.

## Root cause

The adapter default is to create the database on connect.

## Why it was hard to see

The run proceeds against an empty database and fails later for unrelated reasons.

## Fix

Set disableCreateDatabase so a missing database is a named failure.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Make a missing database fail by name instead of creating it.

## Related

[INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md)
