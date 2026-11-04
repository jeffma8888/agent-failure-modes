---
id: INC-0624
title: The clock call ran alone in its own message, yet the ruling label was typed from expectation instead of copied from the returned value; the seventh recurrence
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0624 - The clock call ran alone in its own message, yet the ruling label was typed from expectation instead of copied from the returned value; the seventh recurrence

**Cost:** One ruling carried a label 53 seconds behind the real read and was corrected with a note.

## Signature - how you recognise it

A heading time differs from the clock output returned just before it.

## What happened

The clock call ran alone in its own message, as the earlier batching fix required. The lead then typed the ruling label from expectation, 05:55:24, instead of copying the returned 05:56:17. This is the seventh recurrence of the clock-label class. The batching fix closed one path, writing in the same batch as the read, and not the transcription step.

## Root cause

The fix controlled when the clock was read, not how its value reached the label.

## Why it was hard to see

With the read isolated, the slip moved to the one step left, and nothing checked the label against the output.

## Fix

Copy the label from the returned output, never type it, and add a check that compares the heading's time with the last clock output.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Copy a time label from the returned clock output, never type it; make the check mechanical by comparing the heading's time with the last clock output.

## Related

[INC-0619](./INC-0619-a-clock-label-slip-recurred-a-fifth-time-and-the-clock-call.md) [INC-0617](./INC-0617-a-ruling-quoted-a-clock-value-that-was-never-read-because-th.md) [INC-0613](./INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md)
