---
id: INC-0436
title: A squash recipe equated the landing tree with a stale branch tree and would have dropped later main work
date: 2026-11-02
classes: [vcs-destruction]
severity: low
status: fixed
---

# INC-0436 - A squash recipe equated the landing tree with a stale branch tree and would have dropped later main work

**Cost:** No work was lost; the recipe was corrected before the merge.

## Signature - how you recognise it

A landing recipe that would have silently removed work already on main.

## What happened

a squash landing recipe required the landing commit's tree to equal the branch's final tree, but the branch predated later main landings, so that tree would have dropped main content; a reviewer caught the seam and the lead withdrew the clause: the squash tree must equal the conflict-free merge result, printed by the merge-tree command with both commit ids pinned in the message, and a stale tree is never reused after main moves

## Root cause

the recipe compared the landing with the branch alone, which ignores everything main gained after the branch point

## Why it was hard to see

Tree equality sounds like the strongest check and was against the wrong tree.

## Fix

compare the landing tree with the merge result of the current main and the branch head, never with the branch tree, and rebuild when main moves

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A squash landing tree must equal the merge result of the pinned main and the branch head, never the branch tree; rebuild when main moves

## Related

[INC-0410](./INC-0410-the-lead-re-merged-the-full-candidate-itself-rather-than-que.md) [INC-0335](./INC-0335-a-pinned-base-digest-froze-a-file-that-a-later-row-split-nee.md)
