---
id: INC-0447
title: Tests authored but never executed passed acceptance, and the first run of the heavy tier found a failing case
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0447 - Tests authored but never executed passed acceptance, and the first run of the heavy tier found a failing case

**Cost:** A test defect surfaced one row late, and a fix branch and an acceptance addendum were needed.

## Signature - how you recognise it

A row was signed off with part of its tests never run.

## What happened

a row was accepted on unit, type and lint checks while its ten heavy-tier cases were recorded as authored, not executed; the first run of the heavy tier on the merged tree found one failing case (G08), a test defect: the framework's bulk update computes one generated file once and reuses it for every target, so a two-target bulk replacement gave both documents the same filename; the lead fixed the test on a branch and ruled that from the next row on a production merge is accepted only after the heavy tier passes on the merged tree, added to the other gates and not substituted for them

## Root cause

the acceptance gates did not include the tier that held the row's heaviest cases

## Why it was hard to see

The evidence file honestly said the cases were not run, and the gates still passed.

## Fix

run the heavy tier on the merged tree before acceptance, and treat authored-but-unexecuted cases as missing evidence

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Accept a production merge only after the heavy test tier passes on the merged tree; authored but unexecuted cases are missing evidence, not a pass

## Related

[INC-0203](./INC-0203-a-setup-failure-was-at-risk-of-counting-as-a-test-run.md) [INC-0292](./INC-0292-a-snapshot-recorder-that-finished-was-taken-as-proof-it-had.md) [INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md)
