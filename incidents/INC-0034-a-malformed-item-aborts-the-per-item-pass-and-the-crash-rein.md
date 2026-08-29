---
id: INC-0034
title: A malformed item aborts the per-item pass, and the crash reinstates the veto wearing a traceback
date: 2026-08-28
classes: [detector-fail-closed, checkpoint]
severity: medium
status: fixed
---

# INC-0034 - A malformed item aborts the per-item pass, and the crash reinstates the veto wearing a traceback

**Cost:** No production loss - found while hardening the replacement. Had it run, a single item whose field held the wrong type would have crashed the whole per-item pass before any item was judged, restoring the exact all-or-nothing behaviour that had just cost twelve days.

## Signature - how you recognise it

The pass that was supposed to judge items one at a time dies with a type error naming one item, and nothing is promoted. The log reads as an unrelated bug rather than as a policy decision, so the outcome is never recognised as the failure you just eliminated.

## What happened

The fix for a whole-batch gate was to iterate items and route each one. The loop read fields from each item without checking their SHAPE - a list where a string was expected, a null, a missing key, an unparseable file - so one malformed item raised on attribute access and the whole pass aborted mid-iteration. Items already judged were not committed, so the effective behaviour was identical to the batch veto it replaced.

## Root cause

Per-item isolation is a property of the ERROR PATH, not of the loop. Writing a for-loop makes the WORK per item; only catching per item makes the FAILURES per item. An uncaught exception is a batch-scoped verdict no matter how granular the loop around it is.

## Why it was hard to see

The regression is invisible in review, because the diff genuinely does convert a batch pass into a per-item pass, and every test written for the new behaviour uses well-formed items. The crash also disguises itself: an aggregate refusal is recognisable as policy, whereas a traceback reads as a separate bug to fix later, so nobody connects it to the failure mode just removed.

## Fix

Validate each item's SHAPE before judging it and quarantine a malformed item with a written reason instead of raising. Wrap the per-item work in a per-item handler so an unexpected exception quarantines that item and the pass continues. Then test it directly: feed the pass a batch containing a wrong-typed field, a null, a missing key and an unparseable file, and assert the WELL-FORMED items in the SAME batch were still judged and promoted.

## Verification

25 tests cover the malformed-item paths and 22 of them fail against the unfixed code with the exact attribute error predicted. The suite asserts that a batch containing malformed items still promotes its well-formed members, which is the property the original defect violated.

## Transferable rule

> Per-item isolation lives in the error path, not the loop. A for-loop makes the WORK per item; only a per-item catch makes the FAILURES per item, and an uncaught exception is a batch-wide verdict however granular the loop. Validate each item's shape, quarantine a bad one with a reason, and test that good items in the SAME batch still get through.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - the record-shape gate added alongside the per-record partition mode in `tools/verify_quotes.py`, so a malformed candidate is quarantined instead of crashing the pass.

## Related

[INC-0006](./INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) [INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md)
