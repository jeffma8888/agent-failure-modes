---
id: INC-0133
title: A local guard behind a shared environment pin was masked, and a mutation claim was reasoned instead of measured
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0133 - A local guard behind a shared environment pin was masked, and a mutation claim was reasoned instead of measured

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

Removing a guard changes nothing because an outer pin already covers it.

## What happened

A local guard behind a shared environment pin was masked, so removing it changed nothing. The mutation claim was reasoned, not measured, and mutation scripts did not snapshot untracked copied files before mutating.

## Root cause

Masking was not tested and mutations ran on unprotected files.

## Why it was hard to see

The reasoning sounds right and the files restore only if snapshotted.

## Fix

Measure each mutation claim, test the local guard without the shared pin, and snapshot untracked copied files before mutating.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure mutations and protect files first.

## Related

[INC-0116](./INC-0116-two-validators-enforcing-the-same-rule-masked-single-file-mu.md)
