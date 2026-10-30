---
id: INC-0125
title: A marker generator listing every earlier unmarked root made a root approved later repeat an old path that a later marker already held
date: 2026-10-30
classes: [identity-and-keying, concurrency]
severity: medium
status: fixed
---

# INC-0125 - A marker generator listing every earlier unmarked root made a root approved later repeat an old path that a later marker already held

**Cost:** Minor: caught in review, an audit or an engineer check before it shipped.

## Signature - how you recognise it

Two markers name the same old path because a generator listed all earlier unmarked roots.

## What happened

A marker generator listed every earlier unmarked root, so an earlier root approved later could repeat an old path that a later marker already held. New verdicts could also land in the review folder just before reporting.

## Root cause

Uniqueness of old paths was checked per marker, not globally, and the review folder was read once.

## Why it was hard to see

Each marker is valid alone, and verdicts arrive while the audit is being written up.

## Fix

Check global old-path uniqueness before writing, and re-check the review folder for new verdicts just before reporting.

## Verification

Checked by the reviewer, engineer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check uniqueness across all markers, and re-read inputs immediately before reporting.

## Related

[INC-0079](./INC-0079-a-second-writer-reused-a-shared-registry-s-batch-name-and-it.md)
