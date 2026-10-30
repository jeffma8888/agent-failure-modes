---
id: INC-0077
title: Keeping an error prefix did not keep the downstream classification, and a free-text reason could carry markers or secrets
date: 2026-10-30
classes: [detector-fail-open, observability]
severity: high
status: mitigated
---

# INC-0077 - Keeping an error prefix did not keep the downstream classification, and a free-text reason could carry markers or secrets

**Cost:** Near miss, caught by an independent pre-implementation review. A spec would have let a cleaned-up reason string reclassify a fatal authentication failure as another failure kind, and its length-based redaction could not prove that no secret survived.

## Signature - how you recognise it

New text is appended to a log line that a downstream classifier scans, on the argument that the line keeps its prefix.

## What happened

A spec appended a cleaned-up stderr reason to a fatal authentication line and argued the dispatcher would still classify it as authentication because the prefix was unchanged. The dispatcher scans the whole log for the first matching marker in a fixed kind order, so a reason that contained a service or stall marker would have been filed as that kind.

## Root cause

The argument reasoned about the first characters of the line, but the classifier reads all of it in a fixed priority order. Free text also cannot be proven free of secrets by a length-based pattern.

## Why it was hard to see

The prefix argument sounds right and the classifier's scan order is not visible in the spec. The two risks, misclassification and leakage, come from the same free-text field.

## Fix

Revision 1 emits one of six fixed categories instead of free text, and the tests apply the dispatcher's real scan order to every fatal line.

## Verification

Checked: the classifier's scan order was read and the revised spec removes free text. Not yet verified: the implementation against the new tests.

## Transferable rule

> When output feeds a downstream classifier, test the classifier's verdict on it, not its prefix. Emit fixed categories instead of free text when the text could carry secrets or markers.

## Related

[INC-0033](./INC-0033-one-normaliser-is-not-enough-if-it-maps-the-two-sides-into-d.md) [INC-0032](./INC-0032-removing-a-veto-exposes-the-broken-classifier-it-was-masking.md) [INC-0068](./INC-0068-a-retry-ladder-wrapped-the-model-call-but-not-the-credential.md)
