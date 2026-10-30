---
id: INC-0126
title: Test discovery was compared with an absolute scratch prefix that matched by accident, and guard omission mutants were not each killed
date: 2026-10-30
classes: [test-isolation, detector-fail-open]
severity: medium
status: fixed
---

# INC-0126 - Test discovery was compared with an absolute scratch prefix that matched by accident, and guard omission mutants were not each killed

**Cost:** Minor: caught in review, an audit or an engineer check before it shipped.

## Signature - how you recognise it

A discovery comparison passes because an absolute prefix coincidentally lines up.

## What happened

Test discovery was compared using absolute paths, and an absolute scratch prefix matched by accident. Omission mutants of a guard were not each required to be killed independently.

## Root cause

Paths were not normalized to relative filenames, and mutants were counted together.

## Why it was hard to see

The comparison passes, and a surviving mutant is masked by another one.

## Fix

Compare discovery using relative filenames, kill each omission mutant independently, and keep the unset control.

## Verification

Checked by the reviewer, engineer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compare relative names and kill every mutant on its own.

## Related

[INC-0116](./INC-0116-two-validators-enforcing-the-same-rule-masked-single-file-mu.md) [INC-0113](./INC-0113-a-rule-set-widened-by-tag-survived-dropping-one-tag-because.md)
