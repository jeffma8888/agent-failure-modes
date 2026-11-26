---
id: INC-0651
title: An author self-certified review findings as fixed inside the document being reviewed
date: 2026-11-23
classes: [false-green, delegation]
severity: low
status: mitigated
topic: false-green/oracle-or-claim-written-from-memory
occurrences: 1
---

# INC-0651 - An author self-certified review findings as fixed inside the document being reviewed

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A test oracle, locator or review claim came from memory, not source](../catalog/false-green/oracle-or-claim-written-from-memory.md)

**Cost:** One misleading status line in a review candidate needed correction; no downstream acceptance based on the line was reported.

## Signature - how you recognise it

An artifact under review states that all blocking findings are fixed, but the attestation is authored by the person whose work is being reviewed rather than by the reviewer.

## What happened

An author inserted a status line declaring every one of eight blocking findings fixed in the same document that was awaiting independent review. A second-model reviewer flagged that the line was self-certification, not an independent recheck receipt.

## Root cause

The author treated an assertion of completion in the work product as if it could stand in for a reviewer-owned verification record.

## Why it was hard to see

The status line resembles an ordinary progress update and can be factually plausible, but its placement makes an unaudited author claim look like a review verdict.

## Fix

Remove author-written verification claims from the reviewed artifact; let the independent reviewer record finding closure in a separate reviewer-authored log after inspecting the revised artifact.

## Verification

A second-model reviewer identified the self-certification. The input does not establish whether all eight findings were in fact fixed or whether a final reviewer-authored closure log was completed.

## Transferable rule

> Keep verification status in a reviewer-authored review log; authors may describe changes but must not self-certify that blocking findings are verified closed in the artifact under review.

## Related

[INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) [INC-0057](./INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md)
