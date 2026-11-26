---
id: INC-0642
title: A quote check passed on the collector's own annotations because it only asked whether the text appeared anywhere in the capture file
date: 2026-11-16
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
topic: false-green/check-satisfied-by-unrelated-cause
occurrences: 1
---

# INC-0642 - A quote check passed on the collector's own annotations because it only asked whether the text appeared anywhere in the capture file

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A negative, absence or presence check passed for an unrelated reason](../catalog/false-green/check-satisfied-by-unrelated-cause.md)

**Cost:** A summary claimed the source named specific problem numbers when only the collector had; the affected claims were rewritten after a re-fetch and a review comparison. How long the claim stood was not recorded.

## Signature - how you recognise it

A claim says the source names something, its supporting quote is in the capture file, and the same words are not on the live page.

## What happened

A research teammate saved each page it read into a capture file that mixed verbatim page text with its own annotations, such as notes that a question was a variant of a numbered problem on a public practice site. The verifier's quote check only asked whether a quoted string appeared somewhere in the capture file. The annotations therefore passed as source wording and supported a claim that the source itself named the problem number. An author caught it on re-fetching the page, and a reviewer caught it independently by comparing the summary line with the annotation.

## Root cause

The capture format did not separate verbatim text from collector notes, and the quote check graded membership in the whole file instead of membership in the verbatim block.

## Why it was hard to see

The annotations were short and written in the same register as the page text, and the check reported a match, so the claim carried the look of a verified quote.

## Fix

Claims now cite the page's own wording, and a problem-number grouping is kept only where the source writes the number itself. Captures keep verbatim text and collector notes in visibly separate blocks, and quotes are graded against the verbatim block only.

## Verification

Checked: the page was re-fetched and the claims compared with its wording. Not checked: other capture files from the same collector for annotations that reached a summary.

## Transferable rule

> Keep verbatim captures and collector notes in visibly separate blocks, and grade every quote against the verbatim block only; a match anywhere in a capture file is not a match in the source.

## Related

[INC-0122](./INC-0122-a-digest-present-anywhere-in-a-manifest-was-taken-as-proof-i.md)
