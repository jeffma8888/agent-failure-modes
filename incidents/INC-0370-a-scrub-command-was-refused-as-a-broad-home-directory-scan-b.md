---
id: INC-0370
title: A scrub command was refused as a broad home-directory scan by the operating system's privacy layer
date: 2026-11-01
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0370 - A scrub command was refused as a broad home-directory scan by the operating system's privacy layer

**Cost:** Minor: one refused step and a rerun with a narrower search.

## Signature - how you recognise it

A search step was refused by the operating system as a scan of the whole home directory.

## What happened

a teammate's scrub command searched far beyond the teammate's own worktree and was refused by the operating system's privacy layer as a broad home-directory scan

## Root cause

the search was scoped to a directory tree wider than the work, instead of to the tracked files of the teammate's own tree

## Why it was hard to see

The scrub step looked routine, and the refusal came from the operating system rather than from the tool, so it read like a permission fault.

## Fix

Use a scoped search over tracked files in the teammate's own worktree (a pathspec-limited grep) and a replace that opens only the exact files listed

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scope searches to tracked files in your own tree; never scan the home directory

## Related

[INC-0200](./INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md) [INC-0249](./INC-0249-a-cd-to-a-path-in-a-variable-was-refused-by-the-sandbox.md) [INC-0119](./INC-0119-a-sandboxed-home-hid-tool-caches-such-as-package-manager-shi.md) [INC-0386](./INC-0386-a-path-identity-guard-compared-strings-while-a-temp-director.md)
