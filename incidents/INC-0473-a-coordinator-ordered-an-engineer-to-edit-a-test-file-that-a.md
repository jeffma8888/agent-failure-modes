---
id: INC-0473
title: A coordinator ordered an engineer to edit a test file that a QA identity manifest pins, and the identity gate refused the run before any database
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0473 - A coordinator ordered an engineer to edit a test file that a QA identity manifest pins, and the identity gate refused the run before any database

**Cost:** Minor: the gate stopped the run in 1.5 seconds, before any database, and the change had to be rerouted.

## Signature - how you recognise it

An ordered test edit made the identity gate refuse the run before it started.

## What happened

A coordinator ordered an engineer to edit a browser spec so every request-context call sends an Origin header. The spec is pinned by the terminal digest of a QA owned test root, so the test only change made the admitted run exit 1 at identity selection, before any database, because the active spec no longer equalled the pinned digest. The engineer followed the order exactly and stopped correctly.

## Root cause

The order did not check whether the file was identity pinned, and an engineer edit cannot change pinned bytes.

## Why it was hard to see

The edit is small and correct as a test fix, so nothing about it looks like an identity change until the gate runs.

## Fix

Route the change through a successor root authored by a QA identity, who reviews it as a test correctness fix that must not weaken the oracle and adopts its bytes exactly; a non author checks it, the coordinator lands the supersession record, and the engineer merges and reruns on a new admission.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ordering a test edit, check whether the file is pinned by a QA identity manifest; if it is, route the change through a successor root authored by a QA identity, not an engineer edit.

## Related

[INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md) [INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) [INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md)
