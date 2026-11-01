---
id: INC-0298
title: Harness and ownership defects were left for the build agent to find
date: 2026-11-01
classes: [delegation, false-green]
severity: medium
status: fixed
---

# INC-0298 - Harness and ownership defects were left for the build agent to find

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Defects unrelated to the product were found only after the build started.

## What happened

owner mismatch, a missing decoder import and a missing second account all failed before any product code existed; they surface cheaply in a red check and expensively after the build agent has started

## Root cause

owner mismatch, a missing decoder import and a missing second account all failed before any product code existed; they surface cheaply in a red check and expensively after the build agent has started

## Why it was hard to see

A failing test looks like the expected red, whatever the reason.

## Fix

Run each pending file once against the unmodified snapshot and classify the first failure as product or harness

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run a red check before the build agent starts and classify each first failure

## Related

[INC-0100](./INC-0100-a-new-test-file-was-placed-in-a-row-whose-activation-order-d.md)
