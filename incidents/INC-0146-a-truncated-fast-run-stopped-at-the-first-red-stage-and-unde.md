---
id: INC-0146
title: A truncated FAST run stopped at the first red stage and understated the stage sum by about half
date: 2026-10-30
classes: [observability, false-green]
severity: medium
status: fixed
---

# INC-0146 - A truncated FAST run stopped at the first red stage and understated the stage sum by about half

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A timing taken from a run that stopped early is used as a full measurement.

## What happened

A FAST run that stopped at the first red stage understated the stage sum by about half, and was sold as a green preship measurement.

## Root cause

Time up to a failure was read as total time.

## Why it was hard to see

The numbers look like a normal run.

## Fix

Do not present time to a known red as a complete green measurement.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure the complete run before claiming a budget.

## Related

[INC-0131](./INC-0131-a-stage-hang-deadline-copied-from-a-planning-estimate-killed.md)
