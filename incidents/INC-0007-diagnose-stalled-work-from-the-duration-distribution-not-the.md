---
id: INC-0007
title: Diagnose stalled work from the duration distribution, not the outcome
date: 2026-08-04
classes: [observability, stage-timeout]
severity: medium
status: fixed
---

# INC-0007 - Diagnose stalled work from the duration distribution, not the outcome

**Cost:** A plausible-but-untested fix was shipped and failed. The correct diagnosis was in the log the whole time - it just needed to be tallied.

## Signature - how you recognise it

The loop's per-step success rate looks healthy. But if you compute the median wall-clock per step, one specific step sits AT the hard cap.

## What happened

A stalled team had been miscategorized as 'sometimes green, sometimes red'. Pairing every 'attempt started' line in the dispatcher log with its 'produced / no output file' line showed the step's MEDIAN was 600 seconds - the hard cap - across every recorded sample. Its successes were killed at 600s too and merely happened to have written their output first.

## Root cause

An outcome-only view of a step that runs under a hard timeout is blind to whether the step is chronically over budget. Once you measure the distribution, you cannot un-see it.

## Why it was hard to see

The successes look like proof the step is fine. The raw data was in the log the whole time.

## Fix

Add a small per-step duration reporter to the dispatcher output. Include median, P90, and count-at-cap. Compare against a SIBLING running the same pipeline on the same box in the same window - which cheaply falsifies 'the machine is slow' or 'the provider is throttling'.

## Verification

The reporter surfaced two more chronically-over-budget steps within a week. Both were fixed at the root (INC-0002's write-early pattern, then INC-0003's suite-speed fix).

## Transferable rule

> A success predicate defined as 'the output file exists' hides a chronically over-budget step. Report the DURATION DISTRIBUTION per step, not just the outcome, and compare against a sibling running the same pipeline on the same box - which cheaply falsifies 'the machine is slow' or 'the provider is throttling'.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0006](./INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md)
