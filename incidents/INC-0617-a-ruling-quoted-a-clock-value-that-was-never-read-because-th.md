---
id: INC-0617
title: A ruling quoted a clock value that was never read, because the write ran in the same parallel batch as the clock call; the fourth recurrence
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0617 - A ruling quoted a clock value that was never read, because the write ran in the same parallel batch as the clock call; the fourth recurrence

**Cost:** One ruling carried a clock value 13 seconds ahead of the real read and was corrected with a note; the heading kept its time because a teammate was already pointed at it.

## Signature - how you recognise it

A quoted clock value matches no actual clock read.

## What happened

The lead typed a clock value in the same parallel batch as the clock call, quoting a reading of 04:40:08 that never happened. The real read was 04:39:55. A correction note was added. This is the fourth recurrence of the same class, after estimated labels, a label in the same script as the read, and a label in the same batch as the read.

## Root cause

The rule was stated each time, but nothing prevented issuing the write and the read together.

## Why it was hard to see

Each earlier fix named the rule without changing the order of calls, so the habit survived.

## Fix

Run the clock call alone, read its output, then write the label with that exact value.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run date alone, read the output, then write; never quote a clock value that a call in the same batch has not yet returned.

## Related

[INC-0613](./INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md) [INC-0606](./INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md) [INC-0611](./INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md)
