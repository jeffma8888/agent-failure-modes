---
id: INC-0401
title: A dispatch packet called a root absent an hour after it had landed
date: 2026-11-02
classes: [stale-module]
severity: low
status: fixed
---

# INC-0401 - A dispatch packet called a root absent an hour after it had landed

**Cost:** A review could have been set up around a root that was no longer missing.

## Signature - how you recognise it

A packet stated a root was absent when it was already present on main.

## What happened

a dispatch packet called the r3 root absent an hour after it had landed on main

## Root cause

the packet carried the state from when it was written and was not re-read against main

## Why it was hard to see

A conditional statement read as a fact, and the landing was an hour old and easy to miss.

## Fix

A conditional packet re-reads the newest main for every root it names before review

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A conditional packet must re-read the newest main for every root it names before review

## Related

[INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) [INC-0376](./INC-0376-a-signed-design-heading-outranked-a-plan-census-parenthetica.md) [INC-0414](./INC-0414-a-static-package-constant-check-before-dispatch-found-a-desi.md)
