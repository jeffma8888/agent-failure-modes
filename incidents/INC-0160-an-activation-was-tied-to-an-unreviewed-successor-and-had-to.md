---
id: INC-0160
title: An activation was tied to an unreviewed successor and had to be re-ruled
date: 2026-10-30
classes: [checkpoint, spec-and-scope]
severity: medium
status: fixed
---

# INC-0160 - An activation was tied to an unreviewed successor and had to be re-ruled

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A shipped revision waited on a later revision that had not been reviewed.

## What happened

A ruling tied activation of a reviewed revision to the activation of its unreviewed successor; it was replaced so the reviewed revision activates in the first ready engineer row.

## Root cause

Activation timing was coupled to a successor whose review was still pending.

## Why it was hard to see

The coupling felt safe, since the successor would supersede it anyway.

## Fix

Activate the reviewed revision now; route the successor reviewer advisories forward as non-gating, and note that a flagged pending file owes a revision before its own activation.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not tie the activation of a reviewed revision to an unreviewed successor.

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md)
