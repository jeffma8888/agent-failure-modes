---
id: INC-0274
title: Write times from a command output, not from memory
date: 2026-11-01
classes: [observability, spec-and-scope]
severity: medium
status: fixed
topic: observability/clock-labels-without-clock-evidence
occurrences: 10
---

# INC-0274 - Write times from a command output, not from memory

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An evidence line recorded a time that was not read from a clock.

## What happened

an evidence line first carried a clock time written before the clock was checked; the lead corrected it

## Root cause

an evidence line first carried a clock time written before the clock was checked; the lead corrected it

## Why it was hard to see

A remembered time feels certain.

## Fix

Write times from a command output, not from memory

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write a recorded time from a command output, never from memory

## Recurrences

Occurrences: 10. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) - 2026-11-01 - Time stamps written from an estimate ran ahead of the clock
- [INC-0373](./INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) - 2026-11-01 - Two replies were stamped with times ahead of the clock
- [INC-0383](./INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) - 2026-11-01 - A ruling was stamped four minutes ahead of the clock because the time was written before the clock was read
- [INC-0384](./INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md) - 2026-11-01 - The lead stamped a brief four minutes ahead of the clock again, one round after the same correction
- [INC-0415](./INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md) - 2026-11-02 - A ruling timestamp was written from an estimate and corrected minutes later, twice in one round
- [INC-0442](./INC-0442-the-lead-wrote-a-ruling-timestamp-before-reading-the-clock.md) - 2026-11-02 - The lead wrote a ruling timestamp before reading the clock
- [INC-0456](./INC-0456-the-lead-wrote-ruling-timestamps-from-memory-three-times-and.md) - 2026-11-02 - The lead wrote ruling timestamps from memory three times and had to correct them
- [INC-0567](./INC-0567-heading-times-in-several-rulings-and-briefs-ran-thirty-to-se.md) - 2026-11-04 - Heading times in several rulings and briefs ran thirty to seventy minutes ahead of the real clock
- [INC-0606](./INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md) - 2026-11-04 - Ruling labels written from an estimated clock ran up to six minutes ahead of the real clock

## Related

[INC-0259](./INC-0259-sum-every-runner-the-earlier-record-summed.md)
