---
id: INC-0093
title: A smoke-run deadline shared the normal step budget policy
date: 2026-10-30
classes: [stage-timeout]
severity: medium
status: fixed
---

# INC-0093 - A smoke-run deadline shared the normal step budget policy

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

One timeout policy covers both quick steps and a long smoke run.

## What happened

The smoke-run deadline was tied to normal step budgets, so a policy suited to one distorted the other.

## Root cause

A single budget mechanism was reused for runs with different expected durations.

## Why it was hard to see

Both look like timeouts, so sharing the mechanism seems tidy.

## Fix

Keep the smoke-run deadline policy separate from normal step budgets.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Give runs with different deadline purposes their own policy.

## Related

[INC-0092](./INC-0092-a-whole-group-termination-grace-period-was-shorter-than-the.md)
