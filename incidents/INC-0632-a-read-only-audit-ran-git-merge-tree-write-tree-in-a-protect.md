---
id: INC-0632
title: A read-only audit ran git merge-tree --write-tree in a protected checkout; refs, index and worktree stayed clean while loose objects were written
date: 2026-11-07
classes: [vcs-destruction, false-green]
severity: medium
status: mitigated
---

# INC-0632 - A read-only audit ran git merge-tree --write-tree in a protected checkout; refs, index and worktree stayed clean while loose objects were written

**Cost:** An existing repository's object database was changed during a read-only audit. Without a pre-write inventory, the exact objects newly introduced by this operation cannot be identified reliably, and precise reversal has not been established. Cleanup was withheld, so the mutation stands as a process violation.

## Signature - how you recognise it

A read-only task includes git merge-tree --write-tree (or another command that writes objects), and the only post-check is a clean status and an unchanged HEAD.

## What happened

A delegated audit was told not to write to an existing checkout. To test whether two branches would merge, the auditor ran git merge-tree --write-tree there. The command leaves HEAD, refs, index and worktree alone, but it is an object-writing operation: it writes or reuses merge objects in the git directory, and each call need not add both new trees and new blobs. The auditor disclosed it, and the lead found a clean status and the same HEAD. The technical result was usable, but the rule had still been broken.

## Root cause

The auditor classified the command by visible worktree and ref changes instead of all state it writes. The brief forbade all writes to the existing checkout; it lacked an explicit object-database reminder, but that did not authorize object writes. A clean status and unchanged HEAD did not test the full boundary.

## Why it was hard to see

The merge result looked like a dry run, status stayed clean, and git does not label the object write. Without a pre-write inventory, a clean status cannot show which objects are new, and existing objects may already have been present.

## Fix

Make the existing all-write prohibition explicit about the Git object database. Reconstruct hypothetical merges only in newly isolated scratch clones, with source checkouts read-only. Protected-repository mutations require separate explicit authorization; do not infer it from clean status or an inventory. Disclose violations, do not prune or clean unknown objects, and do not claim reversal or retroactive permission.

## Verification

Verified: the lead saw an unchanged HEAD and a clean tracked and untracked state afterwards. Not verified: which objects were newly introduced, since no earlier inventory exists, or that the write can be reversed. Technical validation of the result is not process compliance.

## Transferable rule

> Classify Git commands by all state they write, not clean status. Run object-writing analysis only in a newly isolated scratch clone. Protected-repository writes need separate explicit authorization; an inventory grants no permission and does not prove reversibility.

## Related

[INC-0324](./INC-0324-a-periodic-status-sweep-took-the-index-lock-of-a-teammate-s.md) [INC-0600](./INC-0600-two-branches-each-green-alone-with-a-clean-merge-tree-went-r.md) [INC-0486](./INC-0486-an-approval-on-main-was-not-an-ancestor-of-the-branch-that-n.md)
