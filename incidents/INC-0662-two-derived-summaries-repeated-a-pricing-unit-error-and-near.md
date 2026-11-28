---
id: INC-0662
title: Two derived summaries repeated a pricing unit error and nearly corroborated each other
date: 2026-11-26
classes: [spec-and-scope, false-green]
severity: medium
status: mitigated
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0662 - Two derived summaries repeated a pricing unit error and nearly corroborated each other

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** The same pricing unit error appeared in two summaries and nearly survived review; no purchase or downstream cost calculation was reported.

## Signature - how you recognise it

Two derived documents agree on a price unit, while their canonical fact section describes a different charging basis.

## What happened

An author summarized a pricing range as per person even though the cited fact section described one provider as charging a flat fee for a team. A recommendation elsewhere repeated the same unit error. During review, agreement with that second summary nearly counted as confirmation until the reviewer returned to the fact section. The author error and reviewer near-miss are two observations of the same unverified transfer of a quantity and its unit through derived documents.

## Root cause

Repeated summaries were treated as independent evidence, and the price unit was not carried and checked alongside the amount at its authoritative source.

## Why it was hard to see

The numbers look consistent across documents; the error becomes visible only when the charging unit is checked rather than the numeric range alone.

## Fix

Trace each price to its fact section, check the amount and charging basis together, and treat any summary agreement as non-independent until that source check is complete.

## Verification

A second-model reviewer compared the pricing unit with the canonical fact section and identified the repeated error. Correction of every downstream copy and later adherence to the rule were not established.

## Transferable rule

> Check each price and its charging unit against the canonical fact section before writing or grading it; agreement between derived summaries is not independent corroboration.

## Related

[INC-0639](./INC-0639-a-number-the-user-said-in-conversation-was-stored-as-a-fact.md) [INC-0643](./INC-0643-a-knowledge-base-digest-s-inference-about-a-past-decision-wa.md)
