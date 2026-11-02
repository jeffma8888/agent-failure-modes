---
id: INC-0368
title: A new worktree symlinked its dependency trees to another worktree's, and the package manager relinked through them
date: 2026-11-01
classes: [concurrency, tooling-paths]
severity: medium
status: fixed
---

# INC-0368 - A new worktree symlinked its dependency trees to another worktree's, and the package manager relinked through them

**Cost:** Minor: found within minutes; the other worktree's links, shims and state files had to be restored and compared.

## Signature - how you recognise it

A package manager command in one worktree changed the dependency links of another worktree.

## What happened

a new worktree linked its three dependency roots (root, application, shared package) to another worktree's trees to avoid a copy. Its first package-manager command ran the tool's automatic freshness check, which relinked through those links: it retargeted the other worktree's workspace package link into the new worktree, re-hoisted two packages and rewrote shims and state files. The lead found it within minutes

## Root cause

two worktrees shared one writable dependency tree by symlink, and the package manager's own freshness check treats the tree as its own to repair

## Why it was hard to see

The command was an ordinary one, the mutation happened inside the tool's automatic check rather than in anything the engineer typed, and the damaged worktree kept working.

## Fix

The lead restored every link to match a clean sibling tree (1564 links compared) and gave the new worktree private copy-on-write clones with rewritten shim paths

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never share a dependency tree between worktrees by symlink; give each worktree a private clone; never run the package manager unless the exact command is authorized; keep the verify-before-run settings off for every child; compare the full link inventory against a clean sibling after any suspected mutation

## Related

[INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0316](./INC-0316-a-recursive-diff-of-a-copied-tree-followed-fixture-symlinks.md) [INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) [INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md)
