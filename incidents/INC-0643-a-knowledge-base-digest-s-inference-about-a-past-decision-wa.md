---
id: INC-0643
title: A knowledge-base digest's inference about a past decision was written into the user's notes as the decision, and the primary record said the opposite
date: 2026-11-19
classes: [spec-and-scope]
severity: medium
status: mitigated
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0643 - A knowledge-base digest's inference about a past decision was written into the user's notes as the decision, and the primary record said the opposite

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** The user's preparation notes stated the opposite of the real decision until a follow-up check; whether they were relied on in the meantime was not recorded.

## Signature - how you recognise it

A decision or status in a user-facing file traces to a summary whose verbs hedge (implicitly aligns, emerged as the leading path), not to the decision record.

## What happened

Asked about a past platform decision, an agent answered from a knowledge-base digest. The digest's wording ('implicitly aligns with', 'emerged as the leading path') was its writer's inference, not a recorded outcome, and the agent wrote it into the user's interview preparation notes as the decision taken. The original decision document recorded the other option. A follow-up question sent the agent to that document and exposed the conflict.

## Root cause

A secondary summary was used as the source for a decision, and its hedged verbs, which mark inference, were read as a report of the outcome.

## Why it was hard to see

The digest was on topic, fluent and part of a trusted knowledge base, and hedged phrasing reads as nuance rather than as a sign that the outcome was never recorded there.

## Fix

The notes were corrected from the primary decision document. A decision or status written into a user's file now cites the primary record; a summary is used only to find it.

## Verification

Checked: the primary decision document was read and the notes corrected. Not checked: other notes written from the same digest.

## Transferable rule

> Read the primary decision record before writing any decision or status into a user's file; treat hedged summary verbs (aligns with, emerged as, appears to) as the summarizer's inference, never as the outcome.

## Related

[INC-0503](./INC-0503-a-brief-stated-a-baseline-environment-from-a-compacted-summa.md)
