---
id: INC-0529
title: A full run stopped at the unit step because one test hit the runner's default five-second bound while host load rose sevenfold
date: 2026-11-02
classes: [stage-timeout]
severity: medium
status: mitigated
---

# INC-0529 - A full run stopped at the unit step because one test hit the runner's default five-second bound while host load rose sevenfold

**Cost:** The later steps of a full run did not run, and the run was not green; acceptance stood on an earlier run.

## Signature - how you recognise it

A unit test fails with a timeout at the runner's default bound, and the host load at the end of the step is many times that at its start.

## What happened

In a full run the unit step passed all but one test, so it exited 1 and the integration, server and smoke steps did not run. The failure was a test that loads the sanitized configuration, timing out at the runner's default per-test bound while the load average rose from about 13 to about 95 during the step. The unit project set no timeout. One implementer change set a 30-second per-test bound in the unit project block, accepting that a hung unit test now fails at 30 seconds.

## Root cause

The per-test bound was never chosen for the project, so the runner default applied to a test that takes seconds under load.

## Why it was hard to see

The failure is a timeout and not an assertion, and the step ending nonzero hides the steps after it.

## Fix

Set a project-level per-test bound that tolerates the load class the unit step runs in.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A per-test bound left at the runner default is a decision nobody made; set it at the project level for the load class the step runs in, and treat a default-bound timeout under load as a wasted run, not a red.

## Related

[INC-0521](./INC-0521-three-unit-tests-timed-out-at-a-short-child-process-bound-un.md) [INC-0500](./INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md)
