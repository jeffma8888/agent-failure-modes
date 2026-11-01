---
id: INC-0227
title: A retry wrapper logged the dependency stderr privately and starved the caller diagnosis
date: 2026-10-31
classes: [observability, detector-fail-open]
severity: medium
status: fixed
---

# INC-0227 - A retry wrapper logged the dependency stderr privately and starved the caller diagnosis

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A long outage was reported with an empty cause.

## What happened

A wrapper around a flaky credential helper captured the helper stderr into its own log and emitted nothing on its own stderr, so a classifier above it saw an empty stderr and reported no category for a 13 hour outage.

## Root cause

A wrapper around a flaky credential helper captured the helper stderr into its own log and emitted nothing on its own stderr, so a classifier above it saw an empty stderr and reported no category for a 13 hour outage.

## Why it was hard to see

Each layer worked; the failure channel was dropped between them.

## Fix

On final failure the wrapper re-emits the last attempt redacted stderr on its own stderr; retries that eventually succeed stay silent.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A wrapper must preserve the failure channel of what it wraps, passing the last cause through on final failure.

## Related

[INC-0200](./INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md)
