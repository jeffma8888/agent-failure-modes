---
id: INC-0064
title: A launcher pointed a live unattended loop at the development checkout instead of a pinned release
date: 2026-10-29
classes: [ipc-and-env, stale-module]
severity: high
status: fixed
---

# INC-0064 - A launcher pointed a live unattended loop at the development checkout instead of a pinned release

**Cost:** Near miss, caught before the cutover ran. Had it gone live, the next round of development in that checkout would have reached live stages half edited.

## Signature - how you recognise it

The path a production loop uses to call its stage engine is the same working tree where developers are still making changes.

## What happened

A drafted launcher set a stage engine to the development repository's own wrapper script, which imports the working tree on every call. Every stage the live loop ran would have executed whatever state that tree was in at that moment, including partial edits.

## Root cause

The deployment and the development copy were the same thing. A wrapper that resolves code from a mutable tree at call time turns every commit, and every unsaved edit, into an immediate production change with no release step.

## Why it was hard to see

It works perfectly at launch, because the tree is in a good state at that moment. The failure arrives later and looks like a random stage error rather than a deployment fault.

## Fix

Tag the release, run the live loop from a detached worktree at that tag, and make upgrades an explicit three-step action: tag, create a worktree, repoint the launcher.

## Verification

Found by reading the drafted launcher's path before the cutover; the launcher's engine path now resolves to a detached worktree at the release tag, and development continues in the original checkout.

## Transferable rule

> A running unattended loop executes a pinned, tagged copy of every tool it calls, never a tree someone is editing. Make upgrades an explicit step, not a side effect of a commit.

## Related

[INC-0021](./INC-0021-stale-module-import-shipped-is-not-live.md) [INC-0036](./INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md)
