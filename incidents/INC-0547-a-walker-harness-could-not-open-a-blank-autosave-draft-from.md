---
id: INC-0547
title: A walker harness could not open a blank autosave draft from the list because its name link had no text, and a second selector matched three links
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0547 - A walker harness could not open a blank autosave draft from the list because its name link had no text, and a second selector matched three links

**Cost:** Two walk rows were blocked; the lead recorded the missing-text link as a candidate defect and ordered a rerun with the exact address and the earlier exact link.

## Signature - how you recognise it

A list link has no accessible text, and a looser selector matches more than the one intended link.

## What happened

A blank autosave draft created during a walk was listed with a name link that had no text, so an ordinary click timed out and the editor could not be opened from the list. A separate row was blocked because the walker selector matched the list link and both create links instead of the exact link recorded earlier. The lead ruled to open the draft by typing its editor address, to rerun the other row with the exact earlier link, and to record the element source, its box and a screenshot as evidence of the candidate defect.

## Root cause

One was a product gap (a link with no text), the other a selector looser than the recorded exact one.

## Why it was hard to see

A blocked row can come from the walker or from the product, and only the element evidence tells which.

## Fix

Record the element and a screenshot, open the record by its address as an ordinary navigation, and reuse the exact recorded link.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Reuse the exact recorded link instead of a looser selector, and record the element evidence for a link that cannot be clicked.

## Related

[INC-0527](./INC-0527-an-absence-check-for-a-hidden-field-matched-the-hidden-input.md)
