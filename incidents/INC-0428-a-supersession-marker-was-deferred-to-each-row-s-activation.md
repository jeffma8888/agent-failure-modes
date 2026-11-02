---
id: INC-0428
title: A supersession marker was deferred to each row's activation because writing it now would trip the freeze test
date: 2026-11-02
classes: [verdict-token]
severity: low
status: fixed
---

# INC-0428 - A supersession marker was deferred to each row's activation because writing it now would trip the freeze test

**Cost:** No STOP was raised; the marker waits for its activation step.

## Signature - how you recognise it

A control write was due while a freeze condition forbade control changes.

## What happened

the supersession chains for the locator successors were not written now but at each row's activation map, because under the standing narrow admission any marker or registry change on main before the diagnostic launch is a new STOP; the reviewer's approval that the markers will cite is already on disk

## Root cause

the marker is needed later but an admission forbids any such change now

## Why it was hard to see

Writing the marker looked like routine bookkeeping.

## Fix

defer a marker that would trip an active freeze test to the step that needs it, and name the approval it will cite

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Defer a marker or registry change that would trip an active freeze test to the activation step, and name the approval it will cite

## Related

[INC-0279](./INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md) [INC-0419](./INC-0419-a-registry-edit-failed-its-own-sorted-order-assertion-and-th.md) [INC-0443](./INC-0443-a-self-imposed-freeze-outlived-its-reason-and-was-blocking-t.md)
