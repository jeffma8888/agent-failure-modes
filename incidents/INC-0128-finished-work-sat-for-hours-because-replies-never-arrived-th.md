---
id: INC-0128
title: Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept
date: 2026-10-30
classes: [delegation, observability]
severity: medium
status: fixed
---

# INC-0128 - Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

Several teammates finish, no reply arrives, and the lead waits.

## What happened

Seven teammates finished work and their replies never arrived. The lead read the clock wrong, assuming stamps from one hour when real time was hours later, and did not sweep worktrees, so finished roots sat about nine hours.

## Root cause

Progress was judged from replies and an assumed time instead of from disk and a real clock.

## Why it was hard to see

Everything looks quiet and the time error makes the delay look short.

## Fix

On every wake, list every worktree untracked roots and every new review file, with real time from the date command, before reading any reply.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Sweep the disk and read a real clock before trusting replies.

## Related

[INC-0091](./INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md)
