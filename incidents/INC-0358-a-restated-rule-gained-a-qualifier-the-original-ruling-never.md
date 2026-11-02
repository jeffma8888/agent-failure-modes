---
id: INC-0358
title: A restated rule gained a qualifier the original ruling never had
date: 2026-11-01
classes: [observability, spec-and-scope]
severity: medium
status: fixed
---

# INC-0358 - A restated rule gained a qualifier the original ruling never had

**Cost:** Minor: caught in review before it shipped.

## Signature - how you recognise it

A ruling said to report every sample over a limit at once, but the spec that restated it said to report only eligible samples.

## What happened

a ruling required that any sample over a time limit be reported to the lead at once. A spec author restated it in a precondition document and in a companion spec as "an eligible sample over the limit". A sample made ineligible by load or transport loss could still exceed the limit, and under the restated text it would be kept for later instead of reported. An earlier review had already asked that the rule not be narrowed to eligible attempts

## Root cause

the restatement borrowed a qualifier from a different purpose (which samples count toward calibration) and applied it to an alarm, and the same wording was copied into a sibling document

## Why it was hard to see

Eligibility was a familiar word in the surrounding text, so the narrowed sentence read as natural, and the summaries elsewhere in the document stayed unqualified, which hid the conflict.

## Fix

A reviewer supplied the exact replacement sentence (report every such sample, whether eligible or ineligible) for both documents; eligibility stays a calibration notion and no longer limits the alarm

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a ruling is restated in a spec, copy its population word for word; a qualifier borrowed from another purpose narrows an alarm, so diff every restated condition against the ruling's own words and fix each sibling copy

## Related

[INC-0302](./INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md) [INC-0346](./INC-0346-a-ruling-sent-in-a-message-was-never-written-to-the-ruling-l.md) [INC-0334](./INC-0334-a-bare-number-beside-a-time-threshold-invited-a-unit-misread.md)
