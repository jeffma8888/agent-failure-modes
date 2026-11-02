---
id: INC-0340
title: A fixture that linked the host dependency tree let the package manager rewrite it
date: 2026-11-01
classes: [test-isolation, tooling-paths]
severity: medium
status: fixed
---

# INC-0340 - A fixture that linked the host dependency tree let the package manager rewrite it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A fixture's package manager run pruned the linked host dependency tree and turned 11 failures into 51.

## What happened

two fixtures linked the source checkout's dependency folder into a temporary folder with an empty manifest and ran the package manager's exec; its default dependency check before exec pruned the linked tree, removing every root dependency link mid-run; runs under a parent exec were safe only because the parent passes the check-off setting to children

## Root cause

two fixtures linked the source checkout's dependency folder into a temporary folder with an empty manifest and ran the package manager's exec; its default dependency check before exec pruned the linked tree, removing every root dependency link mid-run; runs under a parent exec were safe only because the parent passes the check-off setting to children

## Why it was hard to see

The link makes the fixture work, and the damage lands in the host tree, which looks like a growing set of unrelated failures.

## Fix

Restore offline from the frozen lockfile, stop running the tier until the fixture is hermetic, and fix the payload through a pending root

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never link a writable host dependency tree into a fixture that runs the package manager; if unavoidable, turn auto-install off explicitly in the fixture environment and add a guard that fails when the host tree's listing changes

## Related

[INC-0316](./INC-0316-a-recursive-diff-of-a-copied-tree-followed-fixture-symlinks.md) [INC-0257](./INC-0257-moving-the-home-directory-broke-a-launch-that-found-its-cach.md) [INC-0342](./INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0368](./INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md) [INC-0381](./INC-0381-a-whole-tree-content-digest-detected-a-dependency-change-but.md)
