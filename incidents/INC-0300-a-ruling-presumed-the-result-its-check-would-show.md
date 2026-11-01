---
id: INC-0300
title: A ruling presumed the result its check would show
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0300 - A ruling presumed the result its check would show

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A ruling stated that the next check must show a particular failure.

## What happened

a ruling required the next red to be a missing product module, which is wider than the evidence: it could turn another genuine infrastructure failure into a forced classification, and a later baseline need not stay red

## Root cause

a ruling required the next red to be a missing product module, which is wider than the evidence: it could turn another genuine infrastructure failure into a forced classification, and a later baseline need not stay red

## Why it was hard to see

A predicted result reads as part of the plan, so a different result looks like a deviation.

## Fix

Prescribe the remedy and the check, and record the observed first result, including a green or another cause

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A ruling prescribes the remedy and the check, never the result the check must show

## Related

[INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md)
