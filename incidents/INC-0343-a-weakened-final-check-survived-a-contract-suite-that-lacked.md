---
id: INC-0343
title: A weakened final check survived a contract suite that lacked the right-signal, wrong-detail case
date: 2026-11-01
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0343 - A weakened final check survived a contract suite that lacked the right-signal, wrong-detail case

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Weakening a final title check survived an offline response-contract suite because no case left the title wrong while the status looked right.

## What happened

weakening a final title check to a coarse not-published check survived an offline response-contract suite, because no injected answer left the title wrong while the status stayed draft; a new partial dirty refusal cell, where the server refuses after applying a blank title but keeps the status, caught it

## Root cause

weakening a final title check to a coarse not-published check survived an offline response-contract suite, because no injected answer left the title wrong while the status stayed draft; a new partial dirty refusal cell, where the server refuses after applying a blank title but keeps the status, caught it

## Why it was hard to see

The suite covers each signal alone, and the mutant hides in the combination where the coarse signal is right and the detail is wrong.

## Fix

For each surviving mutant, add the cell where the coarse signal looks right and the checked detail is wrong, then rerun the mutant

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a mutant survives, add the cell where the coarse signal is right and the checked detail is wrong, and rerun the mutant to prove the cell kills it

## Related

[INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) [INC-0339](./INC-0339-a-mutant-of-a-shared-helper-proved-sensitivity-but-not-the-r.md)
