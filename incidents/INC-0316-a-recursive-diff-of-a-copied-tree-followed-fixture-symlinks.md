---
id: INC-0316
title: A recursive diff of a copied tree followed fixture symlinks into the host
date: 2026-11-01
classes: [tooling-paths, test-isolation]
severity: medium
status: fixed
---

# INC-0316 - A recursive diff of a copied tree followed fixture symlinks into the host

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A copy check wandered outside the copied tree and hit sockets and pipes.

## What happened

a fixture held symlinks to host temporary space, and a recursive comparison of the copied folder followed them and crawled host sockets and pipes

## Root cause

a fixture held symlinks to host temporary space, and a recursive comparison of the copied folder followed them and crawled host sockets and pipes

## Why it was hard to see

The comparison is correct for a plain tree, and the fixture's links point outside it.

## Fix

Verify copied trees with a manifest that does not follow symlinks, and make fixtures point symlinks at targets the fixture owns

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify copied trees with a manifest that does not follow symlinks; fixtures point symlinks at fixture-owned targets

## Related

[INC-0293](./INC-0293-the-before-state-was-not-preserved-before-an-operator-edit.md) [INC-0295](./INC-0295-a-pure-move-onto-an-existing-path-was-read-from-the-diff-s-r.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) [INC-0368](./INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md)
