---
id: INC-0128
title: Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept
date: 2026-10-30
classes: [delegation, observability]
severity: medium
status: fixed
topic: delegation/finished-on-disk-no-reply
occurrences: 5
---

# INC-0128 - Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md) / [Teammates finished on disk; the reply never came or went unnoticed](../catalog/delegation/finished-on-disk-no-reply.md)

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

## Recurrences

Occurrences: 5. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0317](./INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md) - 2026-11-01 - Finished teammates sat unnoticed because their completion replies never arrived
- [INC-0416](./INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md) - 2026-11-02 - Ten teammate threads showed state paused with complete outputs on disk and no reply message
- [INC-0573](./INC-0573-teammate-replies-stopped-reaching-the-lead-for-about-25-minu.md) - 2026-11-04 - Teammate replies stopped reaching the lead for about 25 minutes while their files landed on disk
- [INC-0630](./INC-0630-a-lead-ended-its-turn-waiting-for-a-reviewer-s-completion-me.md) - 2026-11-07 - A lead ended its turn waiting for a reviewer's completion message while the reviewer's finished files were already on disk, and nothing moved for days

## Related

[INC-0091](./INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md) [INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) [INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0379](./INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md)
