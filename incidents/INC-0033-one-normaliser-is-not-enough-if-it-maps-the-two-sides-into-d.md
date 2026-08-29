---
id: INC-0033
title: One normaliser is not enough if it maps the two sides into different conventions
date: 2026-08-28
classes: [detector-fail-closed, observability]
severity: high
status: fixed
---

# INC-0033 - One normaliser is not enough if it maps the two sides into different conventions

**Cost:** Third recurrence of the same defect in the same module. The first two were caught by hand before they did damage; this one ran long enough to produce roughly nineteen false accusations of fabricated evidence.

## Signature - how you recognise it

A checker reports that a string is absent from a document where you can see it with your own eyes. The near-miss it prints is a clean prefix or suffix of the real text, or differs from it only in whitespace or punctuation.

## What happened

A verifier compared a quote against a fetched page after normalising both sides. It called ONE normaliser on both, which is the correct structure - but the transformation was not text-preserving: replacing a markup tag with a space inserts whitespace the quote side, which never contained markup, can never have. So a single function mapped the two inputs into two different conventions. The two earlier instances in the same module were a curly-quote normalisation applied to the quote but not to the page, and an inline code span whose surrounding tags inserted a space inside a field name.

## Root cause

'Use one normaliser on both sides' is necessary and not sufficient. The normaliser must also map both inputs into the SAME output convention. A rule that is right for one side - tags become whitespace, because tags separate words - is corruption on a side that never had tags.

## Why it was hard to see

Fail-closed defects point at a destructive remedy. A fail-open detector goes unnoticed; a fail-closed one produces a confident, specific accusation about an artifact, and the obvious response is to repair the artifact - deleting correct evidence, or 'correcting' a quote that was already right. The expensive mistake is the DIRECTION of repair, not the bug.

## Fix

Make the normaliser text-preserving where it can be: map word-separating tags to a space and non-separating ones to nothing, then collapse the residue - here, deleting the space the normaliser had inserted before closing punctuation - so both sides land in one convention. Prove it two-sided with a known-good pair (an honest quote that must match) and a known-bad pair (a genuinely absent quote that must not), and assert the property under test is the CONVENTION, not one specific page.

## Verification

Six tests cover the normalisation alone: four fail against the unfixed code, and two pass both before and after, which is what makes the set discriminating rather than decorative. After the fix, both items the gate had quarantined verify verbatim, and 19 of 40 historical accusations resolve to verbatim matches.

## Transferable rule

> One normaliser on both sides is not enough - it must map both sides into the SAME convention. A rule right for one input (tags become spaces) is corruption on an input that never had tags. Prove a comparison with a known-GOOD pair as well as a known-bad one, and when a checker accuses an artifact you can see is correct, suspect the checker: a fail-closed defect points at a destructive repair.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - the space-before-punctuation collapse added inside the single `_norm` in `tools/verify_quotes.py`, with the two prior recurrences recorded in the same module's history.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0029](./INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0032](./INC-0032-removing-a-veto-exposes-the-broken-classifier-it-was-masking.md)
