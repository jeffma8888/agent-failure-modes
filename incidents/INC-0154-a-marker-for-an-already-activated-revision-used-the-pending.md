---
id: INC-0154
title: A marker for an already activated revision used the pending path form
date: 2026-10-30
classes: [identity-and-keying, false-green]
severity: medium
status: fixed
---

# INC-0154 - A marker for an already activated revision used the pending path form

**Cost:** Minor: the identity checker went red on main until the edge was rewritten.

## Signature - how you recognise it

A marker was committed without running the identity checker on the exact tree.

## What happened

A lead marker for a revision whose older copy was already activated used the pending path form, and the identity checker reported a missing unlisted deletion on main until the edge was rewritten in the active path form.

## Root cause

The marker generator emitted the pending form regardless of whether the older copy was already active, and the checker was not run before the commit.

## Why it was hard to see

Both path forms look valid by eye; only the checker on the exact tree tells them apart.

## Fix

Rewrite the edge in the active path form; the marker generator now emits the active form.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the identity checker on the exact tree before committing any marker.

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md)
