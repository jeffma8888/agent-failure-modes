---
id: INC-0567
title: Heading times in several rulings and briefs ran thirty to seventy minutes ahead of the real clock
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
topic: observability/clock-labels-without-clock-evidence
occurrences: 1
recurrence_of: INC-0274
---

# INC-0567 - Heading times in several rulings and briefs ran thirty to seventy minutes ahead of the real clock

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

> **Recurrence of [INC-0274](./INC-0274-write-times-from-a-command-output-not-from-memory.md).** This record repeats an earlier failure and is kept for history; INC-0274 is the canonical record (10 occurrences in total) and carries the rule to apply.

**Cost:** Timestamps in the ledger were wrong, so the order of events could not be read from headings.

## Signature - how you recognise it

A heading time was written from memory or estimation, not read from the clock.

## What happened

The lead wrote heading times and stamps in several consecutive rulings and in six briefs that said 00:40 to 01:40, while the real times were 00:10 to 00:31. The lead issued a correction: use file and log timestamps, not those stamps.

## Root cause

The times were estimated, not read.

## Why it was hard to see

A stamp in a ruling looks authoritative.

## Fix

Take times from the date command and from file stamps, and correct the ledger by an appended note.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock immediately before writing a timestamp; when a stamp is wrong, trust file and log times and append a correction.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
