---
id: INC-0222
title: A clean-tree positive did not exercise the working-file context
date: 2026-10-31
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0222 - A clean-tree positive did not exercise the working-file context

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The clean tree matched the baseline, so the refusal path never ran.

## What happened

A clean-tree positive did not test the working-file context of a checker that picks its baseline by byte equality.

## Root cause

A clean-tree positive did not test the working-file context of a checker that picks its baseline by byte equality.

## Why it was hard to see

A clean tree is the natural fixture.

## Fix

Plant a harmless byte difference before proving a refusal

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Plant a harmless byte difference before proving a refusal when the baseline is chosen by byte equality

## Related

[INC-0183](./INC-0183-sibling-fixture-factories-lacked-the-metadata-that-makes-a-c.md)
