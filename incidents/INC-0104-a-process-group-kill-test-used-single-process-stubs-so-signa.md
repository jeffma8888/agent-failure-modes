---
id: INC-0104
title: A process-group kill test used single-process stubs, so signalling the leader and the group looked the same
date: 2026-10-30
classes: [false-green, concurrency]
severity: medium
status: fixed
---

# INC-0104 - A process-group kill test used single-process stubs, so signalling the leader and the group looked the same

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A group-kill test passes with stubs that have no descendants.

## What happened

A process-group kill test used single-process stubs, so killing only the leader and killing the whole group gave the same observable result.

## Root cause

The fixture had no descendant in the group.

## Why it was hard to see

The test goes green with a leader-only kill, so the gap is invisible.

## Fix

Put a descendant in the group and assert it is gone.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A group-kill test needs a descendant, or it cannot tell group from leader.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
