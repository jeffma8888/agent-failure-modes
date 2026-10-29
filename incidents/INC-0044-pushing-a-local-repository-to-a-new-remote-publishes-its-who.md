---
id: INC-0044
title: Pushing a local repository to a new remote publishes its whole history, not its current tree
date: 2026-10-28
classes: [vcs-destruction, spec-and-scope]
severity: high
status: fixed
---

# INC-0044 - Pushing a local repository to a new remote publishes its whole history, not its current tree

**Cost:** Near miss, caught before the first push. Confidential commercial documents sat in the history of a planning repository about to get a remote; the plan was to leave them out, which would have changed the tree and not the history. Published history cannot be recalled, so the cost avoided was permanent.

## Signature - how you recognise it

A repository is about to be pushed for the first time, the plan is stated in terms of which files to exclude, and nobody has listed the paths that were EVER tracked.

## What happened

A client project's planning repository was about to be pushed to a new private remote. Business documents containing pricing had been committed earlier. The plan was to omit them, but deleting a file from the working tree leaves every earlier blob and every commit message that mentions it in the pushed history, and a push transmits the history.

## Root cause

The author reasoned about the repository as its current tree. What a push publishes is the full reachable history: every path ever tracked, every blob version, every commit message. A one-way door was approached with a model of the repository that only describes the present.

## Why it was hard to see

The working tree is clean and a scan of it passes. The sensitive content is invisible to every command people habitually run before a push, and a private remote feels low-stakes, which discourages the audit that would find it.

## Fix

Audit the history, not the tree: list every path ever tracked across all refs, scan every blob version and every commit message. Rewrite a scratch clone with path exclusion plus text replacement, rescan the rewritten history to zero hits, push that, then move the working copy onto the rewritten history. Keep the original history in a local-only archive. Install a pre-push guard that scans the pushed range.

## Verification

The rewritten history was scanned across blobs and commit messages with zero hits before any push, and the guard rejects a push whose range contains a banned token.

## Transferable rule

> Pushing an existing repository publishes its HISTORY. Before the first push audit every path ever tracked, every blob version and every commit message, never only the tree, and install a pre-push guard that scans the pushed range. Excluding a file from the tree does not remove it from history.

## Related

[INC-0015](./INC-0015-git-identity-leak-real-name-via-ambient-global-config.md) [INC-0040](./INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md)
