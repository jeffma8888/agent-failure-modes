---
id: INC-0167
title: A revision marker added a second edge to bytes the previous marker already claimed
date: 2026-10-30
classes: [identity-and-keying, false-green]
severity: medium
status: fixed
---

# INC-0167 - A revision marker added a second edge to bytes the previous marker already claimed

**Cost:** Minor: caught on a scratch clone before the commit.

## Signature - how you recognise it

The identity check went red with an old digest mismatch on a marker that looked complete.

## What happened

A marker for a new revision takes its edge from the newest pending earlier copy when one exists; an extra active-path edge to the same active bytes that the earlier marker already claims turned the identity check red.

## Root cause

The marker author added an edge for the active bytes without noticing the earlier marker claimed them.

## Why it was hard to see

Both edges look valid alone and the clash appears only in the whole tree.

## Fix

Drop the extra edge; take the edge from the newest pending earlier copy.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the identity checker on a scratch clone before committing a marker, and take the edge from the newest pending earlier copy.

## Related

[INC-0154](./INC-0154-a-marker-for-an-already-activated-revision-used-the-pending.md)
