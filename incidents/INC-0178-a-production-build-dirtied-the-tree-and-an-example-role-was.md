---
id: INC-0178
title: A production build dirtied the tree and an example role was missing locally
date: 2026-10-30
classes: [tooling-paths, test-isolation]
severity: medium
status: fixed
---

# INC-0178 - A production build dirtied the tree and an example role was missing locally

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The tree was dirty after a successful build.

## What happened

A production build in a checkout that still tracks a per-mode generated file dirtied the tree, and an example env file named a role absent from the local cluster.

## Root cause

The tracked generated file and the example role were never exercised locally.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Check porcelain after every build and make the example role exist locally.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check porcelain after every build; verify an example role exists locally.

## Related

[INC-0170](./INC-0170-a-tracked-file-rewritten-per-tool-mode-could-not-stay-clean.md)
