---
id: INC-0366
title: A walk checklist attached another request variant's clause to the keyless request, so a correct response read as a failure
date: 2026-11-01
classes: [detector-fail-closed, spec-and-scope]
severity: low
status: fixed
---

# INC-0366 - A walk checklist attached another request variant's clause to the keyless request, so a correct response read as a failure

**Cost:** Minor: one triage cycle; no product change was needed.

## Signature - how you recognise it

A walk reported one failure on a response that matched the delivered spec.

## What happened

the first milestone walk reported one failure. Triage against the delivered spec row showed the checklist had attached a clause meant for a different request variant (an empty-body not-found status for a wrong key) to the keyless request, which correctly returns the not-found view. The product was right and the checklist was a transcription error

## Root cause

a checklist expectation was written from memory of the spec instead of copied from the delivered spec row, and mixed two request variants

## Why it was hard to see

The failing expectation looked authoritative because it sat in the checklist, and the two variants differ by one clause.

## Fix

Triage every failure against the delivered spec row, the code and the active tests before calling it a defect; correct the checklist from the spec row and record the verdict as a checklist error

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Derive each checklist expectation verbatim from the delivered spec row and cite the row; triage every failure against the spec, the code and the active tests before calling it a defect

## Related

[INC-0265](./INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md) [INC-0244](./INC-0244-a-correct-not-found-page-was-served-with-a-200-status.md)
