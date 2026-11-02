---
id: INC-0120
title: A guard control asserted only exit 0, so a warn-and-pass guard looked like a clean pass
date: 2026-10-30
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0120 - A guard control asserted only exit 0, so a warn-and-pass guard looked like a clean pass

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

A guard that prints an error but exits 0 passes a control that checks the exit code.

## What happened

A guard control did not assert the absence of the error text, so a guard that warned and passed was indistinguishable from a clean pass.

## Root cause

Only the exit code was checked.

## Why it was hard to see

Exit 0 is the expected success signal.

## Fix

Assert the absence of the error text as well.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check output as well as exit status in a clean-pass control.

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) [INC-0347](./INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md) [INC-0462](./INC-0462-an-identity-guard-compared-to-a-plain-address-while-the-data.md)
