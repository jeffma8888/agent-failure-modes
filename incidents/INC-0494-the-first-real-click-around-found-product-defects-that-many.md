---
id: INC-0494
title: The first real click-around found product defects that many static review rounds and every gate had missed
date: 2026-11-02
classes: [observability]
severity: medium
status: mitigated
---

# INC-0494 - The first real click-around found product defects that many static review rounds and every gate had missed

**Cost:** Several review rounds on a walker that found none of the defects; the defects sat in the product behind green gates until the first real run.

## Signature - how you recognise it

A cheap exploratory run on a real build produced mismatches on every checklist row, within an hour of parking the strict tool.

## What happened

After a strict browser walker was parked, a plain-checklist click-around on a real build reported mismatches against all fifteen rows. Most flows worked. It found that a seed option meant to create a minimal set had no effect and the full set was created, that a create page rendered an empty body with no input, that seeded records were published in one status field and draft in another, and that a seed report said zero media created while rows existed. Six static review rounds on the walker and every gate had found none of these. Each defect was sent to a diagnosis before any fix row, and a guess about the cause of the first stayed marked as unverified.

## Root cause

Review effort went into the tool that would run the product instead of into running the product.

## Why it was hard to see

Every gate was green and every review round produced real findings about the walker, so the product looked healthy and the review looked productive.

## Fix

Run the real product early and often on a scratch build against a plain sourced checklist, report observed against expected with screenshots, and send each mismatch to a diagnosis before a fix row.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the real product early and often; a cheap exploratory run beats another review round of the tool that would run it.

## Related

[INC-0491](./INC-0491-a-browser-walker-gathered-guards-over-many-static-rounds-unt.md) [INC-0488](./INC-0488-static-review-rounds-on-a-test-harness-left-the-same-finding.md)
