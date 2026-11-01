---
id: INC-0297
title: A test needed a second account that the minimal seed did not create
date: 2026-11-01
classes: [test-isolation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0297 - A test needed a second account that the minimal seed did not create

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Cases looked up a second admin account that the seed lacked.

## What happened

two cases needed exactly one second admin, the minimal seed created only the first, and the design lists the second, so the dependency sat outside the declared dependencies

## Root cause

two cases needed exactly one second admin, the minimal seed created only the first, and the design lists the second, so the dependency sat outside the declared dependencies

## Why it was hard to see

The cut lists the account, so the gap is only seen when the case runs.

## Fix

Declare the account as a dependency or extend the seed owner's row, and raise it before the build starts

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check each test's seed needs against the seed its declared dependencies provide

## Related

[INC-0086](./INC-0086-after-a-dependency-fix-two-rows-still-called-the-same-seed-f.md)
