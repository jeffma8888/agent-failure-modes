---
id: INC-0147
title: A moved history row was silently modernized instead of staying byte identical
date: 2026-10-30
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0147 - A moved history row was silently modernized instead of staying byte identical

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A move that is described as byte identical changes a this version label.

## What happened

A historical row moved between documents was updated to the current version label during a purported byte identical move.

## Root cause

Relocation and status update were done in one edit.

## Why it was hard to see

A reader sees only the new text.

## Fix

Keep a moved history row byte identical, or carry a separately attributed status line.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Separate source-preserving relocation from attributed status changes.

## Related

[INC-0127](./INC-0127-a-document-already-at-its-hard-size-cap-had-no-room-for-the.md)
