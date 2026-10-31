---
id: INC-0176
title: A shape regex was used as ownership evidence for a sweep
date: 2026-10-30
classes: [detector-fail-open, identity-and-keying]
severity: medium
status: fixed
---

# INC-0176 - A shape regex was used as ownership evidence for a sweep

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A sweep matched files it did not own.

## What happened

A sweep selected files by a shape regex and treated the match as ownership, with no decoys to prove it did not over-match.

## Root cause

Shape is cheap to match and looks like ownership.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Add decoys to the sweep as a gate has.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A sweep that decides by shape needs decoys.

## Related

[INC-0159](./INC-0159-a-second-reader-of-the-same-registry-file-was-at-risk-of-rep.md)
