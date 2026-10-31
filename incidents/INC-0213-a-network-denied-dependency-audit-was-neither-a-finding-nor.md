---
id: INC-0213
title: A network-denied dependency audit was neither a finding nor a pass
date: 2026-10-31
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0213 - A network-denied dependency audit was neither a finding nor a pass

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The audit could not run and exited like a result.

## What happened

A network-denied dependency audit is neither a vulnerability finding nor a pass, and an error code shared with other failures hides the difference.

## Root cause

A network-denied dependency audit is neither a vulnerability finding nor a pass, and an error code shared with other failures hides the difference.

## Why it was hard to see

The exit code looks the same as a real result.

## Fix

Classify it by its exact signature as the offline warning, and keep other errors with the same code failing

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Classify a network-denied audit by its exact signature, and keep other errors with the same code failing

## Related

[INC-0200](./INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md)
