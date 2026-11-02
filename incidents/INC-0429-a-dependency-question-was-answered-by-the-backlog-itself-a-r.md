---
id: INC-0429
title: A dependency question was answered by the backlog itself, a relation owned by a later row, so no wait was needed
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0429 - A dependency question was answered by the backlog itself, a relation owned by a later row, so no wait was needed

**Cost:** No work was blocked; a wait that was not needed was avoided.

## Signature - how you recognise it

A spec raised a wait on something a later row was already scheduled to add.

## What happened

a spec asked whether to wait for a relation to sponsorship data, and the lead answered from the backlog: a later row adds that relation, so this row ships without it and no stub collection is created; it is not a deviation from the cut

## Root cause

the spec did not check which row owns the relation

## Why it was hard to see

The relation looked like a missing prerequisite.

## Fix

before raising a WAIT on a dependency, read the backlog for the row that owns it; if a later row owns it, ship without it and add no stub

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before waiting on a dependency, read the backlog for the row that owns it; if a later row owns it, ship without it and add no stub

## Related

[INC-0115](./INC-0115-rows-that-point-at-a-relationship-target-were-ordered-before.md) [INC-0424](./INC-0424-a-captions-upload-relation-in-a-spec-would-have-added-a-medi.md)
