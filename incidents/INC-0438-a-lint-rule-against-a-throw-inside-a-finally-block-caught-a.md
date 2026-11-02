---
id: INC-0438
title: A lint rule against a throw inside a finally block caught a real defect in production code
date: 2026-11-02
classes: [detector-fail-closed]
severity: low
status: fixed
---

# INC-0438 - A lint rule against a throw inside a finally block caught a real defect in production code

**Cost:** The defects were fixed before the merge.

## Signature - how you recognise it

A final lint gate failed on code that looked finished.

## What happened

the final lint gate exited non-zero on two errors in a request-size helper, a dead assignment and a throw inside a finally block; the lead ruled both real production defects, fixed in one commit with the intended behaviors each pinned by a unit case and no disable comment or rule change

## Root cause

a release failure was handled by throwing inside a finally block, which can replace the original outcome

## Why it was hard to see

The code passed its tests; only the static rule saw the control-flow hazard.

## Fix

treat a lint error as a defect until a reviewer shows otherwise, restructure the code, pin each intended behavior with a case, and add no disable comment

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Treat a lint error as a defect: restructure, pin each intended behavior with a unit case, and add no disable comment or rule change

## Related

[INC-0199](./INC-0199-an-inline-directive-could-bypass-a-lint-rule-on-a-protected.md) [INC-0378](./INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md)
