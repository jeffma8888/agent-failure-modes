---
id: INC-0635
title: A review was assigned to a reviewer by role name, but the reviewer and the author ran the same model, so it was not an independent review
date: 2026-11-10
classes: [delegation]
severity: low
status: mitigated
topic: null
occurrences: 1
---

# INC-0635 - A review was assigned to a reviewer by role name, but the reviewer and the author ran the same model, so it was not an independent review

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md)

**Cost:** One review assignment was caught at landing time and moved to a different reviewer; no output was accepted on the same-model review.

## Signature - how you recognise it

A reviewer assigned for independence runs the same model as the author of the work under review.

## What happened

A lead assigned the review of an engineer's audit to a QA thread by role name, on the rule that a different model reviews each output. Both threads ran the same model, so the review would not have been independent. The lead noticed at landing time, moved the review to a thread on a different model, and re-listed every review by the model of each thread.

## Root cause

The reviewer was chosen by role name, and the model of each thread was not compared with the author's model.

## Why it was hard to see

Role names suggest separate parties, and the model of a thread is not visible in its name or in the assignment.

## Fix

Re-list each review by the model of the author thread and the model of the reviewer thread, and move any review whose models match.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Choose each reviewer by the model of its thread, checked against the author's thread, not by role name.

## Related

[INC-0630](./INC-0630-a-lead-ended-its-turn-waiting-for-a-reviewer-s-completion-me.md) [INC-0589](./INC-0589-the-only-copies-of-eight-reviewed-drafts-sat-untracked-in-on.md)
