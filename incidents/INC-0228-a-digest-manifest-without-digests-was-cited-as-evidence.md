---
id: INC-0228
title: A digest manifest without digests was cited as evidence
date: 2026-10-31
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0228 - A digest manifest without digests was cited as evidence

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The manifest looked complete and held no digests.

## What happened

A backup digest manifest listed file names with no digests and was cited as evidence.

## Root cause

A backup digest manifest listed file names with no digests and was cited as evidence.

## Why it was hard to see

A list of names looks like a list of digests.

## Fix

Keep the bad file and add a correct one beside it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check that a manifest has one digest per line before citing it

## Related

[INC-0183](./INC-0183-sibling-fixture-factories-lacked-the-metadata-that-makes-a-c.md)
