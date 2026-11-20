---
id: INC-0611
title: A time label was written in the same script that read the clock afterwards, minutes after a rule to read the clock first was recorded
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
topic: observability/clock-labels-without-clock-evidence
occurrences: 4
---

# INC-0611 - A time label was written in the same script that read the clock afterwards, minutes after a rule to read the clock first was recorded

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Timestamp labels disagree with the actual clock](../catalog/observability/clock-labels-without-clock-evidence.md)

**Cost:** One ruling carried a label a minute ahead of the real time until it was corrected in place with a note.

## Signature - how you recognise it

A time label is later than the clock read in the same script.

## What happened

The lead labelled a ruling with a time inside a script that read the clock only afterwards, minutes after the rule to read the clock before every label was recorded. The real time was one minute earlier. The label was corrected in place with a note that the first label was written before the clock was read.

## Root cause

The rule existed but the clock read and the label were in one call, so the label was typed first.

## Why it was hard to see

A rule that exists is not a check; nothing forced the order.

## Fix

Read the clock in its own call and copy that value into the label.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the clock in its own call and copy that value into the label; a rule that exists is not a check.

## Recurrences

Occurrences: 4. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0613](./INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md) - 2026-11-04 - A time label was typed in the same parallel batch of calls that read the clock, so it was written before the clock was seen; the third recurrence
- [INC-0617](./INC-0617-a-ruling-quoted-a-clock-value-that-was-never-read-because-th.md) - 2026-11-04 - A ruling quoted a clock value that was never read, because the write ran in the same parallel batch as the clock call; the fourth recurrence
- [INC-0619](./INC-0619-a-clock-label-slip-recurred-a-fifth-time-and-the-clock-call.md) - 2026-11-04 - A clock label slip recurred a fifth time, and the clock call became the only call in its batch

## Related

[INC-0606](./INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md)
