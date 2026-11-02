---
id: INC-0317
title: Finished teammates sat unnoticed because their completion replies never arrived
date: 2026-11-01
classes: [delegation, observability]
severity: medium
status: fixed
---

# INC-0317 - Finished teammates sat unnoticed because their completion replies never arrived

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Work was complete on disk while the coordinator was still waiting for a message.

## What happened

several delegated workers finished, but their completion replies never reached the coordinator, which noticed only minutes later when it checked the activity list and found the output files finished

## Root cause

several delegated workers finished, but their completion replies never reached the coordinator, which noticed only minutes later when it checked the activity list and found the output files finished

## Why it was hard to see

Waiting for a reply looks like patience, and nothing signals that the reply was lost.

## Fix

When an output file stops changing and no reply came, check the run status and land from disk

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never wait on a reply alone: when an output file stops changing and no reply came, check the run status and land from disk

## Related

[INC-0041](./INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) [INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md) [INC-0128](./INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md)
