---
id: INC-0259
title: Sum every runner the earlier record summed
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0259 - Sum every runner the earlier record summed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A reported total omitted one runner.

## What happened

the FAST total was summed from the Vitest lines only and left out the 3 browser smoke tests, so 1052 was reported for a run of 1055

## Root cause

the FAST total was summed from the Vitest lines only and left out the 3 browser smoke tests, so 1052 was reported for a run of 1055

## Why it was hard to see

The partial sum looks plausible.

## Fix

Sum every runner the earlier record summed, and compare against the earlier formula

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compute a total with the same formula as the earlier record, covering every runner

## Related

[INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md)
