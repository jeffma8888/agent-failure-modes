---
id: INC-0511
title: A harness test failed because another run's orphan database vanished mid-test, so the test depended on state it did not own
date: 2026-11-02
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0511 - A harness test failed because another run's orphan database vanished mid-test, so the test depended on state it did not own

**Cost:** One full-suite run was spent on an environmental red, and a rerun was needed.

## Signature - how you recognise it

A cleanliness assertion over a shared server sees a resource disappear between its baseline and its end.

## What happened

In the second full-suite run one harness step failed: a cleanliness assertion saw a test database vanish between its baseline and its end. That database was an orphan of the previous run, which had timed out, and it was removed during the second run, most likely by the garbage collection the test exercises. The red was environmental and not a code defect. A second orphan remained and was reported and left in place.

## Root cause

The test took a baseline over shared state and so depended on every other run leftovers.

## Why it was hard to see

The failure message names a real change in the shared state, so it looks like a product defect until the orphan's origin is traced.

## Fix

Treat a red caused by another run leftover as environmental, rerun on the next admitted slot, and report the leftover without removing it.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test must not assert on state it did not create; compare only the names the test itself made.

## Related

[INC-0361](./INC-0361-a-test-s-teardown-emptied-a-shared-server-database-and-a-gat.md) [INC-0436](./INC-0436-a-squash-recipe-equated-the-landing-tree-with-a-stale-branch.md)
