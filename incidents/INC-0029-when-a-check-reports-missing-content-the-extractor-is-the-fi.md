---
id: INC-0029
title: When a check reports missing content, the extractor is the first suspect
date: 2026-08-27
classes: [detector-fail-open, tooling-paths, observability]
severity: high
status: fixed
---

# INC-0029 - When a check reports missing content, the extractor is the first suspect

**Cost:** Came one step from 'repairing' a CORRECT file by re-inserting 83 words that were never missing - which would have duplicated content and made a provably lossless artifact genuinely lossy.

## Signature - how you recognise it

The reported-missing content forms a clean PREFIX plus SUFFIX of the whole, instead of being scattered through the middle. Two different ways of counting the same units disagree.

## What happened

A checker verifying that a reformatted document was lossless stripped structured segment labels with a pattern whose character class did not allow parentheses. It therefore skipped the two segments whose labels contained them, and reported the words inside those segments as absent from a file that was in fact complete.

## Root cause

The MEASUREMENT was wrong, not the artifact: the extractor's pattern was narrower than the real data format. This class is expensive because of its asymmetry - a false negative about content points directly at a DESTRUCTIVE remedy, so believing it costs more than any missed detection would.

## Why it was hard to see

The checker ran cleanly over most of the file and produced a precise, plausible list of missing words. Nothing errored, and a delegated runner had reported the underlying conversion as 2/2 SUCCESS, so every green signal agreed with the wrong conclusion.

## Fix

Count the units TWO ways - strict pattern matches versus a loose structural count - and treat disagreement as an indictment of the extractor, not the artifact. Read the real format off disk BEFORE writing any repair: the pre-write inspection is the control, and the assertion is not. And grade delegated work by its artifact, never by the runner's success ledger.

## Verification

The two counts were 81 against 83; reading the actual label format off disk revealed the parenthesised labels; after widening the pattern the file verified as lossless and needed no repair at all. The shape of the diff was the free tell that had been available from the start - a real conversion loss is scattered, not a tidy prefix plus suffix.

## Transferable rule

> When a check reports missing content, suspect the extractor before the artifact: a false negative about content points at a destructive remedy. Count the units two ways (strict pattern versus loose structural) and let disagreement indict the measurement. Read the real format off disk before writing any repair, and never grade delegated work by a runner's success ledger.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md)
