---
id: INC-0416
title: Ten teammate threads showed state paused with complete outputs on disk and no reply message
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0416 - Ten teammate threads showed state paused with complete outputs on disk and no reply message

**Cost:** No work was lost; waiting on replies would have stalled ten reviews.

## Signature - how you recognise it

A thread showed paused and sent no reply while its output file was complete.

## What happened

ten teammate threads showed state paused with complete outputs on disk and no reply message; the lead graded each output from the file, never from a missing reply

## Root cause

the thread state and the reply channel do not reliably report that the work is finished

## Why it was hard to see

A paused state looks like unfinished work.

## Fix

treat a paused thread with no reply as unknown, open the output file, and grade the file

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Grade a teammate output from the file on disk; a missing reply or a paused state is not a verdict

## Related

[INC-0091](./INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md) [INC-0317](./INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md) [INC-0449](./INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md) [INC-0451](./INC-0451-the-lead-missed-eight-teammate-replies-with-no-compaction-an.md)
