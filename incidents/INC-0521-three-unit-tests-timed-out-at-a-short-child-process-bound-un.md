---
id: INC-0521
title: Three unit tests timed out at a short child-process bound under parallel load and passed in isolation
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: mitigated
---

# INC-0521 - Three unit tests timed out at a short child-process bound under parallel load and passed in isolation

**Cost:** An acceptance run showed three extra failures and needed an isolated rerun to classify them.

## Signature - how you recognise it

Tests that spawn a child process fail with a spawn timeout at a five-second bound only while the host is loaded.

## What happened

In an acceptance run of the whole unit tier, eight tests failed: the five known baseline cases and three new ones, all spawn timeouts at a five-second bound, in fixtures that use a temporary root and do not depend on the repository. Rerun alone after waiting for the load to fall under the class limit, the two files passed. The acceptance was ruled equal to the baseline apart from the known timeout class under load.

## Root cause

A short fixed bound on child-process tests assumes an idle host.

## Why it was hard to see

The failures look like regressions in a run with new merges, and only an isolated rerun separates load from code.

## Fix

Rerun the timed-out files alone under an admitted load and record the reading, and change the bound only where the file is not a pinned root.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A short child-process bound fails under parallel load while the test is correct; classify such a timeout by an isolated rerun, and give child-process tests a bound that tolerates the load class they run in.

## Related

[INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) [INC-0500](./INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md)
