---
id: INC-0457
title: A ruling wrote a media directory binding from memory that contradicted the pinned scripts, and the runner stopped instead of substituting
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0457 - A ruling wrote a media directory binding from memory that contradicted the pinned scripts, and the runner stopped instead of substituting

**Cost:** A short delay: the runner stopped and waited for a correction.

## Signature - how you recognise it

A written binding contradicted the scripts it was meant to drive.

## What happened

a ruling wrote the media directory binding from memory and it contradicted the pinned helper and walker scripts and the earlier ruling for that step; the runner stopped rather than substitute, and the next ruling corrected the binding to the media folder under the walk root exactly, with no symlink, while the other overrides stood; the lead said the runner was right to stop

## Root cause

the binding was written from memory

## Why it was hard to see

The ruling read as plausible, and only a check against the pinned bytes shows the difference.

## Fix

check a binding against the pinned bytes before writing it into a ruling

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check a binding against the pinned scripts before writing it, and stop on a contradiction rather than substitute

## Related

[INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) [INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0433](./INC-0433-a-job-text-swapped-two-commit-identities-and-reading-the-log.md)
