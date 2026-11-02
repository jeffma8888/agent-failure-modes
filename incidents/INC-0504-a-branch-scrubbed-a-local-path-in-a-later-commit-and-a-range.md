---
id: INC-0504
title: A branch scrubbed a local path in a later commit, and a range scan found it still in history
date: 2026-11-02
classes: [detector-fail-open]
severity: low
status: mitigated
---

# INC-0504 - A branch scrubbed a local path in a later commit, and a range scan found it still in history

**Cost:** The merge became a squash and the branch was kept locally as the review record; nothing leaked to the pushed history.

## Signature - how you recognise it

The final tree passes a leak scan, and a scan of every commit of the range does not.

## What happened

Intermediate commits of a branch added a local home path to an evidence document, and a later commit removed it. The final tree was clean. A scan of the whole range found the path in history, and a plain merge would have carried those commits into the history that is pushed. The branch was landed as a squash whose tree equalled the merge result.

## Root cause

A final-tree check was treated as covering history, but a later commit that removes a value does not remove it from earlier commits.

## Why it was hard to see

The tree the reviewer reads is clean, and the leak exists only in commits nobody opens.

## Fix

Scan every commit of the range before merging anything that will be pushed. Squash a branch whose intermediate commits leak, and keep the branch locally as the review record.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scan every commit of a range, not only the final tree, before merging anything that will be pushed; a scrub in a later commit does not clean history.

## Related

[INC-0437](./INC-0437-evidence-receipts-leaked-absolute-paths-into-branch-history.md) [INC-0436](./INC-0436-a-squash-recipe-equated-the-landing-tree-with-a-stale-branch.md)
