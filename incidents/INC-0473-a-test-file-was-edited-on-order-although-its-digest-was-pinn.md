---
id: INC-0473
title: A test file was edited on order although its digest was pinned by the test authors, and the integrity gate refused the run before it started
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0473 - A test file was edited on order although its digest was pinned by the test authors, and the integrity gate refused the run before it started

**Cost:** Minor: the gate stopped the run in 1.5 seconds, before any database, and the change had to be rerouted.

## Signature - how you recognise it

An ordered test edit made the integrity gate refuse the run before it started.

## What happened

A coordinator ordered an engineer to edit a browser test so every request sends an Origin header. The test file is pinned by a digest recorded in a manifest that the test authors own, so the edit made the approved run exit 1 at its integrity check, before any database was touched, because the active file no longer matched the pinned digest. The engineer followed the order exactly and stopped correctly.

## Root cause

The order did not check whether the file was pinned by a digest, and an edit by anyone but the owner cannot change pinned bytes.

## Why it was hard to see

The edit is small and correct as a test fix, so nothing about it looks like an identity change until the gate runs.

## Fix

Route the change through a successor version authored by the test owner or another test author, who reviews it as a correctness fix that must not weaken the check and adopts its bytes exactly; a second person checks it, the coordinator records the replacement, and the engineer merges and reruns.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ordering an edit to a test file, check whether a digest manifest pins it; if it does, route the change through a successor version authored by a test author, not a direct edit.

## Related

[INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md) [INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) [INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md)
