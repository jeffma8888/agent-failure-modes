---
id: INC-0336
title: A tier exclusion was added only after a witness failed without it
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0336 - A tier exclusion was added only after a witness failed without it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A configuration change had a witness that was red before and green after.

## What happened

a config change that moves tests between tiers was made test first: witnesses of the destination failed while the fast tier still included the moved files, and passed once the exclusion was added

## Root cause

a config change that moves tests between tiers was made test first: witnesses of the destination failed while the fast tier still included the moved files, and passed once the exclusion was added

## Why it was hard to see

Configuration looks like plumbing, so it is changed without the red step that code gets.

## Fix

Write the red witness first, then change the config and watch it pass

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A config change that moves tests between tiers needs a red witness first, the same as a code change

## Related

[INC-0332](./INC-0332-a-tier-exclusion-matched-only-one-file-extension.md) [INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md)
