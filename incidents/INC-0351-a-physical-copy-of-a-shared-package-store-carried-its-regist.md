---
id: INC-0351
title: A physical copy of a shared package store carried its registry of outside links
date: 2026-11-01
classes: [test-isolation, tooling-paths]
severity: low
status: fixed
---

# INC-0351 - A physical copy of a shared package store carried its registry of outside links

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A preparation check that no copied link resolves outside the copy stopped the first authorized run before setup.

## What happened

a reviewed acceptance recipe copied the shared package store into a private home and verified that no copied link resolves outside the copy; the store's projects registry held 373 links to every project that ever used the store (temporary clones, worktrees, fixtures), 353 already dangling, so the first authorized run stopped in preparation before setup and nothing ran

## Root cause

the copy included the store's projects registry, which is metadata made of links to every project that ever used the store, so the containment check read it as a breach

## Why it was hard to see

The recipe was reviewed and its containment check was correct, but nobody listed the links in the store before copying it.

## Fix

Exclude the registry from the private copy, create it empty, keep every other outside link a stop, and record the excluded count

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before copying a shared tool cache into an isolated run, list its links; a registry of outside links is metadata to exclude, while any other outside link is a containment failure

## Related

[INC-0316](./INC-0316-a-recursive-diff-of-a-copied-tree-followed-fixture-symlinks.md) [INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) [INC-0119](./INC-0119-a-sandboxed-home-hid-tool-caches-such-as-package-manager-shi.md) [INC-0356](./INC-0356-a-reviewed-recipe-never-ran-its-real-tool-queries-because-ev.md) [INC-0368](./INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md) [INC-0375](./INC-0375-an-engineer-overwrote-its-own-unit-ledger-with-a-later-run.md) [INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md) [INC-0380](./INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md) [INC-0381](./INC-0381-a-whole-tree-content-digest-detected-a-dependency-change-but.md) [INC-0446](./INC-0446-a-fresh-worktree-can-be-provisioned-by-a-copy-on-write-clone.md)
