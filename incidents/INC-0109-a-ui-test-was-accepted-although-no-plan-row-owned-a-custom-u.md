---
id: INC-0109
title: A UI test was accepted although no plan row owned a custom UI component it needed
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0109 - A UI test was accepted although no plan row owned a custom UI component it needed

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A test drives a component that no row builds, so the last row meets a missing UI.

## What happened

A UI test needed a custom UI component that no plan row owned, so the last row would have met a missing UI.

## Root cause

Acceptance checked the test against the oracle and not against row ownership of its components.

## Why it was hard to see

The test is valid on paper and the gap appears only at build time.

## Fix

Before accepting a UI test, check that some plan row owns each custom UI component it needs.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Every component a test needs has an owning row.

## Related

[INC-0098](./INC-0098-an-acyclic-declared-dependency-graph-hid-producer-rows-that.md)
