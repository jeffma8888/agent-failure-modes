---
id: INC-0315
title: A static checker's PASS was read as acceptance without an anchored baseline
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0315 - A static checker's PASS was read as acceptance without an anchored baseline

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An identity PASS appeared with no recorded hash behind the supplied baseline.

## What happened

a static identity check reported PASS against a baseline it never anchored to recorded hashes, and the PASS was read as acceptance

## Root cause

a static identity check reported PASS against a baseline it never anchored to recorded hashes, and the PASS was read as acceptance

## Why it was hard to see

The word PASS carries no label for what kind of check produced it or what it was compared with.

## Fix

Label a static PASS as static, anchor it to recorded hashes, and never let it stand in for runtime or acceptance

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A static tool's PASS is labeled as static and anchored to recorded hashes; it never stands in for runtime or acceptance

## Related

[INC-0289](./INC-0289-a-passing-identity-check-was-taken-as-agreement-with-the-sig.md) [INC-0193](./INC-0193-a-negative-grep-was-taken-as-proof-that-a-removal-ruling-was.md)
