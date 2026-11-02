---
id: INC-0484
title: A test fixture was refused by an earlier check than the one the case was written to prove
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0484 - A test fixture was refused by an earlier check than the one the case was written to prove

**Cost:** Minor: a red full run; the check under test stayed unverified until the case was repaired.

## Signature - how you recognise it

The case failed on the wrong guard, so the intended guard never ran.

## What happened

A test meant to assert that a wrong-role relation is refused used an image smaller than the role's minimum size. The size check refused the fixture create first, before the relation check was ever tried, so the case failed for the wrong reason and the guard under test was never exercised.

## Root cause

The fixture violated an earlier guard than the one under test, so that guard's refusal masked the intended one.

## Why it was hard to see

A refusal looks like the expected refusal, so the case reads as aimed at the right check until the failing reason is read.

## Fix

Build the fixture so it passes every guard except the one under test, assert which guard refused (by message or field path), and prove the case reaches its guard with one product mutation that turns it red for the right reason.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Build a fixture that passes every guard except the one under test, and assert which guard refused; an earlier guard's refusal masks the guard the case is meant to prove.

## Related

[INC-0477](./INC-0477-a-browser-test-failed-at-its-first-request-and-after-that-wa.md) [INC-0222](./INC-0222-a-clean-tree-positive-did-not-exercise-the-working-file-cont.md) [INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md)
