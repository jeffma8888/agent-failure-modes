---
id: INC-0204
title: A precommit check reported a merge-brought approval as unreachable
date: 2026-10-30
classes: [identity-and-keying, false-green]
severity: medium
status: fixed
---

# INC-0204 - A precommit check reported a merge-brought approval as unreachable

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The check read the wrong commit.

## What happened

A precommit identity check that reads HEAD reported a merge-brought approval as unreachable during the merge.

## Root cause

A precommit identity check that reads HEAD reported a merge-brought approval as unreachable during the merge.

## Why it was hard to see

The approval becomes reachable only once the merge is committed.

## Fix

Judge reachability on the committed two-parent merge; treat the precommit note as a known checker limit, not a reason to split the merge

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Judge reachability on the committed merge, not on the precommit state

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md)
