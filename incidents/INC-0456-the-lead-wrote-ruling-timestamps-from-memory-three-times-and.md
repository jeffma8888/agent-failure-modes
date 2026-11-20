---
id: INC-0456
title: The lead wrote ruling timestamps from memory three times and had to correct them
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
topic: observability/clock-labels-without-clock-evidence
occurrences: 1
recurrence_of: INC-0274
---

# INC-0456 - The lead wrote ruling timestamps from memory three times and had to correct them

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

> **Recurrence of [INC-0274](./INC-0274-write-times-from-a-command-output-not-from-memory.md).** This record repeats an earlier failure and is kept for history; INC-0274 is the canonical record (10 occurrences in total) and carries the rule to apply.

**Cost:** Minor: three corrections.

## Signature - how you recognise it

Timestamps in rulings were wrong until corrected.

## What happened

the lead wrote ruling timestamps from memory three times and corrected each one afterwards

## Root cause

times were typed from estimates

## Why it was hard to see

Estimated times feel right and drift in fast work.

## Fix

compute the timestamp from the clock in the same command that writes it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compute a timestamp from the clock in the same command that writes it, never from memory

## Related

[INC-0415](./INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md) [INC-0442](./INC-0442-the-lead-wrote-a-ruling-timestamp-before-reading-the-clock.md) [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md)
