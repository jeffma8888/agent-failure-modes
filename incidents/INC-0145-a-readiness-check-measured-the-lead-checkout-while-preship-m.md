---
id: INC-0145
title: A readiness check measured the lead checkout while preship measures the Foundry clone
date: 2026-10-30
classes: [stale-module, observability]
severity: medium
status: fixed
---

# INC-0145 - A readiness check measured the lead checkout while preship measures the Foundry clone

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A readiness verdict is taken from one checkout and the gate reads another.

## What happened

Preship measures the Foundry clone, not the lead checkout, so a readiness check on the lead checkout said nothing about what preship would see.

## Root cause

The checked tree and the measured tree were different.

## Why it was hard to see

Both trees carry the same branch name and look current.

## Fix

Fast-forward the Foundry clone as part of every readiness check.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check the tree the gate actually reads.

## Related

[INC-0114](./INC-0114-a-second-clone-named-after-the-remote-held-a-stale-tip-and-w.md)
