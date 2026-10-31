---
id: INC-0169
title: A garbage collection test with a moved clock reaped the outer tier own live database
date: 2026-10-30
classes: [test-isolation, concurrency]
severity: medium
status: fixed
---

# INC-0169 - A garbage collection test with a moved clock reaped the outer tier own live database

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A test removed a database that belonged to the run that was executing it.

## What happened

A garbage collection test with a moved clock could reap the live database of the outer tier running it.

## Root cause

The full tier created its database before running the harness step.

## Why it was hard to see

The collision depends on order and on which tier owns the database.

## Fix

Run the harness step before the full tier owns a database, with the same isolation as the fast tier.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that reaps shared resources must run before the outer run owns any.

## Related

[INC-0143](./INC-0143-two-branches-implementing-the-same-stage-split-were-merged-w.md)
