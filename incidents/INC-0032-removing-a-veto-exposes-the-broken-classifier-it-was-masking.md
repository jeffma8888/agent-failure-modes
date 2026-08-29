---
id: INC-0032
title: Removing a veto exposes the broken classifier it was masking
date: 2026-08-28
classes: [detector-fail-closed, observability]
severity: high
status: fixed
---

# INC-0032 - Removing a veto exposes the broken classifier it was masking

**Cost:** Twelve days of refusals were attributed to bad input data. Re-measured with the repaired comparison, roughly half the historical accusations are false: of 40 unique accusations across 113 escalation reports, 19 verify verbatim against their cited pages.

## Signature - how you recognise it

You remove a blocking aggregate gate expecting a flood of passes, and get a small number of confident, specific refusals instead. Each surviving refusal is individually plausible and quotable - which is exactly why you believe it.

## What happened

Two defects were stacked. The outer one was a whole-batch verdict that refused every cycle. The inner one was the comparison itself: the page normaliser turned every markup tag outside a small zero-width set into a SPACE, so a quote whose last word was wrapped in emphasis normalised to 'word .' on the page while the honest quote normalised to 'word.' - and the honest quote read as absent. While the outer veto refused everything for its own reason, the inner defect produced no distinguishable signal at all. Removing the outer veto immediately produced two refusals, and both were later shown to be false.

## Root cause

A blocking gate upstream of a classifier destroys that classifier's observability. Its false accusations are indistinguishable from the upstream refusal, so the only evidence the classifier is wrong is a mismatch nobody can see until the veto is gone. Removing the veto did not create the false accusations - it revealed them.

## Why it was hard to see

The natural reading of the first post-fix run is that the fix worked and the data was bad, because the surviving refusals are few, specific and citable. Believing them discards real evidence and accuses an honest producer of fabrication. The historical record is not self-correcting either: 113 reports had already recorded 40 distinct accusations as settled fact, so leaving them standing propagates the error into every later reading of the log.

## Fix

When a blocking gate is removed, treat every refusal the newly-unblocked classifier produces as UNVERIFIED, and re-check the first batch by hand against the primary source before acting on it. Then re-run the repaired classifier over the historical accusations and publish the split, rather than letting the old verdicts stand. Restore falsely accused items to the queue instead of dropping them.

## Verification

Both post-fix refusals were re-checked by hand against the live pages: every quote in both verified verbatim, and both items were restored to the queue. Re-running all 40 unique historical accusations through the repaired comparison gives 19 verbatim and 21 still absent (weighted by report occurrence, 1,013 rows against 1,102). The remaining 21 are a mix of genuine fabrication and page drift on heavily-edited documentation sites, and are deliberately NOT reported as fabrication.

## Transferable rule

> A blocking gate upstream of a classifier hides that classifier's errors, so removing the gate does not create the refusals you then see - it reveals them. Treat the first batch of refusals after unblocking as unverified, hand-check them against the primary source, and re-run the repaired check over the historical verdicts before letting any of them stand.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - the normaliser repair in `tools/verify_quotes.py` (71c46ad) landed only after the whole-batch veto was removed (af2db9a), and that order is what made the false accusations visible at all.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md)
