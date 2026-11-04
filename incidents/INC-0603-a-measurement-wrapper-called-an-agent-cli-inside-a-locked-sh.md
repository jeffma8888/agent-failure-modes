---
id: INC-0603
title: A measurement wrapper called an agent CLI inside a locked shell and failed before any child ran, and the one-invocation bound was kept by voiding the attempt
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0603 - A measurement wrapper called an agent CLI inside a locked shell and failed before any child ran, and the one-invocation bound was kept by voiding the attempt

**Cost:** One heavy-run invocation spent on a wrapper defect, with no measurement from it.

## Signature - how you recognise it

A bounded run exits before any child process starts.

## What happened

A measurement was bounded to one heavy-run invocation. The wrapper called an agent CLI from inside a locked shell and failed before any child ran. The attempt was voided openly and one corrected invocation was made, instead of a silent retry. The corrected run measured and then ran a control, both 29 of 29, exit 0.

## Root cause

The wrapper used a command that does not work inside the locked shell, and it was not tried before the bounded run.

## Why it was hard to see

A failure before any child ran produced no result, and a quiet retry would have hidden that the bound was exceeded.

## Fix

Void the failed attempt openly with its cause, correct the wrapper, and make the one corrected invocation.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a bounded run fails before any child runs, void it openly as a wrapper defect and report the corrected invocation; do not retry silently.

## Related

[INC-0588](./INC-0588-a-reviewer-s-original-race-script-could-not-run-unmodified-a.md)
