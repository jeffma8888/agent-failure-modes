---
id: INC-0185
title: Rename detection reported a false rename in a merge
date: 2026-10-30
classes: [vcs-destruction, identity-and-keying]
severity: medium
status: fixed
---

# INC-0185 - Rename detection reported a false rename in a merge

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A merge showed a rename and delete that did not happen.

## What happened

When two branches both activated the same pending root, rename detection paired the deleted pending copy with the near-identical new revision copy.

## Root cause

Similarity is not identity.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Keep the new revision file with main bytes and confirm the blob against main.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not accept either side of a reported rename; confirm the blob against main.

## Related

[INC-0175](./INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md)
