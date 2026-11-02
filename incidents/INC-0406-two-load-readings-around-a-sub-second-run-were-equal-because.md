---
id: INC-0406
title: Two load readings around a sub-second run were equal because the host load average updates on a fixed interval
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
---

# INC-0406 - Two load readings around a sub-second run were equal because the host load average updates on a fixed interval

**Cost:** Equal readings could have been read as copied or invented.

## Signature - how you recognise it

Two readings of host load were identical around a very short run.

## What happened

two load readings taken around a sub-second run were equal because the host load average updates on a fixed interval; the lead's re-run showed the same, so equal readings are expected and were not copied

## Root cause

the load average updates on a fixed interval, longer than the run

## Why it was hard to see

Identical numbers look like a copy even when both were read.

## Fix

Treat equal readings around a very short run as expected; record both readings as read

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Equal load readings around a sub-second run are expected from the fixed update interval; record each as read, never copy

## Related

[INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0271](./INC-0271-a-load-induced-harness-red-is-not-headroom.md) [INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md)
