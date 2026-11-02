---
id: INC-0449
title: The lead missed six teammate replies across a context compaction and left the critical-path engineer idle for 35 minutes
date: 2026-11-02
classes: [steering-channel]
severity: low
status: fixed
---

# INC-0449 - The lead missed six teammate replies across a context compaction and left the critical-path engineer idle for 35 minutes

**Cost:** The critical-path engineer idled about 35 minutes.

## Signature - how you recognise it

Replies sat unread after a compaction.

## What happened

after a context compaction the lead missed replies from six teammates, which finished between 04:29 and 04:45 and were seen at 05:05 through the activity listing; the critical-path engineer had a stop waiting and sat idle for 35 minutes

## Root cause

the compaction dropped the lead's awareness of pending replies and nothing prompted a re-check

## Why it was hard to see

Nothing signalled that replies had arrived while the lead was working.

## Fix

check thread activity right after every compaction, before any other step

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check thread activity right after every context compaction, before any other step

## Related

[INC-0317](./INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md) [INC-0416](./INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md)
