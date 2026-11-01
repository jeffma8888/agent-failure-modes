---
id: INC-0260
title: Prove an alias fix by the exact-SHA run with the default spelling
date: 2026-11-01
classes: [tooling-paths, false-green]
severity: medium
status: fixed
---

# INC-0260 - Prove an alias fix by the exact-SHA run with the default spelling

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A path-alias fix could be proven only with a workaround in place.

## What happened

a fix for a path-alias refusal was proven by running the exact-SHA FAST with the default temp root spelling and no workaround: 128 s, 1061 tests, green

## Root cause

a fix for a path-alias refusal was proven by running the exact-SHA FAST with the default temp root spelling and no workaround: 128 s, 1061 tests, green

## Why it was hard to see

A workaround hides whether the default path still fails.

## Fix

Run the exact SHA after merge with the default spelling

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a path-alias fix by running the exact SHA with the default spelling and no workaround

## Related

[INC-0150](./INC-0150-a-missing-independently-callable-guard-lacked-protocol-cases.md)
