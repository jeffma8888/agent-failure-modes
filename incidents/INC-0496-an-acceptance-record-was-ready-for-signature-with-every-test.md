---
id: INC-0496
title: An acceptance record was ready for signature with every test tier green while the main page of the row was blank
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
topic: false-green/real-page-or-response-wrong-behind-green
occurrences: 1
recurrence_of: INC-0241
---

# INC-0496 - An acceptance record was ready for signature with every test tier green while the main page of the row was blank

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [Tests pass but the real page, status or session is wrong](../catalog/false-green/real-page-or-response-wrong-behind-green.md)

> **Recurrence of [INC-0241](./INC-0241-automated-tests-passed-while-nobody-had-walked-the-real-site.md).** This record repeats an earlier failure and is kept for history; INC-0241 is the canonical record (2 occurrences in total) and carries the rule to apply.

**Cost:** Four record revisions reached the point of signature on a row whose deliverable page did not render; the signature and the later steps that wait on it were held.

## Signature - how you recognise it

Every test tier was green and a page the row ships returned a blank body.

## What happened

An acceptance record went through four revisions and was ready for signature with every test tier green. The create page for one of the row deliverables rendered with a success status and an empty body, with no input. Only a click-around on a real build showed it. The diagnosis found that the render threw an error in the server log, because the collection enables draft autosave and the empty new draft ran a slug hook that has no source to derive from; the sibling collections without autosave rendered. The signature was held until the fix row is merged and a rerun shows the page working and a record created and edited.

## Root cause

The acceptance evidence was test tiers alone, and none of them rendered the page the row ships.

## Why it was hard to see

The record was complete, reviewed and green, and a page that returns a success status with an empty body looks fine to every check that does not read the body.

## Fix

Hold the signature, fix the page with a test first, and require one observed run showing the page rendering and a record created and edited before signing.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before signing a row that ships a page, require one observed run of that page; green test tiers alone are not acceptance for a user-facing row.

## Related

[INC-0494](./INC-0494-the-first-real-click-around-found-product-defects-that-many.md) [INC-0490](./INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md)
