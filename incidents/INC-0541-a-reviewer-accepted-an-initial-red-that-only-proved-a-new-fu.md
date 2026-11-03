---
id: INC-0541
title: A reviewer accepted an initial red that only proved a new function was missing, and said so
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0541 - A reviewer accepted an initial red that only proved a new function was missing, and said so

**Cost:** None. The limit was disclosed, so the red was not counted as behavioral evidence.

## Signature - how you recognise it

A test-first red fails on an assertion that the new function exists.

## What happened

Five new cases each failed at their first line with an assertion that the new function was of function type. The reviewer read the log and noted that this proves only that the function was absent and does not show the behavioral assertions fail against the old code. The reviewer accepted it with that note, also recorded that 21 skipped tests in the log were unexplained, and treated the later fail-closed cases as green coverage, not test-first reds.

## Root cause

A missing symbol is the first failure of any new function, so it is red for any test.

## Why it was hard to see

The log shows failed tests, which reads as test-first evidence unless the failing line is read.

## Fix

State what the red proves and what it does not, and do not count it as behavioral red.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An initial red that only shows a new function is missing is not behavioral evidence; say so, and ask for a mutation or old-code run that reaches the behavioral assertions.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
