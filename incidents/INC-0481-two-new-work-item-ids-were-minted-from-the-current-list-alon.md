---
id: INC-0481
title: Two new work item ids were minted from the current list alone, and both had already been used by merged work
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0481 - Two new work item ids were minted from the current list alone, and both had already been used by merged work

**Cost:** Minor: found when a branch creation failed; the new items were renamed and earlier mentions rewritten.

## Signature - how you recognise it

A checker that read only the current list passed ids that history had already used.

## What happened

A coordinator minted two new work item ids by reading only the current backlog list. Both ids had already been used by merged work, one in branch names and merge subjects and one in a regression branch. The backlog checker passed because the current list did not hold the old ids. The collision surfaced only when an engineer's branch creation failed on an existing branch name.

## Root cause

Ids were checked against the current list only, while earlier ids lived on in branch names, commit subjects and plan text.

## Why it was hard to see

The checker passed, so there was no signal until a tool tried to reuse an existing name.

## Fix

Rename the new items to the next free ids, rewrite earlier mentions, leave the old branches as history, and before minting an id search every place ids have lived.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before minting an id, check every place ids have ever lived (branch names, commit subjects, plan text), not only the current list; a checker that reads only the current list cannot catch reuse.

## Related

[INC-0079](./INC-0079-a-second-writer-reused-a-shared-registry-s-batch-name-and-it.md) [INC-0140](./INC-0140-a-known-red-was-listed-before-checking-the-scan-roots-of-the.md)
