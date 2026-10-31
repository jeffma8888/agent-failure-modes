---
id: INC-0186
title: A per-root checker summary undercounted edges
date: 2026-10-30
classes: [detector-fail-open, identity-and-keying]
severity: medium
status: fixed
---

# INC-0186 - A per-root checker summary undercounted edges

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The summary showed fewer edges than the manifests hold.

## What happened

The per-root summary of the identity checker undercounts edges.

## Root cause

The summary groups by root, so shared edges collapse.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Derive the full marker set from the manifests.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Derive the marker set from the manifests, not from a per-root summary.

## Related

[INC-0182](./INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md)
