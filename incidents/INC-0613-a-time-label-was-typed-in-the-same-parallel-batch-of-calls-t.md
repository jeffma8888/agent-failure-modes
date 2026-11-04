---
id: INC-0613
title: A time label was typed in the same parallel batch of calls that read the clock, so it was written before the clock was seen; the third recurrence
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0613 - A time label was typed in the same parallel batch of calls that read the clock, so it was written before the clock was seen; the third recurrence

**Cost:** One ruling carried a label that had to be corrected in place with a note.

## Signature - how you recognise it

A time label is written in a call issued alongside the clock read, and the two disagree.

## What happened

The lead issued the clock read and the write of the ruling label in the same parallel batch of tool calls, so the label was typed before the clock output was seen. The label was corrected in place with a note. This is the third recurrence: an estimated clock ran up to six minutes fast, then a label was written in the same script that read the clock afterwards, and now a label sat in a batch alongside the clock read.

## Root cause

The two earlier fixes put the clock read first in intent but not in order: the read and the write still ran together.

## Why it was hard to see

Parallel calls look like one step, and a rule about reading first is satisfied in words while the order is not enforced.

## Fix

Make the clock its own call, and copy its output into the label only after it has been seen.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock in its own call and see its output before any label is typed; never issue the read and the label write together.

## Related

[INC-0606](./INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md) [INC-0611](./INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md)
