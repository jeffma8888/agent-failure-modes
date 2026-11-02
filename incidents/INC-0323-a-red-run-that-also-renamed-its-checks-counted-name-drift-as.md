---
id: INC-0323
title: A red run that also renamed its checks counted name drift as defects
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0323 - A red run that also renamed its checks counted name drift as defects

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A large failure count included checks that failed only because they were renamed.

## What happened

a red-first run against the older tool also renamed checks, so part of its failure count was missing names and presentation differences instead of behaviour defects, and the count alone suggested more evidence than existed

## Root cause

a red-first run against the older tool also renamed checks, so part of its failure count was missing names and presentation differences instead of behaviour defects, and the count alone suggested more evidence than existed

## Why it was hard to see

A big red number looks strong, and the renamed checks fail for a reason that is not a defect.

## Fix

Show real behavioural reds per fix, paired with aggregate and exit evidence, and not a bare failure count

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A red-first run that also renames checks shows real behavioural reds per fix, paired with aggregate and exit evidence, never a bare failure count

## Related

[INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) [INC-0287](./INC-0287-an-oracle-that-matches-a-substring-or-a-loose-boundary-can-b.md)
