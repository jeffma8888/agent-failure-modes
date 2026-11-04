---
id: INC-0565
title: A second request for a part-row driver showed that the row runner needs a case filter
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0565 - A second request for a part-row driver showed that the row runner needs a case filter

**Cost:** None. The request was sanctioned for one root and a case filter became a candidate row.

## Signature - how you recognise it

A runner cannot run one case, so people ask for private drivers.

## What happened

A tester asked, as the earlier ruling required, to run mutation reds as single cases because the coverage needs one case alone, and the row runner has no case filter. The lead sanctioned it for that root only: the unmodified harness functions and the test command on the exact spec path with an anchored, escaped case-tag filter, the driver saved with its hash quoted in each receipt, each red log showing exactly one test ran and failed at its assertion, and each restored green the full unmodified row run in the same invocation with the restore in a trap. The lead recorded that a case filter for the runner is now a candidate row, and that until it exists each request needs asking.

## Root cause

The runner lacked a feature that the coverage design needs.

## Why it was hard to see

Each private driver is a one-off that needs its own review.

## Fix

Add a case filter to the runner, and until then ask each time.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A second request for a part-row driver means the runner needs a case filter; until it has one, ask for each sanction.

## Related

[INC-0549](./INC-0549-a-reviewer-wrote-its-own-browser-only-driver-to-reach-a-muta.md) [INC-0546](./INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md)
