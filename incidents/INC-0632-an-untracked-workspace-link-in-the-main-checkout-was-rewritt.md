---
id: INC-0632
title: An untracked workspace link in the main checkout was rewritten during a sibling worktree's provisioning to a target that only worked from main by accident, and four days later a gate that copied dependencies failed in a way that looked like a product fault
date: 2026-11-08
classes: [tooling-paths]
severity: high
status: mitigated
---

# INC-0632 - An untracked workspace link in the main checkout was rewritten during a sibling worktree's provisioning to a target that only worked from main by accident, and four days later a gate that copied dependencies failed in a way that looked like a product fault

**Cost:** A full gate run failed 2 of 115 integration cases with a module-not-found error and was first read as a product fault; four days of unnoticed risk before it.

## Signature - how you recognise it

A module-not-found error in a copied dependency tree for a workspace package that main resolves.

## What happened

An untracked workspace link in the main checkout was rewritten at 06:10 on 11/04, inside a sibling prototype worktree's provisioning window, to a relative target that reached the prototype's copy of the shared package. From main's depth it resolved by accident, so main kept working. Four days later a full gate that copies the dependency tree from main into a deeper worktree met the dangling link and failed integration with module-not-found, which looked like a product fault. The earlier run had started before the rewrite and the next stopped before any tier, so this was the first to meet it. A scan of the dependency trees found no other link into a worktree. The link was restored to main's own package, and the gate script now stops before any test unless the link resolves inside its own tree, which was red-checked on the failed worktree. The engineer's account refines the mechanism: the prototype worktree's dependency directories were first linked into main, and a package-manager command run in that worktree did an automatic install pass that, through the alias, rewrote main's nested workspace link. A later copy of the directories carried the rewritten link. The engineer's earlier claim of no changes in main rested on an empty git status, which never shows ignored dependency trees.

## Root cause

Provisioning a worktree wrote through the main checkout's dependency tree, and the link was untracked, so nothing reviewed it.

## Why it was hard to see

The wrong link worked from main by depth coincidence, so nothing failed until a copy was made one level deeper.

## Fix

Restore the link to its own package, add a gate guard that stops before any test unless workspace links resolve inside the gate's own tree, and prove the guard red on the failed worktree.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never provision a worktree by writing through the main checkout's dependency tree; a gate that copies dependencies verifies workspace links resolve inside its own tree before any test. A no-change claim about a checkout must check the ignored trees it could have touched, not only git status.

## Related

[INC-0599](./INC-0599-a-checklist-expected-a-slug-first-link-and-excused-absent-he.md) [INC-0588](./INC-0588-a-reviewer-s-original-race-script-could-not-run-unmodified-a.md)
