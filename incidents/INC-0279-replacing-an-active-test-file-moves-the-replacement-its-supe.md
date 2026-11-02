---
id: INC-0279
title: Replacing an active test file moves the replacement, its supersession record and the registry line in one commit
date: 2026-11-01
classes: [identity-and-keying, checkpoint]
severity: medium
status: fixed
---

# INC-0279 - Replacing an active test file moves the replacement, its supersession record and the registry line in one commit

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A supersession record was refused in both path forms because the replacement had not moved yet.

## What happened

the supersession record for replacing an already active test file was refused in pending-path form, then in active-path form the identity checker refused it as duplicate pending and active copies while the new pending payload still existed

## Root cause

the supersession record for replacing an already active test file was refused in pending-path form, then in active-path form the identity checker refused it as duplicate pending and active copies while the new pending payload still existed

## Why it was hard to see

Each half of the change is valid only if the other half is present.

## Fix

Move the replacement as a pure rename activation, its supersession record in active-path form and the registry line in one commit

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Move a replacement, its supersession record and its registry line together in one commit when the old file is already active

## Related

[INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md) [INC-0419](./INC-0419-a-registry-edit-failed-its-own-sorted-order-assertion-and-th.md)
