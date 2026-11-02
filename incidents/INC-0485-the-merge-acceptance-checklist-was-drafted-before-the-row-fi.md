---
id: INC-0485
title: The merge acceptance checklist was drafted before the row finished, and reading it found a test change that the merge would have turned red
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0485 - The merge acceptance checklist was drafted before the row finished, and reading it found a test change that the merge would have turned red

**Cost:** None incurred: the owed change was found by reading before the merge, at the price of one extra assigned job.

## Signature - how you recognise it

A source change altered a seed record, while a unit test still asserted the old shape.

## What happened

A branch changed its seed so the first user is created with a name and roles. A unit test on the seed still expected only an email and a password. Nobody had run the whole unit tier on the branch, so the mismatch would have surfaced as a red run after the merge. A checklist for the merge, drafted while the row was still open, predicted the failure by reading the changed source against the tests that assert on it. A second latent weakness in the same test file, report assertions not scoped to the staff key, was folded into the same repair.

## Root cause

The row changed a seed shape without a step that finds the tests asserting on it, and the whole unit tier was first due to run at the merge.

## Why it was hard to see

The row passed its own checks, and the stale test lived in a tier the row did not run, so nothing signalled the mismatch until someone read both files together.

## Fix

Assign the owed test change to the branch engineer before the merge, draft the exact replacement text, have a second person review it, apply it on the branch, and run the whole unit tier on the branch.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Draft the merge acceptance checklist while the row is still open, and for each source change read the tests that assert on it, so owed test changes are found before the merge turns the full run red.

## Related

[INC-0482](./INC-0482-tests-added-by-a-branch-were-never-run-before-the-merge-and.md) [INC-0477](./INC-0477-a-browser-test-failed-at-its-first-request-and-after-that-wa.md)
