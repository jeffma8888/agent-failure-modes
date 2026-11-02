---
id: INC-0374
title: A clause-survival script flagged 21 digest rules that a word diff showed were only wording compressions
date: 2026-11-01
classes: [detector-fail-open]
severity: low
status: fixed
---

# INC-0374 - A clause-survival script flagged 21 digest rules that a word diff showed were only wording compressions

**Cost:** A detector reported losses that were not real, which risked needless rework of the digest.

## Signature - how you recognise it

A clause-survival check flagged many rules as lost although their meaning was intact.

## What happened

a clause-survival script flagged 21 digest rules as lost; a word diff showed each was only a wording compression, so no clause was missing

## Root cause

the script compared surface words and treated any rewording as a missing clause

## Why it was hard to see

A flag from a surface-word script looks authoritative and invites restoring text that was never lost.

## Fix

Run a word diff on each flagged rule before treating it as lost; restore only what the diff shows is missing

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run a word diff before treating a flagged rule as lost

## Related

[INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) [INC-0126](./INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) [INC-0387](./INC-0387-one-review-asked-to-delete-an-error-text-assertion-while-ano.md)
