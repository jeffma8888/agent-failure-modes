---
id: INC-0149
title: Marker SHA, reviewer approval scope, successor closure and activation ownership were treated as one fact
date: 2026-10-30
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0149 - Marker SHA, reviewer approval scope, successor closure and activation ownership were treated as one fact

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A marker is read as proof of approval, closure and ownership at once.

## What happened

An audit found that marker SHA, reviewer approval scope, successor closure and activation ownership are four different facts, and old-path edges must stay globally unique.

## Root cause

One field was asked to carry four meanings.

## Why it was hard to see

Each meaning is plausible from the marker alone.

## Fix

Keep each fact explicit and keep old-path edges globally unique.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> One fact per field.

## Related

[INC-0125](./INC-0125-a-marker-generator-listing-every-earlier-unmarked-root-made.md)
