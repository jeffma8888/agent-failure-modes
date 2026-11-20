---
id: INC-0384
title: The lead stamped a brief four minutes ahead of the clock again, one round after the same correction
date: 2026-11-01
classes: [observability]
severity: low
status: fixed
topic: observability/clock-labels-without-clock-evidence
occurrences: 1
recurrence_of: INC-0274
---

# INC-0384 - The lead stamped a brief four minutes ahead of the clock again, one round after the same correction

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

> **Recurrence of [INC-0274](./INC-0274-write-times-from-a-command-output-not-from-memory.md).** This record repeats an earlier failure and is kept for history; INC-0274 is the canonical record (10 occurrences in total) and carries the rule to apply.

**Cost:** A brief carried a time later than the real one, a second time in two rounds.

## Signature - how you recognise it

A brief carried a time stamp later than the moment it was written, after a rule against it was already recorded.

## What happened

the lead stamped a brief four minutes ahead of the clock again, one round after the same failure was recorded; a repeated failure needs a mechanism, so the brief generator now writes the time from the clock

## Root cause

the rule relied on the author remembering to read the clock; nothing enforced it

## Why it was hard to see

A written rule felt sufficient, and the stamp still looked plausible.

## Fix

Make the brief generator write the time from the clock instead of relying on the author to read it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A failure that repeats after a written rule needs a mechanism: generate the time from the clock, never type it

## Related

[INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) [INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) [INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) [INC-0415](./INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md)
