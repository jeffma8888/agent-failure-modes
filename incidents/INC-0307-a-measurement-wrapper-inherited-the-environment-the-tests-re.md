---
id: INC-0307
title: A measurement wrapper inherited the environment the tests replace
date: 2026-11-01
classes: [tooling-paths, ipc-and-env]
severity: medium
status: fixed
---

# INC-0307 - A measurement wrapper inherited the environment the tests replace

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A timing wrapper found its tool through variables the tests replace on purpose, so runs failed before measuring anything.

## What happened

a wrapper that only added timing resolved its tool through the search path and then the home variable, both of which the tests replace on purpose, so the first attempt ran zero tests and two more produced false reds

## Root cause

a wrapper that only added timing resolved its tool through the search path and then the home variable, both of which the tests replace on purpose, so the first attempt ran zero tests and two more produced false reds

## Why it was hard to see

The wrapper works in a clean shell and fails only under fixtures that replace its variables, and the failures look like test reds.

## Fix

Give the wrapper fixed absolute tool paths, have it read no variable the tests set or replace, and label a run that fails this way INVALID INVOCATION, keep it, and count it neither as a red nor as a measurement

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A wrapper that only adds reporting uses fixed absolute tool paths and reads no variable the tests set or replace; an invalid invocation is kept but is neither a red nor a measurement

## Related

[INC-0256](./INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) [INC-0257](./INC-0257-moving-the-home-directory-broke-a-launch-that-found-its-cach.md)
