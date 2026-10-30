---
id: INC-0092
title: A whole-group termination grace period was shorter than the wrapper process, so the wrapper exit ended the wait early
date: 2026-10-30
classes: [stage-timeout, concurrency]
severity: medium
status: fixed
---

# INC-0092 - A whole-group termination grace period was shorter than the wrapper process, so the wrapper exit ended the wait early

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A shutdown waits for a process group, but the wait ends when the wrapper process exits.

## What happened

A TERM grace period for a whole process group was tied to a wrapper process. When the wrapper exited, the wait ended before the group had finished.

## Root cause

The wait was bound to the first process to exit rather than to the whole group.

## Why it was hard to see

The wrapper usually exits last in simple runs, so the early end shows only with slow children.

## Fix

Make the group TERM grace period outlive any wrapper process.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Bind a group shutdown wait to the group, not to a wrapper that can exit first.
