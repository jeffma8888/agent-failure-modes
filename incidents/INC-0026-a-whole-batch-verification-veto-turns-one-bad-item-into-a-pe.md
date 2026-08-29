---
id: INC-0026
title: A whole-batch verification veto turns one bad item into a permanent block
date: 2026-08-28
classes: [spec-and-scope, observability, false-green]
severity: high
status: fixed
---

# INC-0026 - A whole-batch verification veto turns one bad item into a permanent block

**Cost:** Twelve days with zero promotions. The refusal streak grew from 13 to 113 consecutive holds while the input queue grew from 104 to 991 candidates; a launcher kept adding work every two hours to a pool that could no longer pass.

## Signature - how you recognise it

A gate that used to pass now refuses on every cycle, and it names a DIFFERENT offending item each time. The queue grows monotonically. Each individual refusal is correct and well-reported.

## What happened

An unattended research pipeline verified the evidence quotes of its ENTIRE inbox before promoting anything, and the calling driver returned before the promoter whenever the verifier exited non-zero. One unverifiable quote anywhere in the pool therefore vetoed all 991 candidates. With a launcher adding candidates on a timer and a non-zero per-item failure rate, the probability that the pool contained at least one bad item approached 1 and stayed there.

## Root cause

The verdict's SCOPE was the batch while the decision it gated was per record, and the exit code was all-or-nothing. That makes the gate a ratchet rather than a filter: every added item can only ever increase the chance of a total block, so the system's throughput trends to zero while every component behaves exactly as designed.

## Why it was hard to see

Nothing is broken. Every refusal is individually correct, the escalation reports are accurate, and the component tests are green - so the obvious remedy is to fix the named item. That remedy is measurably wrong: a shipped fix for the exact defect diagnosed the previous day changed nothing at the system level, because a different item took its place and the streak grew by twelve on the same day.

## Fix

Three parts. (1) Make the verdict PER RECORD and act on it: keep the verified, quarantine one whose evidence is genuinely absent, and DEFER one whose source could not be fetched - unreachable is not a verdict. (2) Return SUCCESS even when quarantining, because a non-zero exit is exactly what lets a caller rebuild the batch veto. (3) Bound the producer: pause new work while the backlog exceeds a threshold, so a stalled consumer cannot be buried.

## Verification

The first partitioned pass promoted 24 records and grew the register from 16 to 40 with a green suite. It also exposed a second defect the veto had been hiding: the comparison itself was falsely accusing honest quotes, because every HTML tag became a space, so re-checking the 40 unique historical accusations found 19 false and 21 genuinely absent. Both records the first partitioned pass quarantined were re-checked by hand, both were false, and both were restored to the queue.

## Transferable rule

> A gate whose verdict covers the whole batch, and whose caller aborts on any failure, turns one bad item into a permanent block as soon as the queue keeps growing - a ratchet, not a filter. Judge each item on its own evidence, act per item, and never let the gate's exit code re-create the batch veto.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - commit af2db9a makes quote verification per record so one bad quote cannot veto the pool; a747cc8 adds the verified-staging directory so bounding a pass stays honest; tools/verify_quotes.py documents why --partition exists in its own module docstring.

## Related

[INC-0004](./INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md) [INC-0025](./INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md)
