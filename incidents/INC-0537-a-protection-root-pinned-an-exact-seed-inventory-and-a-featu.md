---
id: INC-0537
title: A protection root pinned an exact seed inventory, and a feature row that grew the seed turned it red
date: 2026-11-02
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0537 - A protection root pinned an exact seed inventory, and a feature row that grew the seed turned it red

**Cost:** No loss. The red was correct and was routed to a successor root instead of a test edit.

## Signature - how you recognise it

An active root asserts an exact count of seeded records, and a feature branch adds more records.

## What happened

An active root pinned exactly 15 media records of one role. A feature row added 11 more seeded covers of another role, so the root went red on that branch. The red was right-reason, because the inventory had grown. The ruling was not to let the implementer edit the test. The author of the root writes a successor that derives the expected set from the source declarations, fails closed if either declaration changes shape, keeps per-role checks and the same idempotence cases, and activates only on the feature branch with a separate reviewer.

## Root cause

A hard-coded inventory duplicates what the seed declarations already say, so any legitimate growth breaks it.

## Why it was hard to see

Editing the test to match the code would silently weaken the guard, and leaving it red blocks the feature.

## Fix

Derive the expected inventory from the source declarations, and route the change through a reviewed successor root.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A root that pins an exact inventory should derive it from the source declarations and fail closed on a shape change; a right-reason red from legitimate growth is fixed by a reviewed successor, never by the implementer editing the test.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
