---
id: INC-0577
title: An exact list in a test was authored on an older base and reviewed on a newer one where a new collection already existed
date: 2026-11-04
classes: [stale-module]
severity: low
status: mitigated
---

# INC-0577 - An exact list in a test was authored on an older base and reviewed on a newer one where a new collection already existed

**Cost:** The baseline failed in setup; no browser credit was given, and another successor was needed.

## Signature - how you recognise it

An exact list of business items is authored before a merge that adds an item, and reviewed after.

## What happened

A successor root was authored on a base before a feature merge and approved on a later base where the configuration already registered a new business collection. The activation baseline failed in setup because the exact list received the new collection after the earlier ones, and one case failed while two did not run. The new collection is a real business collection with authenticated access, never to be filtered as internal. The review had checked the internal entries only. The lead lesson: a review of an exact list compares it to the current main product source.

## Root cause

The list was compared with the author base, not with the current product source.

## Why it was hard to see

The internal entries matched and the review stopped there.

## Fix

Compare an exact list against the current main product source at review time.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A review of an exact list compares it with the current main product source, including business items, not the internal entries alone.

## Related

[INC-0559](./INC-0559-a-successor-root-was-authored-and-approved-without-a-run-and.md)
