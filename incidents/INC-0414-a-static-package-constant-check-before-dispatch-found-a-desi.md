---
id: INC-0414
title: A static package-constant check before dispatch found a design constant absent on main
date: 2026-11-02
classes: [stale-module]
severity: low
status: fixed
---

# INC-0414 - A static package-constant check before dispatch found a design constant absent on main

**Cost:** A runtime import failure was found at planning time instead of during a run.

## Signature - how you recognise it

A design named a constant that the code on main did not export.

## What happened

a static package-constant check before dispatch found that the design's upload constant was absent on main, which turned a predictable runtime import failure into a planning fact

## Root cause

the design was written ahead of the code that would export the constant

## Why it was hard to see

The failure would have appeared only when the importing code ran.

## Fix

Run a static check of the constants and exports a design names before dispatching the work

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before dispatch, check statically that every constant and export the design names exists on main

## Related

[INC-0405](./INC-0405-the-demo-server-served-a-build-made-before-the-merge-so-a-wa.md) [INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0430](./INC-0430-a-route-validator-rejected-a-width-that-the-generator-was-re.md)
