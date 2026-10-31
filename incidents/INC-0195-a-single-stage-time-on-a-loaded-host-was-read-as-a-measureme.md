---
id: INC-0195
title: A single stage time on a loaded host was read as a measurement
date: 2026-10-30
classes: [stage-timeout, observability]
severity: medium
status: fixed
---

# INC-0195 - A single stage time on a loaded host was read as a measurement

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The same tree read 30.5 s and then 14.9 s.

## What happened

One stage time on a loaded host was treated as a measurement; the same tree gave 30.5 s in one run and 14.9 s in the next.

## Root cause

One stage time on a loaded host was treated as a measurement; the same tree gave 30.5 s in one run and 14.9 s in the next.

## Why it was hard to see

A single number looks like a fact.

## Fix

Decide timing rules on repeated runs with the load recorded

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Decide timing rules on repeated runs with the load recorded, never on one stage time

## Related

[INC-0146](./INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md)
