---
id: INC-0482
title: Tests added by a branch in the server tier were never run before the merge, and the full suite failed on them afterwards
date: 2026-11-02
classes: [false-green]
severity: medium
status: open
---

# INC-0482 - Tests added by a branch in the server tier were never run before the merge, and the full suite failed on them afterwards

**Cost:** The merged main was red at one test tier and further merges were frozen until a fix landed.

## Signature - how you recognise it

Tests nobody ran before the merge failed on their first execution after it.

## What happened

A branch added engineer written tests in the server tier. The branch acceptance run covered its unit tests, its integration tests and one browser case, but not those server tier files, so they were never executed before the merge. The full suite after the merge was their first run. One test failed on its own fixture, because the create was refused by a size check before the assertion was reached, and a second, older test then failed too. A leftover file from the refused create is a hypothesis, not a finding.

## Root cause

The branch acceptance run did not include every test file the branch added, so the first execution of some files happened after the merge.

## Why it was hard to see

The acceptance run was green and complete for the tiers it covered, so nothing signalled that other added files had not run.

## Fix

Fix forward on the merged branch with further merges frozen, and run every test file a branch adds or changes, in its own tier, in the branch acceptance run before the merge.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before a merge, the branch acceptance run must run every test file the branch adds or changes, in its own tier; a full run after the merge is a backstop, not the first execution.

## Related

[INC-0447](./INC-0447-tests-authored-but-never-executed-passed-acceptance-and-the.md) [INC-0477](./INC-0477-a-browser-test-failed-at-its-first-api-read-and-the-next-run.md)
