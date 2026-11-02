---
id: INC-0467
title: A run plan barred the test author from running the script, and a later message assigned that author anyway
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0467 - A run plan barred the test author from running the script, and a later message assigned that author anyway

**Cost:** None: caught before the run.

## Signature - how you recognise it

A message contradicted the plan it was meant to follow.

## What happened

a run plan barred the author of the tests from running the walk, and a later lead message assigned that author to run it anyway; the author of the walker script caught the conflict before the run; the independence rule stood, and a runner who authored neither code nor tests was named

## Root cause

the assignment was written without reading the independence rule in the plan

## Why it was hard to see

A later message looks newer than the plan, so it seems to win.

## Fix

name the runner as someone who wrote neither the code nor the tests, and have the lead check each assignment against the independence rules of the plan before sending it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check an assignment against the independence rules of the plan before sending it

## Related

[INC-0337](./INC-0337-reviewers-named-at-ruling-time-were-busy-when-the-artifact-l.md) [INC-0399](./INC-0399-a-final-review-was-reassigned-from-a-busy-reviewer-to-an-idl.md) [INC-0423](./INC-0423-a-review-was-reassigned-off-the-critical-path-so-the-reviewe.md)
