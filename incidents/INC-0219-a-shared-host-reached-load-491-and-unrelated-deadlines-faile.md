---
id: INC-0219
title: A shared host reached load 491 and unrelated deadlines failed
date: 2026-10-31
classes: [concurrency, stage-timeout]
severity: medium
status: fixed
---

# INC-0219 - A shared host reached load 491 and unrelated deadlines failed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Unrelated deadlines failed under a shared load.

## What happened

The cap on heavy runs was per worker, so the team total overloaded the host to a load of 491.

## Root cause

The cap on heavy runs was per worker, so the team total overloaded the host to a load of 491.

## Why it was hard to see

Each worker kept to its own limit.

## Fix

Cap concurrent heavy runs across a team, not per worker (two), and record load at start and end with any overlap

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Cap concurrent heavy runs across the team and record load at start and end

## Related

[INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md)
