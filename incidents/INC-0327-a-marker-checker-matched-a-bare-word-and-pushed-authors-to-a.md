---
id: INC-0327
title: A marker checker matched a bare word and pushed authors to a workaround
date: 2026-11-01
classes: [detector-fail-closed, tooling-paths]
severity: medium
status: fixed
---

# INC-0327 - A marker checker matched a bare word and pushed authors to a workaround

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A checker reported many focused-test markers that were only object keys.

## What happened

a static checker for focused-test markers rejected the bare word fit even as an object key, so the author quoted the key to get past the false positive instead of fixing the checker

## Root cause

a static checker for focused-test markers rejected the bare word fit even as an object key, so the author quoted the key to get past the false positive instead of fixing the checker

## Why it was hard to see

The workaround passes the check, so the false positive hides and every later author repeats it.

## Fix

Anchor the marker check on call syntax, not a bare word, and when a false positive forces a workaround, record it and fix the checker instead of spreading workarounds

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Anchor a marker check on call syntax, not a bare word; when a checker false positive forces a workaround, record it and fix the checker rather than spreading workarounds

## Related

[INC-0287](./INC-0287-an-oracle-that-matches-a-substring-or-a-loose-boundary-can-b.md) [INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md)
