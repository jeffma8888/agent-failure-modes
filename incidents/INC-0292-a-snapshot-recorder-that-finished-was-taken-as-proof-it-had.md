---
id: INC-0292
title: A snapshot recorder that finished was taken as proof it had collected
date: 2026-11-01
classes: [detector-fail-open, observability]
severity: medium
status: fixed
---

# INC-0292 - A snapshot recorder that finished was taken as proof it had collected

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A recorder reached its completion message while observations were missing.

## What happened

offsets were saved but never used, failed root resolution was skipped as a root, an empty inventory looked the same as a failed traversal, and completion was always reached

## Root cause

offsets were saved but never used, failed root resolution was skipped as a root, an empty inventory looked the same as a failed traversal, and completion was always reached

## Why it was hard to see

Empty output is also the expected output of a quiet window, so failure looks like success.

## Fix

Record a per-observation status and expectation verdict, treat an unreadable required source as an error, and fail the snapshot on missing evidence

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Completion is not collection; require per-observation status and distinguish empty from failed

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md)
