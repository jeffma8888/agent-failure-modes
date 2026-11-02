---
id: INC-0091
title: Teammate replies arrived while the lead was busy and were missed, leaving finished work idle for about 30 minutes
date: 2026-10-30
classes: [delegation, observability]
severity: medium
status: fixed
---

# INC-0091 - Teammate replies arrived while the lead was busy and were missed, leaving finished work idle for about 30 minutes

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A teammate finished and replied, but the lead assumed work was still in flight.

## What happened

Replies arrived while the lead was busy and went unnoticed, so four teammates sat idle with finished work for about 30 minutes.

## Root cause

The lead relied on being woken by replies rather than checking who spoke last.

## Why it was hard to see

A quiet thread looks identical to work in progress.

## Fix

Check every teammate last speaker through conversation search before assuming work is in flight.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify the last speaker per teammate instead of assuming no news means work is running.

## Related

[INC-0416](./INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md) [INC-0469](./INC-0469-a-long-acceptance-run-launched-with-a-detached-command-insid.md)
