---
id: INC-0182
title: A marker generator covered every payload of a root when only part was approved
date: 2026-10-30
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0182 - A marker generator covered every payload of a root when only part was approved

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A marker claimed more than the ruling approved.

## What happened

A marker generator emitted an edge for every payload of a root, giving four edges where the ruling approved two.

## Root cause

The generator knew roots, not approvals.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Filter the edges to the approved payload and prove the marker on a scratch clone.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A marker covers only what the ruling approved.

## Related

[INC-0167](./INC-0167-a-revision-marker-added-a-second-edge-to-bytes-the-previous.md)
