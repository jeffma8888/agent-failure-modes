---
id: INC-0432
title: Hand delivery under a hold, with one reconciliation after the load, replaced blocking on a state flip
date: 2026-11-02
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0432 - Hand delivery under a hold, with one reconciliation after the load, replaced blocking on a state flip

**Cost:** No rows were blocked; one reconciliation step was added after the load.

## Signature - how you recognise it

Three rows waited on a backlog state flip that was held on purpose.

## What happened

with the backlog state flip held until a later load, the design conditions for three rows were met, so the lead adopted hand delivery as the operating mode: implement on branches and merge by hand as for earlier rows, record the backlog state for every hand-merged row in one reconciliation after the load, regenerate the dependent patch on the real post-load base with a non-author re-review, and keep the freeze admission rules for any registry or marker change

## Root cause

the flip depends on an event that is not on the critical path

## Why it was hard to see

Waiting for the flip looked like the safe default.

## Fix

when a state flip is held, deliver by hand under the existing precedent, reconcile once after the hold lifts, and keep every freeze rule in force

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Under a held state flip, deliver by hand on the established precedent and reconcile once after the hold; keep every freeze rule

## Related

[INC-0410](./INC-0410-the-lead-re-merged-the-full-candidate-itself-rather-than-que.md) [INC-0317](./INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md)
