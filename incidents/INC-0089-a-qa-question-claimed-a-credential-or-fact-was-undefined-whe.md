---
id: INC-0089
title: A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed
date: 2026-10-30
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0089 - A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed

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
