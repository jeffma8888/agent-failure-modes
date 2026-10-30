---
id: INC-0123
title: After activation a registry line named a pending path that no longer existed, and a verifier flagged it
date: 2026-10-30
classes: [stale-module, tooling-paths]
severity: medium
status: fixed
---

# INC-0123 - After activation a registry line named a pending path that no longer existed, and a verifier flagged it

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

A verifier reports a missing path that was legitimately moved at activation.

## What happened

After activation, a registry line named a pending path that no longer existed, and a verifier flagged it instead of following history.

## Root cause

The verifier assumed paths in the registry always exist on disk.

## Why it was hard to see

The path is gone for a valid reason, so the flag looks like a real failure.

## Fix

Resolve the line through history rather than flag it.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A verifier must follow moves through history, not require the old path to exist.

## Related

[INC-0101](./INC-0101-a-later-row-overwrote-a-file-that-was-already-active.md)
