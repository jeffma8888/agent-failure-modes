---
id: INC-0054
title: A display name drifted from the model identifier it was supposed to describe
date: 2026-10-29
classes: [identity-and-keying, observability]
severity: low
status: fixed
---

# INC-0054 - A display name drifted from the model identifier it was supposed to describe

**Cost:** A roster and review credits named a newer model than the one that actually did the work. Caught before a routing policy was written on top of it.

## Signature - how you recognise it

Credits, rosters or reports carry a hand-typed model name next to an identifier that was typed separately.

## What happened

A reviewer agent was recorded under the name of a newer model version but had been spawned with the older model's identifier; the newer identifier existed and worked. Roster and review credits named the newer model.

## Root cause

Two fields that must agree were maintained independently: the human-readable name and the machine identifier. The name is what readers see, the identifier is what runs, and nothing tied them together.

## Why it was hard to see

The name looks authoritative and the work product is fine, so there is no symptom. The mismatch exists only in the record.

## Fix

Roster rows carry the exact model identifier, and display names are derived from the identifier, never typed separately. The registry identifiers were probed one by one before the routing policy was written.

## Verification

Each identifier was probed against the registry and compared with the roster row.

## Transferable rule

> Record the exact model ID wherever a model is credited, and derive the display name from it. A display name is not evidence of which model did the work.

## Related

[INC-0053](./INC-0053-a-command-line-agent-silently-ran-an-older-model-than-assume.md) [INC-0027](./INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md)
