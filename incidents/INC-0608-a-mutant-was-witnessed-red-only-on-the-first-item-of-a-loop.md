---
id: INC-0608
title: A mutant was witnessed red only on the first item of a loop, so the second row was not witnessed under the mutant
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0608 - A mutant was witnessed red only on the first item of a loop, so the second row was not witnessed under the mutant

**Cost:** None. The limit was disclosed and accepted, but the second row had no mutant evidence.

## Signature - how you recognise it

A loop assertion goes red at its first item, so later items never run under the mutant.

## What happened

The mutant was red as a single assertion at the first loop item, a seeded row. The second item, a freshly created row, was not exercised under the mutant, because the first failure ended the case. The row would show its other text under the mutant, which the same assertion would also reject, but that is by design and was not witnessed. The author disclosed the limit and the reviewer accepted it as disclosed.

## Root cause

One assertion in a loop stops at its first failure, so a mutant that breaks every item shows only the first.

## Why it was hard to see

A red mutant looks like full coverage of the loop.

## Fix

Disclose which loop items the mutant witnessed, or add a mutant or per-item case that reaches each item.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a mutant turns a looped assertion red, state which items were witnessed; items after the first failure are not witnessed unless each has its own case.

## Related

[INC-0588](./INC-0588-a-reviewer-s-original-race-script-could-not-run-unmodified-a.md)
