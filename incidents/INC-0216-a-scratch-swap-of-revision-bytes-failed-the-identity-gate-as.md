---
id: INC-0216
title: A scratch swap of revision bytes failed the identity gate as designed
date: 2026-10-31
classes: [identity-and-keying, false-green]
severity: medium
status: fixed
---

# INC-0216 - A scratch swap of revision bytes failed the identity gate as designed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The gate failed for the right reason, which the proof had not intended.

## What happened

A scratch swap of revision bytes without their approved supersession chain correctly fails the identity gate.

## Root cause

A scratch swap of revision bytes without their approved supersession chain correctly fails the identity gate.

## Why it was hard to see

Bytes look like the whole identity.

## Fix

Use the real chain in the proof

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Use the real approved chain in a causal proof, not just the bytes

## Related

[INC-0204](./INC-0204-a-precommit-check-reported-a-merge-brought-approval-as-unrea.md)
