---
id: INC-0314
title: A probe-based test never ran its probe, so its red proved nothing about the probe
date: 2026-11-01
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0314 - A probe-based test never ran its probe, so its red proved nothing about the probe

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The test was red on the feature assertion without the probe ever executing.

## What happened

a probe-based test failed at the feature assertion before its probe machinery ran, so the red did not show that the probe could observe anything

## Root cause

a probe-based test failed at the feature assertion before its probe machinery ran, so the red did not show that the probe could observe anything

## Why it was hard to see

A red looks like proof that the test can fail, and the probe path stays unexercised.

## Fix

Add a positive control that goes green on current code, then trust a red from the new probe machinery

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Add a positive control that goes green on current code before trusting a red from new probe machinery

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) [INC-0095](./INC-0095-port-validation-tests-lacked-separate-absent-zero-and-shared.md) [INC-0318](./INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md) [INC-0320](./INC-0320-a-positive-control-s-first-red-was-the-control-s-own-defect.md) [INC-0323](./INC-0323-a-red-run-that-also-renamed-its-checks-counted-name-drift-as.md) [INC-0336](./INC-0336-a-tier-exclusion-was-added-only-after-a-witness-failed-witho.md) [INC-0339](./INC-0339-a-mutant-of-a-shared-helper-proved-sensitivity-but-not-the-r.md) [INC-0343](./INC-0343-a-weakened-final-check-survived-a-contract-suite-that-lacked.md)
