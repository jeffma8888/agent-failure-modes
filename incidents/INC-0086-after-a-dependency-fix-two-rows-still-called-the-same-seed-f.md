---
id: INC-0086
title: After a dependency fix, two rows still called the same seed function with different payloads
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0086 - After a dependency fix, two rows still called the same seed function with different payloads

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A fix is verified by name, but the same seed function is called with different arguments elsewhere.

## What happened

A second audit pass found that two rows called one seed function for different payloads, so a fix that satisfied one did not cover the other.

## Root cause

The re-check looked at the fix, not at the exact fixture or seed-call line in each row.

## Why it was hard to see

Matching function names suggest identical data.

## Fix

After a dependency fix, re-read the exact fixture or seed-call line in each affected row.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify the call site and arguments, not only the function name, after a dependency change.
