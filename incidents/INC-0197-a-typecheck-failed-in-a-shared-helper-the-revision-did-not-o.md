---
id: INC-0197
title: A typecheck failed in a shared helper the revision did not own
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0197 - A typecheck failed in a shared helper the revision did not own

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The red was in code the revision could not touch.

## What happened

A typecheck over pending destinations failed in a shared active helper the revision does not own, which invited an edit or a suppression in the consumer root.

## Root cause

A typecheck over pending destinations failed in a shared active helper the revision does not own, which invited an edit or a suppression in the consumer root.

## Why it was hard to see

The failure appears in the consumer run.

## Fix

Route it to that helper own row as a revision; never edit or suppress it inside the consumer root

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Fix a shared helper in its own row, never inside the consumer root

## Related

[INC-0157](./INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md)
