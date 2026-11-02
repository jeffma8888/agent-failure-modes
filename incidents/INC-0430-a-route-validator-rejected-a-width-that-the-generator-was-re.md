---
id: INC-0430
title: A route validator rejected a width that the generator was required to emit
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0430 - A route validator rejected a width that the generator was required to emit

**Cost:** No served file was affected; the seam was found at spec review.

## Signature - how you recognise it

A consumer refused a value that its own producer was required to emit.

## What happened

the spec's route validator accepted only the standard rendition widths, while the generator must emit a smaller fallback width when the crop is under the smallest standard width; the lead sanctioned a syntactic width rule (a standard width or a canonical integer in the fallback range), with served files still limited to those the generator stored, and required controls for the under-size fixture and for rejected widths

## Root cause

the validator and the generator were specified separately and never compared on the edge case

## Why it was hard to see

Each side was correct for the standard cases.

## Fix

check every producer output against every consumer validator, and add a control for the producer's edge case and for the widths the consumer must still refuse

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check every producer output against every consumer validator before signing a design, with a control for the edge output and for each refused value

## Related

[INC-0173](./INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md) [INC-0414](./INC-0414-a-static-package-constant-check-before-dispatch-found-a-desi.md)
