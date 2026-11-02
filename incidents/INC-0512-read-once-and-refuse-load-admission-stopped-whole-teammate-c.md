---
id: INC-0512
title: Read-once-and-refuse load admission stopped whole teammate cycles while load spiked and fell within a minute
date: 2026-11-02
classes: [stage-timeout]
severity: medium
status: mitigated
---

# INC-0512 - Read-once-and-refuse load admission stopped whole teammate cycles while load spiked and fell within a minute

**Cost:** Whole teammate cycles ended on a single refusal while the host load was back under the limit within a minute.

## Signature - how you recognise it

A launch is refused on one load reading, and the next reading a minute later would have admitted it.

## What happened

A once-at-launch load reading refused scoped runs, and each refusal ended the teammate whole cycle, although load spiked and fell within a minute. A helper now waits up to fifteen minutes until the load is under the class limit, prints the admitting reading and exits with a distinct code on timeout. The limits per class are unchanged, and the printed line is the admission evidence.

## Root cause

Admission was a single sample of a signal that varies faster than the cycle it gates.

## Why it was hard to see

A refusal looks like a correct safety stop, and the cost shows up only as an idle teammate.

## Fix

Admit by waiting for the gate with a bounded timeout and a printed admitting reading, not by one reading at launch.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When load is spiky, admit by waiting for the gate with a bounded timeout and a printed admitting reading, not by one reading at launch.

## Related

[INC-0500](./INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md) [INC-0465](./INC-0465-an-admission-sent-at-a-low-load-reading-reached-the-runner-a.md)
