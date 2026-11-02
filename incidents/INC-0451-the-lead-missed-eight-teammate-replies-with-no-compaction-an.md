---
id: INC-0451
title: The lead missed eight teammate replies with no compaction and saw them only through thread activity
date: 2026-11-02
classes: [steering-channel]
severity: low
status: fixed
---

# INC-0451 - The lead missed eight teammate replies with no compaction and saw them only through thread activity

**Cost:** None beyond a delay: the outputs were on disk and were landed once seen.

## Signature - how you recognise it

Replies were missing from the lead view while the work sat finished.

## What happened

eight teammates finished between 05:11 and 05:21 and the lead saw the replies only through the thread activity listing, although no context compaction had happened

## Root cause

the lead checked for lost replies only after compactions

## Why it was hard to see

The lead assumed that no compaction meant every reply had arrived.

## Fix

check thread states after every landing batch, not only after a compaction

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check thread states after every landing batch, not only after a context compaction

## Related

[INC-0449](./INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md) [INC-0416](./INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md) [INC-0317](./INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md)
