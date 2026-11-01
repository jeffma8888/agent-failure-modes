---
id: INC-0239
title: A hold outcome had no proof that nothing changed
date: 2026-10-31
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0239 - A hold outcome had no proof that nothing changed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

No change looks the same as no run.

## What happened

A hold index is an explicit no-selection outcome and needed proof that nothing moved.

## Root cause

A hold index is an explicit no-selection outcome and needed proof that nothing moved.

## Why it was hard to see

Absence of change is hard to prove.

## Fix

Prove it by the remote main SHA unchanged before and after and the build clone porcelain empty

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a hold by the remote main SHA unchanged before and after and an empty porcelain on the build clone

## Related

[INC-0228](./INC-0228-a-digest-manifest-without-digests-was-cited-as-evidence.md)
