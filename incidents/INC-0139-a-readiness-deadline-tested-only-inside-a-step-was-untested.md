---
id: INC-0139
title: A readiness deadline tested only inside a step was untested outside it
date: 2026-10-30
classes: [stage-timeout, false-green]
severity: medium
status: fixed
---

# INC-0139 - A readiness deadline tested only inside a step was untested outside it

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A deadline is proven on one code path and ships on another.

## What happened

A readiness deadline was tested only inside a step, so the path outside a step had no test.

## Root cause

The test used the convenient path.

## Why it was hard to see

The deadline works where it is tested.

## Fix

Add a case for the outside path.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Test the deadline on every path that can reach it.

## Related

[INC-0095](./INC-0095-port-validation-tests-lacked-separate-absent-zero-and-shared.md)
