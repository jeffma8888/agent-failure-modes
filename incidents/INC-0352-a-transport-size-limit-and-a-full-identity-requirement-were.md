---
id: INC-0352
title: A transport size limit and a full-identity requirement were specified for the same record with no framing
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0352 - A transport size limit and a full-identity requirement were specified for the same record with no framing

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A timing spec required every record to fit 512 bytes and to carry full file and case identity, and a long path could not satisfy both.

## What happened

a timing spec required every record to fit 512 bytes (the portable atomic pipe write) and also to carry full file and case identity; a long path or case title cannot satisfy both, and the spec gave no representation for an oversized record, so the engineer could only truncate, hash or drop

## Root cause

two requirements in the spec could not both hold for long identities, and the spec did not say how an oversized record is represented

## Why it was hard to see

A single record that is short enough for the transport looks complete, and the conflict appears only with a long path or a non-ASCII title.

## Fix

Keep the logical record, add a versioned transport frame (emitter PID, sequence, index, total, encoded chunk) so each physical line fits the budget, and reconstruct before counting

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a transport limit and a completeness requirement meet, specify the framing and reconstruction, and test with long and non-ASCII identities

## Related

[INC-0071](./INC-0071-a-plan-claimed-minutes-denominated-stage-times-fit-inside-a.md) [INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md) [INC-0353](./INC-0353-an-authorization-point-was-placed-after-the-first-event-that.md)
