---
id: INC-0646
title: A debrief graded an answer as off-script against a plan stored in memory six weeks earlier, and the plan had since changed
date: 2026-11-23
classes: [spec-and-scope]
severity: medium
status: mitigated
topic: spec-and-scope/records-drift-or-lose-provenance
occurrences: 1
---

# INC-0646 - A debrief graded an answer as off-script against a plan stored in memory six weeks earlier, and the plan had since changed

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [A cited baseline, count, line, or digest no longer matches its source](../catalog/spec-and-scope/records-drift-or-lose-provenance.md)

**Cost:** One answer was wrongly scored as a repeated delivery failure, and three unsent follow-up drafts carried the stale plan; all were corrected before anything was sent.

## Signature - how you recognise it

A grade or a draft depends on a stored preference much older than the decision it gates, and the person's current statement differs from it.

## What happened

An agent debriefing a practice interview scored the person's answer about where they wanted to work as a delivery failure, a hedge for the third time, because it differed from a plan stored in memory six weeks earlier. The plan had changed, and the answer was the person's real current position. The same stale plan had also been written into three unsent follow-up drafts.

## Root cause

A stored preference was used as ground truth for a grade without checking its age or asking whether it still held.

## Why it was hard to see

The stored plan was explicit and had once been right, and the third-time framing made the mismatch look like a pattern in the person rather than a stale record.

## Fix

A correction was logged in the debrief as a correction, not an amendment; the answer was re-graded, and each draft that carried the stale line got a dated warning.

## Verification

Checked by the person who reported it: the current plan differs from the stored one, and the three drafts are marked. Not checked: other stored preferences of similar age that drive grades or drafts.

## Transferable rule

> Before scoring an answer as off-script, confirm the script still matches the person's current plan; date every stored preference that drives a grade or a draft, and re-confirm it if it is older than the decision it gates.
