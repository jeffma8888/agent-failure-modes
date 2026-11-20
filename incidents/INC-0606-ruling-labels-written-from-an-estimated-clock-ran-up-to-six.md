---
id: INC-0606
title: Ruling labels written from an estimated clock ran up to six minutes ahead of the real clock
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
topic: observability/clock-labels-without-clock-evidence
occurrences: 1
recurrence_of: INC-0274
---

# INC-0606 - Ruling labels written from an estimated clock ran up to six minutes ahead of the real clock

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

> **Recurrence of [INC-0274](./INC-0274-write-times-from-a-command-output-not-from-memory.md).** This record repeats an earlier failure and is kept for history; INC-0274 is the canonical record (10 occurrences in total) and carries the rule to apply.

**Cost:** Time labels on three rulings and several briefs were wrong, and the true start of a full run had to be rebuilt from its step records.

## Signature - how you recognise it

A time label disagrees with the step records of the run it describes.

## What happened

The lead wrote time labels without reading the clock from one ruling onward. Three rulings and the briefs that followed ran ahead of the real clock by up to about six minutes, which showed when the run's own step file gave a later start than the labels implied. The date command read a time several minutes behind the last label. The run directory, task id and every commit were right; only the labels were wrong, and a correction ruling restated the real start time from the step records.

## Root cause

Each label was extended from the last one by estimate instead of read from the clock.

## Why it was hard to see

Estimated times drift by small steps that each look plausible, and nothing checks them until a record with a real timestamp is compared.

## Fix

Read the date before writing every time label, and correct earlier labels from timestamped records.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock with date before every time label; never extend a time by estimate, and correct wrong labels from timestamped records.

## Related

[INC-0590](./INC-0590-a-full-acceptance-run-stopped-at-a-step-hang-limit-with-ever.md)
