---
id: INC-0400
title: An activation instruction to delete superseded pending copies had nothing to delete because an earlier pure rename had already moved them
date: 2026-11-02
classes: [vcs-destruction]
severity: low
status: fixed
---

# INC-0400 - An activation instruction to delete superseded pending copies had nothing to delete because an earlier pure rename had already moved them

**Cost:** A delete step written from an assumed state could have failed or removed the wrong file.

## Signature - how you recognise it

An instruction assumed pending copies still existed after they had been renamed away.

## What happened

an activation instruction told the engineer to delete the superseded pending copies, but an earlier pure rename had already moved those files, so no deletion was needed

## Root cause

the instruction was written from the expected state, not from the current tree

## Why it was hard to see

A step that deletes nothing looks like a success, and a failure there looks like a real fault.

## Fix

Check that a file exists before a delete step; when a pure rename already moved it, record that no deletion was needed

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before a delete step in an activation, check the file exists; a prior pure rename leaves nothing to delete, so record that

## Related

[INC-0380](./INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md) [INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md)
