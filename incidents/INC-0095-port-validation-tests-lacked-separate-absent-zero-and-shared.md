---
id: INC-0095
title: Port validation tests lacked separate absent, zero and shared-port negatives and a positive callback control
date: 2026-10-30
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0095 - Port validation tests lacked separate absent, zero and shared-port negatives and a positive callback control

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

One combined negative case passes for any of several unrelated reasons.

## What happened

Port validation was tested without distinct cases for an absent port, port zero and a port shared with another listener, and with no positive control in the same flow.

## Root cause

Negatives were merged and the validator was never shown to accept a valid port.

## Why it was hard to see

A merged refusal case stays green when only one of its branches works.

## Fix

Test absent, zero and shared-port negatives separately, plus a positive callback control in the same flow.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> One negative per rejection reason, and a positive control in the same flow.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
