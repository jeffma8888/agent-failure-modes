---
id: INC-0041
title: A verifier that lived and answered can still deliver an unusable verdict
date: 2026-09-02
classes: [observability, verdict-token, delegation]
severity: high
status: mitigated
---

# INC-0041 - A verifier that lived and answered can still deliver an unusable verdict

**Cost:** An audit's single FAIL was never identifiable. The verifier's reply was cut off before it reached the failing item, and the persisted task log truncated at the same point - so the finding was LOST rather than merely hidden, and the whole audit had to be redone by hand.

## Signature - how you recognise it

A verifier reports a COUNT of failures in its summary line but the detail for the failing item is missing, and re-reading the stored log truncates at the same place.

## What happened

An independent verifier was asked to check thirteen claims. It answered with a summary line - one FAIL found, all other claims PASS - and was cut off at claim 7. The failing claim was somewhere in 8 to 13. Re-reading the persisted task log truncated at the identical point, so no channel held the finding.

## Root cause

Two independent truncations landing at the same boundary, plus a report format that put the AGGREGATE first and the per-item evidence after it. A summary line asserting a count is not a finding: it is a claim ABOUT findings, and it survives truncation while the thing it describes does not.

## Why it was hard to see

Every failure mode here presents as success. The verifier ran, it answered, its answer was well-formed and even alarming in the right direction. Assuming the transport is lossless is the default, and the stored log is normally the fallback that makes truncation recoverable - here both failed identically, so the second look confirmed the first rather than correcting it.

## Fix

Require the verifier to write its FULL report to a FILE and reply with only the compact verdict table, so the reply is small enough to survive any transport and the evidence lives somewhere re-readable. When a verdict arrives without its supporting detail, do not quote the partial trace as a result: re-measure every claim yourself against the primary sources.

## Verification

Re-measuring all thirteen claims by hand found zero document defects; the reported FAIL remained an unresolved hypothesis, most likely the verifier's own strict-equality comparison of a qualified cell value against a bare one. So the verdict was not merely unreadable, it was probably wrong - which is the second argument for never quoting a partial trace.

## Transferable rule

> A verifier that answers is not a verifier that reported: transport AND the stored log can truncate at the same boundary, losing the finding entirely. Have the verifier write its full report to a FILE and reply with only the verdict table. A summary line asserting a count is a claim about findings, not a finding - never quote a partial trace as a result.

## Related

[INC-0005](./INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md) [INC-0025](./INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md)
