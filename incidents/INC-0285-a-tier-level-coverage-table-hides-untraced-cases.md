---
id: INC-0285
title: A tier-level coverage table hides untraced cases
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0285 - A tier-level coverage table hides untraced cases

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A coverage table summarized a tier while individual cases had no trace.

## What happened

coverage was recorded per tier, so a case with no plan row, no signed decision or no anchor could hide inside a covered tier

## Root cause

coverage was recorded per tier, so a case with no plan row, no signed decision or no anchor could hide inside a covered tier

## Why it was hard to see

A tier row reads as complete when most of its cases are traced.

## Fix

Use one row per case keyed by its exact title, each naming plan row, decision row and anchors; reviewers check row by row

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Trace coverage per case, never per tier

## Related

[INC-0253](./INC-0253-two-of-four-selected-projects-executed-no-case.md)
