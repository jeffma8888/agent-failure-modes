---
id: INC-0390
title: A dispatch packet written for a future branch went stale when a later ruling started the work elsewhere
date: 2026-11-01
classes: [stale-module]
severity: low
status: fixed
---

# INC-0390 - A dispatch packet written for a future branch went stale when a later ruling started the work elsewhere

**Cost:** A packet pointed at a branch the work had already left.

## Signature - how you recognise it

A packet named a branch and checkout that a later ruling had superseded.

## What happened

a dispatch packet written for a future branch went stale when a later ruling had already started the work on another checkout

## Root cause

the packet was written ahead of time and not compared with the rulings made since

## Why it was hard to see

The packet was correct when written, so it read as authoritative.

## Fix

Reconcile a packet with the newest ruling at the moment it lands

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Reconcile a dispatch packet with the newest ruling when it lands

## Related

[INC-0376](./INC-0376-a-signed-design-heading-outranked-a-plan-census-parenthetica.md) [INC-0368](./INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md) [INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0405](./INC-0405-the-demo-server-served-a-build-made-before-the-merge-so-a-wa.md) [INC-0413](./INC-0413-an-acceptance-document-cited-a-ruling-that-did-not-yet-exist.md) [INC-0433](./INC-0433-a-job-text-swapped-two-commit-identities-and-reading-the-log.md) [INC-0457](./INC-0457-a-ruling-wrote-a-media-directory-binding-from-memory-that-co.md) [INC-0466](./INC-0466-a-script-carried-internal-load-vetoes-that-contradicted-a-la.md)
