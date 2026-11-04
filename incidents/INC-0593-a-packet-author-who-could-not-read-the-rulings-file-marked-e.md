---
id: INC-0593
title: A packet author who could not read the rulings file marked every claim resting on it, so the recheck knew what to verify
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0593 - A packet author who could not read the rulings file marked every claim resting on it, so the recheck knew what to verify

**Cost:** None. The recheck was scoped to the marked claims.

## Signature - how you recognise it

A packet states ruling-dependent facts that its author could not check against the source.

## What happened

The author of a packet could not read the lead rulings file and marked every claim that rests on it. The recheck assignment then named exactly which claims to verify against the rulings, instead of assuming they were checked or rechecking everything.

## Root cause

The author had no access to one source the packet depends on.

## Why it was hard to see

Unmarked claims from an unread source read as verified.

## Fix

Mark each claim resting on an unreadable source, and have the recheck verify those claims against it.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When you cannot read a source, mark every claim that rests on it so the next checker knows what to verify.

## Related

[INC-0538](./INC-0538-a-dispatch-draft-marked-every-unsourced-value-for-the-lead-t.md)
