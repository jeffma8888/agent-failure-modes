---
id: INC-0552
title: The walker helper produced two provisional mismatches of its own, which it traced and corrected append-only before any defect was filed
date: 2026-11-02
classes: [detector-fail-closed]
severity: low
status: mitigated
---

# INC-0552 - The walker helper produced two provisional mismatches of its own, which it traced and corrected append-only before any defect was filed

**Cost:** None. Two false mismatches were corrected before they became defects.

## Signature - how you recognise it

A walk check reports a mismatch that comes from the helper expectation, not from the product.

## What happened

In a walk phase, two provisional mismatches were helper errors: the helper required a non-draft read where an autosave survived as a draft, and it required a literal key where the server names the field differently, by the localized field name twice. The walker traced both, corrected them append-only with evidence, and filed no defect. The other checks were observed as expected and the walk closed no gate it had not observed.

## Root cause

The helper encoded an expectation of the response shape that the server does not follow.

## Why it was hard to see

A mismatch looks like a product defect until the expectation is read.

## Fix

Trace each mismatch to its source, correct it append-only with evidence, and file no defect before that.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Trace a provisional mismatch to its expectation before filing a defect, and correct it append-only with evidence.

## Related

[INC-0547](./INC-0547-a-walker-harness-could-not-open-a-blank-autosave-draft-from.md)
