---
id: INC-0028
title: When two distributions overlap there is no threshold - change the signal, not the number
date: 2026-08-28
classes: [false-green, observability, detector-fail-open]
severity: medium
status: fixed
---

# INC-0028 - When two distributions overlap there is no threshold - change the signal, not the number

**Cost:** A tuning exercise that could never have converged: every lexical signal measured overlapped between the two populations it was supposed to separate, so each retune only chose which error to make.

## Signature - how you recognise it

Every candidate cutoff either misses real positives or refuses real work, and moving it just trades one error for the other. Each individual measurement looks reasonable.

## What happened

A near-duplicate gate needed a similarity threshold. Hand-labelling 24 real records gave 276 pairs - 28 restatements of one item and 248 genuinely distinct - and every lexical signal overlapped on that ground truth: body Jaccard ran a 0.100 minimum on duplicates against a 0.105 maximum on distinct pairs; containment 0.205 against 0.213; title similarity 0.275 against 0.482. Restricting comparison to records sharing a category did not rescue it either, because only 13 of the 28 duplicate pairs shared both category fields.

## Root cause

The signal did not carry the distinction. A threshold can only separate populations whose distributions are separable; where the ranges overlap, no cutoff exists and tuning merely selects which class of error to commit.

## Why it was hard to see

Every individual similarity number is plausible and the code is correct. The impossibility is invisible until you deliberately print the MINIMUM of one population against the MAXIMUM of the other - a comparison nobody makes while iterating on a cutoff that is 'nearly right'.

## Fix

Change what is measured to something EXECUTABLE: two records are the same if their detectors reproduce each other's verdicts on each other's own fixtures. Require the agreement to be MUTUAL, because a one-way hit is subsumption rather than identity. And require the SILENT half - fires on the other's bad fixture AND stays quiet on the other's good fixture - because without it any sufficiently broad check counts as a twin.

## Verification

The behavioural test gave ZERO false positives on the same 248 distinct pairs where every lexical signal overlapped. Mutation testing then found three blind spots the green suite had hidden, including a control whose two fixtures shared zero tokens and would therefore have passed at ANY threshold including zero; that test only became real once its fixture was measured into the band just below the cutoff (0.167 against 0.20) and the test asserted that precondition itself.

## Transferable rule

> Before choosing a threshold, measure the MINIMUM of one population against the MAXIMUM of the other. If they overlap, no cutoff exists and tuning only picks which error you make - find an EXECUTABLE consequence of the two things being the same instead. Require mutual agreement (one-way is subsumption) and test the silent half, or any broad check counts as a twin.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - commit 315bc6e ships the behavioural interchangeability check that replaced the lexical threshold; e37ef89 and tools/verify_mutations.py are the mutation harness that found the blind spots.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0027](./INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md)
