---
id: INC-0446
title: A fresh worktree can be provisioned by a copy-on-write clone of the dependency tree instead of an install that may hit dead store links
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0446 - A fresh worktree can be provisioned by a copy-on-write clone of the dependency tree instead of an install that may hit dead store links

**Cost:** Minor: a fresh worktree could not be provisioned by the usual install.

## Signature - how you recognise it

An offline install failed on dead links in the package store.

## What happened

a fresh worktree can be provisioned with a copy-on-write clone copy of the dependency tree, because the package manager's links are relative, instead of an install that may hit dead store links

## Root cause

the store links an install depends on can be dead, while a copied tree carries relative links

## Why it was hard to see

Copying a tree and linking it look alike, and only one is safe.

## Fix

provision a fresh worktree by cloning the dependency tree as a copy, never by linking it, when an install may hit dead store links

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Provision a fresh worktree by a copy-on-write clone of the dependency tree, never by linking, when an install may hit dead store links

## Related

[INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) [INC-0110](./INC-0110-a-cross-row-test-needed-setup-absent-from-its-own-lifecycle.md)
