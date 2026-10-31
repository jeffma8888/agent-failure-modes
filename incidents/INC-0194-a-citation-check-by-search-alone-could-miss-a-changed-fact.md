---
id: INC-0194
title: A citation check by search alone could miss a changed fact
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0194 - A citation check by search alone could miss a changed fact

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A moved range was matched by text while its behavior changed.

## What happened

A version bump moved pinned-source citations, and a search finds the text but cannot show whether the text around it changed.

## Root cause

A version bump moved pinned-source citations, and a search finds the text but cannot show whether the text around it changed.

## Why it was hard to see

The match looks like confirmation.

## Fix

Compare the cited ranges by diff, not only by search

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compare cited ranges by diff when a version bump moves pinned-source citations

## Related

[INC-0185](./INC-0185-rename-detection-reported-a-false-rename-in-a-merge.md)
