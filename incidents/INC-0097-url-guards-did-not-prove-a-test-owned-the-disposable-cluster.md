---
id: INC-0097
title: URL guards did not prove a test owned the disposable cluster, and shared state was not restored on failure
date: 2026-10-30
classes: [test-isolation, identity-and-keying]
severity: medium
status: fixed
---

# INC-0097 - URL guards did not prove a test owned the disposable cluster, and shared state was not restored on failure

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A test destroys or mutates state after checking only that the URL looks safe.

## What happened

URL guards were used as proof that a test owned a disposable cluster, and shared state was not restored when the test failed.

## Root cause

A URL pattern shows what a target looks like, not who owns it.

## Why it was hard to see

The guard passes in the normal run, and the missing restore shows only after a failure.

## Fix

Prove ownership from a recorded set of created resources, and restore shared state even when the test fails.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Ownership comes from what the test created; restoration belongs in teardown that runs on failure.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
