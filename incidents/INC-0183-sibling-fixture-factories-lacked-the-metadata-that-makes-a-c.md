---
id: INC-0183
title: Sibling fixture factories lacked the metadata that makes a checker required
date: 2026-10-30
classes: [test-isolation, false-green]
severity: medium
status: fixed
---

# INC-0183 - Sibling fixture factories lacked the metadata that makes a checker required

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A positive control passed without reaching its negative.

## What happened

Complete metadata absence tells a required checker from an optional path, and sibling fixture factories did not carry the same required metadata, so the controls never reached the negatives they claim to test.

## Root cause

Each factory was written alone.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Give every sibling factory the same required metadata.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Sibling fixture factories carry the same required metadata.

## Related

[INC-0173](./INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md)
