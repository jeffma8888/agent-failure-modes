---
id: INC-0013
title: add-then-commit is a shared-index race; use a path-limited commit
date: 2026-08-03
classes: [vcs-destruction, concurrency]
severity: high
status: fixed
---

# INC-0013 - add-then-commit is a shared-index race; use a path-limited commit

**Cost:** An entire in-flight iteration's changeset shipped under a human's out-of-band commit message. Non-destructive but history mislabeled.

## Signature - how you recognise it

You ran `git add <paths>` followed by a separate `git commit` and the resulting commit contains files you never touched. Diff against your parent shows the loop's whole iteration.

## What happened

A human ran add-then-commit-then-push in one shell line while a loop's final step was live. In the window between the add and the commit, the loop ran its own `git add -A`. The human's PATHLESS `git commit` then swept the entire loop iteration into the human's commit under the human's subject and pushed it. All content preserved; history mislabeled.

## Root cause

The git index is process-shared state and a pathless commit commits whatever is staged AT THAT INSTANT, not what you originally staged. Any other writer to the same index between your add and your commit contributes its files to your commit.

## Why it was hard to see

There is no error and every test still passes. The failure is invisible unless you diff the commit against its parent and notice files you did not touch.

## Fix

For any out-of-band write to a loop-owned repo, name the paths on the COMMIT itself, not on a separate add: `git commit -m 'msg' -- <paths>`. This bypasses the index entirely. Never amend or force-push to fix the mislabel while the loop is live (non-ff hazard) - either accept the cosmetic mess or repair during a quiescent window.

## Verification

The pattern was proven live: a subsequent out-of-band edit landed as a single-file commit even while the loop's final step was mid-run.

## Transferable rule

> The git index is process-shared: a pathless commit takes whatever is staged at that instant, not what you staged. For any out-of-band write to a repo another writer touches: name the paths on the commit itself (`git commit -m 'msg' -- <paths>`) rather than doing add-then-commit. Do not force-push while the loop is live.

## Related

[INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md)
