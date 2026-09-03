---
id: INC-0040
title: A guard that asserts a lifecycle stage fails at exactly the moment it was written to protect
date: 2026-08-30
classes: [false-green, test-isolation, detector-fail-open]
severity: medium
status: fixed
---

# INC-0040 - A guard that asserts a lifecycle stage fails at exactly the moment it was written to protect

**Cost:** A publication-safety gate was green on every local run for the entire life of the project and went red on the FIRST run after the artifact was published - the one moment its verdict actually mattered.

## Signature - how you recognise it

A safety test has never once failed, and the state it forbids is a state on the project's own roadmap. It fails for the first time immediately after a milestone.

## What happened

A pre-publication check required the repository to have NO git remote, as a proxy for 'this has not been published yet'. Having no remote is a STAGE in a repository's life, not a property of it. The check therefore passed forever locally and failed on the first remote CI run, because publishing was the intended destination all along.

## Root cause

The guard asserted a schedule rather than an invariant. Any guard whose forbidden state is one the project intends to REACH is guaranteed to fail exactly when the guarded event happens - which is the worst possible moment to discover a gate was mis-specified, because the failure arrives mixed in with the milestone's other noise.

## Why it was hard to see

The test is green, cheap and looks like diligence, and its name describes a real risk. Only its PREDICATE is wrong, and a predicate that is never violated locally produces no evidence at all - a check never seen returning false has not been tested.

## Fix

Replace the stage assertion with the property one level down: not 'no remote' but 'no credential in any remote' - every fetch and push URL must be credential-free HTTPS or Git-only SSH to a public host - with two-sided tests for unsafe local paths, private hosts, embedded credentials, unexpected schemes, raw IPs and SSH usernames.

## Verification

The replacement is two-sided by construction: each unsafe form has a test asserting the guard FIRES, and each safe form a test asserting it stays silent. The new predicate is also true both before and after publication, so the milestone no longer changes the verdict.

## Transferable rule

> Write down the state your guard FORBIDS, then ask whether the project intends to REACH that state. If it does, the guard is asserting a schedule, not a safety property, and it will fail precisely when the guarded event happens. The invariant worth protecting sits one level down: not 'no remote' but 'no credential in a remote'.

## Related

[INC-0022](./INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) [INC-0038](./INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md)
