---
id: INC-0111
title: HTTP-only timeouts were copied from a process-hang pattern without the reason
date: 2026-10-30
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0111 - HTTP-only timeouts were copied from a process-hang pattern without the reason

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

A timeout override appears in a test where its original cause does not apply.

## What happened

Timeout overrides written for a process-hang pattern were copied into HTTP-only tests, with no record of why they were needed.

## Root cause

The override travelled without its reason, so nobody could judge whether it still applied.

## Why it was hard to see

The value looks harmless and the missing reason is not visible.

## Fix

Require a reason comment naming the real lifecycle for every timeout override.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An override without a stated reason is not reviewable.

## Related

[INC-0093](./INC-0093-a-smoke-run-deadline-shared-the-normal-step-budget-policy.md) [INC-0107](./INC-0107-a-timeout-override-was-not-re-checked-against-the-newest-rul.md)
