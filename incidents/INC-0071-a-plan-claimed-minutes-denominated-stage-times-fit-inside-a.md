---
id: INC-0071
title: A plan claimed minutes-denominated stage times fit inside a cap stated in seconds
date: 2026-10-29
classes: [spec-and-scope, stage-timeout]
severity: medium
status: mitigated
---

# INC-0071 - A plan claimed minutes-denominated stage times fit inside a cap stated in seconds

**Cost:** Caught in plan review before the plan was accepted. Left in, it would have scheduled work that the hard per-step cap kills.

## Signature - how you recognise it

A budget in one unit is compared with an estimate in another, and the document states that one fits inside the other.

## What happened

A plan called 20 to 45 minutes of engineer stage time inside an 1800 second stage cap and a 1700 second engine budget. Forty-five minutes is 2700 seconds, so the fit claim was arithmetically false.

## Root cause

Two quantities in different units were compared by eye. The shape of the sentence (a range inside a cap) read as correct without a conversion.

## Why it was hard to see

The numbers are each reasonable and the claim sounds like the conclusion of an analysis. Only converting both to one unit exposes it.

## Fix

Queued for the next revision: give per-stage numbers in the cap's unit, relabel totals as iteration time, and split rows whose stage can exceed about 25 minutes.

## Verification

Two reviewers independently caught it by converting the units. The revised plan is not yet verified.

## Transferable rule

> Convert every budget and estimate to one unit before writing that one fits inside the other.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0003](./INC-0003-a-slow-test-suite-makes-a-product-unbuildable-by-the-loop.md)
