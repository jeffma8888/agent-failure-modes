---
id: INC-0619
title: A clock label slip recurred a fifth time, and the clock call became the only call in its batch
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0619 - A clock label slip recurred a fifth time, and the clock call became the only call in its batch

**Cost:** One ruling was first labelled with a clock value that was never read and had to be corrected.

## Signature - how you recognise it

A quoted clock value matches no clock read.

## What happened

A ruling was first written as 05:06, quoting a clock read that never happened; the real read was 05:05:12. The clock call and the write had again been issued in the same parallel batch. The earlier fix, to run the clock alone and read it before writing, was a rule and did not change how the calls were issued. The lead now issues the clock call as the only call in its batch.

## Root cause

The fix was stated as a rule to remember, not as a change to how the batch is built.

## Why it was hard to see

After four recurrences the rule was known, and the slip still happened under pressure to move fast.

## Fix

Issue the clock call as the only call in its batch, and write the label in the next call.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Make the process impossible to get wrong: issue the clock call as the only call in its batch, and write the label only in a later call.

## Related

[INC-0617](./INC-0617-a-ruling-quoted-a-clock-value-that-was-never-read-because-th.md) [INC-0613](./INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md)
