---
id: INC-0403
title: The identity checker allowed a successor root's new path with no predecessor line, and a marker maps only replaced paths
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0403 - The identity checker allowed a successor root's new path with no predecessor line, and a marker maps only replaced paths

**Cost:** A marker with an invented predecessor line would have claimed a replacement that did not occur.

## Signature - how you recognise it

A successor root added a path that had no earlier copy, and it was unclear whether a marker line was owed.

## What happened

the identity checker allows a successor root's new path with no predecessor line, because a marker maps only the paths it replaces

## Root cause

the rule for new paths in a successor was not written down

## Why it was hard to see

A marker that lists extra paths looks safe but asserts a replacement that never happened.

## Fix

Give a marker only for replaced paths; a new path in a successor needs no predecessor line

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A marker maps only replaced paths; a successor's new path needs no predecessor line

## Related

[INC-0397](./INC-0397-a-pending-root-whose-supersession-line-said-review-pending-f.md) [INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md)
