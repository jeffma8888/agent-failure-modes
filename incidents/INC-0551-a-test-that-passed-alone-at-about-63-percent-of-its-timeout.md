---
id: INC-0551
title: A test that passed alone at about 63 percent of its timeout budget timed out in a loaded whole-suite run
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: mitigated
---

# INC-0551 - A test that passed alone at about 63 percent of its timeout budget timed out in a loaded whole-suite run

**Cost:** One red in a merge run, classified as load sensitive and handed to the next full run.

## Signature - how you recognise it

A test finishes at well over half of its budget alone, then times out under load.

## What happened

A test passed 8 of 8 alone in 3172 ms against a 5000 ms budget, which is about 63 percent, yet it timed out at 5000 ms in the merge run of the whole suite under host load. It has no baseline on the main branch. The lead ruled that the branch may merge, the next full run decides, and if it times out the author raises that one budget with the measured duration recorded, never an assertion.

## Root cause

The budget leaves too little margin for a loaded host.

## Why it was hard to see

Alone the test passes, so the failure seems random.

## Fix

Raise the budget, with the measured duration recorded, and never change the assertion.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that needs over half its timeout budget alone will time out under load; raise the budget with the measured duration recorded, and do not touch the assertion.

## Related

[INC-0550](./INC-0550-integration-files-that-need-a-live-server-failed-with-connec.md)
