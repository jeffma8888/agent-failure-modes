---
id: INC-0653
title: Case-insensitive machine-path detection falsely flagged public API user URLs
date: 2026-11-23
classes: [detector-fail-closed]
severity: low
status: mitigated
topic: null
occurrences: 1
---

# INC-0653 - Case-insensitive machine-path detection falsely flagged public API user URLs

**Catalog:** [root](../catalog/README.md) / [detector-fail-closed](../catalog/detector-fail-closed/README.md)

**Cost:** Two public URLs were falsely reported as private-path leaks; the checking and correction time was not recorded.

## Signature - how you recognise it

A case-insensitive private-path prefix pattern matches a lowercase user-resource segment in a public API URL.

## What happened

A leak-scan command combined a machine-path prefix and personal-name alternatives under one case-insensitive setting. It flagged two public API user-resource URLs because the lowercase URL segment matched the uppercase-starting machine-path prefix. Reading the hits showed that neither was a local filesystem path.

## Root cause

A single case-insensitivity modifier was applied to tokens with different case semantics: machine-local path prefixes require exact casing, while human-name tokens may need case-insensitive matching.

## Why it was hard to see

The scanner returned real textual matches and a leak warning, but the surrounding URL scheme and host changed the meaning of the matched bytes. A combined pattern hid which alternative had produced the false positive.

## Fix

Split machine-path tokens into a case-sensitive pattern and name tokens into a separate case-insensitive pattern, then examine contextual hits before reporting a leak.

## Verification

The two hits were inspected and found to be public URL paths rather than machine-local paths. Not checked in the input: a planted-case test for the revised scanner or future leak-scan behavior.

## Transferable rule

> Keep filesystem-prefix patterns case-sensitive and separate them from case-insensitive personal-name patterns; review matched context to distinguish a public URL segment from a machine-local path.

## Related

[INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md) [INC-0479](./INC-0479-a-leak-scanner-that-walked-the-working-directory-reported-an.md)
