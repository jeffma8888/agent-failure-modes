---
id: INC-0014
title: A revert-on-failure loop destroys uncommitted human work in a shared tree
date: 2026-08-04
classes: [vcs-destruction]
severity: critical
status: mitigated
---

# INC-0014 - A revert-on-failure loop destroys uncommitted human work in a shared tree

**Cost:** Potential (avoided): uncommitted human work sat in a tree the loop was about to run. The failure path would have destroyed it with `git reset --hard origin/main`.

## Signature - how you recognise it

A loop is enabled that commits from a working directory where another writer has uncommitted changes. The loop's failure path is a full reset to the remote head.

## What happened

A build loop's failure handler was `git reset --hard origin/main && git clean -fd` - a fine idempotent reset for the loop's own tree, but catastrophic if any human uncommitted work happened to be in the same tree. A parallel session had staged design edits there.

## Root cause

The loop's revert-to-remote is a legitimate safety mechanism for the LOOP's state. It cannot distinguish loop-authored dirt from human-authored work-in-progress: both are 'uncommitted files under this tree'.

## Why it was hard to see

The reset is designed to be aggressive. It has no notion of ownership.

## Fix

The correct protection is a per-team STOP sentinel that pauses ONE team without disabling it. The sentinel must name (a) the owner, (b) the exact files at risk, (c) an explicit lift condition, (d) whether a dispatcher restart is required to lift it. Sentinels are polled every round (instant effect); the `enabled` flag is read only at dispatcher startup (needs a restart). Never take an ownership decision by editing the enabled flag; use STOP to pause and enabled to remove.

## Verification

Before lifting any protective STOP, re-verify the stated lift condition in the SAME command that removes the STOP (e.g. `git status --porcelain` empty AND HEAD == origin/main immediately before `rm STOP`). The tree can go dirty again between a survey and the action.

## Transferable rule

> A loop's revert-to-remote cannot distinguish loop dirt from human work-in-progress. Guard shared trees with a per-team STOP sentinel that names owner, files at risk, lift condition and whether restart is needed. Sentinels are polled every round; the enabled flag needs a restart. Verify the lift condition in the SAME command that removes it.

## Related

[INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0013](./INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md)
