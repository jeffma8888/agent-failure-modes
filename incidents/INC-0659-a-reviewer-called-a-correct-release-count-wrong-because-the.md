---
id: INC-0659
title: A reviewer called a correct release count wrong because the feed had moved on since the document's date, and the real defect was a missing as-of date
date: 2026-11-25
classes: [spec-and-scope, detector-fail-closed]
severity: low
status: mitigated
topic: spec-and-scope/records-drift-or-lose-provenance
occurrences: 1
---

# INC-0659 - A reviewer called a correct release count wrong because the feed had moved on since the document's date, and the real defect was a missing as-of date

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [A cited baseline, count, line, or digest no longer matches its source](../catalog/spec-and-scope/records-drift-or-lose-provenance.md)

**Cost:** One false review finding that would have changed a correct number; the reviewer withdrew it before the author acted. Minutes.

## Signature - how you recognise it

A review marks a number or a state as wrong after checking the live source, the document's date shows it was right when written, and the sentence carries no as-of date.

## What happened

A reviewer checked a release count in a research document against the live release feed, found more releases, and flagged the count as wrong. Re-reading the document's date showed the count was correct on that date; the feed had simply moved on. The real defect was that the sentence stated a time-varying fact without an as-of date. Another document's first draft had the same author-side gap: currency claims with no date.

## Root cause

Accuracy (true on the date written) and currency (still true today) were conflated. The sentence gave no as-of date, so the reviewer compared it with today's source by default.

## Why it was hard to see

The live source is the obvious oracle and it really disagrees with the document, so the finding looks well evidenced. Without a date in the sentence, nothing prompts the reviewer to look up when it was written.

## Fix

The reviewer re-checked the document date, withdrew the accuracy finding and raised a currency finding instead: add an as-of date. Time-varying facts (counts, prices, availability, versions) now carry an as-of date in the sentence.

## Verification

Checked: the count matched the feed as of the document date. Not checked: whether every other time-varying claim in the documents now carries a date.

## Transferable rule

> Write every time-varying fact with an as-of date; when reviewing one, check the document's date before calling it wrong, and report currency (stale since) separately from accuracy (wrong on its date).

## Related

[INC-0648](./INC-0648-a-current-project-thesis-relied-on-a-shutdown-report-that-ha.md) [INC-0055](./INC-0055-a-scope-cut-was-mapped-against-the-previous-version-of-its-b.md)
