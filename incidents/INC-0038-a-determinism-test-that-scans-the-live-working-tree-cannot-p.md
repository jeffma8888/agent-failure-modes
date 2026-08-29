---
id: INC-0038
title: A determinism test that scans the live working tree cannot pass while another writer edits it
date: 2026-08-28
classes: [test-isolation, concurrency]
severity: medium
status: open
---

# INC-0038 - A determinism test that scans the live working tree cannot pass while another writer edits it

**Cost:** Two tests intermittently red on an otherwise green suite, with no defect in the code under test. The cost is diagnostic: a red suite that is not evidence of a regression teaches a reader to ignore the suite, and it blocks a release gate that is supposed to mean something.

## Signature - how you recognise it

A test asserting that two consecutive runs produce identical output fails in the full suite and passes in isolation. The failure moves between runs and correlates with another session's file timestamps rather than with anything that changed under test.

## What happened

A tool's output was asserted reproducible by scanning a repository twice and comparing. The repository scanned was the tool's OWN checkout - the live, mutable working tree. When a second agent or a human saved a file between the two scans, the scan legitimately reported different results, and the test failed: correctly reporting a change in the world as a failure of the code.

## Root cause

The test's fixture is a shared mutable resource that no participant has agreed to hold still. Determinism is a property of a function over a FIXED input; asserting it over an input another writer owns tests the writers, not the function.

## Why it was hard to see

It passes in isolation, which is the signature engineers read as flakiness to be retried rather than as a design fault. It also passes essentially always on a single-writer machine, so it can sit in a suite for months and first fail only once concurrency arrives - at which point the failure looks like a regression in whatever changed most recently.

## Fix

Scan a fixture the test OWNS: build a small repository in a temporary directory, or copy a fixed file set, so the input cannot change between the two runs. If the live tree genuinely must be the subject, snapshot it once and run both passes against the snapshot, then assert the snapshot's own hash is unchanged at the end - so the test can report 'the world moved' distinctly from 'the output differs'.

## Verification

Not fixed. Both tests were confirmed to pass in isolation and to fail in the full suite while a second writer's file timestamps fell inside the failing window, which establishes the mechanism but not the repair. Status is open deliberately: the diagnosis is recorded before the fix rather than after.

## Transferable rule

> Determinism is a property of a function over a FIXED input. A test that scans the live working tree twice and compares is really asserting that no other writer touched the tree, so it tests the writers, not the code - and it passes in isolation, which reads as flakiness. Give the test a fixture it owns, or snapshot the input once and assert the snapshot is unchanged.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - the scan-determinism tests that take the repository root itself as their scan target, so the fixture is the live mutable checkout.

## Related

[INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0022](./INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) [INC-0023](./INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md) [INC-0031](./INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md)
