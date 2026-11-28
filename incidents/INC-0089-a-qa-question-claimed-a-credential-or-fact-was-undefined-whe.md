---
id: INC-0089
title: A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed
date: 2026-10-30
classes: [spec-and-scope]
severity: low
status: fixed
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 2
---

# INC-0089 - A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A recorded question says a value is undefined, but a search of the cut finds it.

## What happened

Before acceptance a QA question was found to be answered in the cut. Separately, a restore performed through a gated write failed unless the seed satisfied the gate.

## Root cause

The question was written without searching the oracle, and the gate precondition was not part of the seed.

## Why it was hard to see

An unsearched question looks like a real gap.

## Fix

Grep the cut before accepting a question that says a fact is undefined; make the seed satisfy any gate a restore passes through.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Search the oracle before recording a question, and design seeds for the gates that tests pass through.

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-26 - A design reviewer first classified an unresolved tier as a contradiction; the upstream handoff note already recorded it as a hold owned by an external approver. Caught on re-reading the handoff before the finding was issued; a gap is now classified by its stated owner first.
