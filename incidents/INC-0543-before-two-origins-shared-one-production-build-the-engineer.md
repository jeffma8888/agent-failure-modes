---
id: INC-0543
title: Before two origins shared one production build, the engineer searched the build output for the baked origin and found none
date: 2026-11-02
classes: [ipc-and-env]
severity: low
status: mitigated
---

# INC-0543 - Before two origins shared one production build, the engineer searched the build output for the baked origin and found none

**Cost:** None. The check removed the need for a second build.

## Signature - how you recognise it

A production build can embed an origin or address, which would make one build wrong for a second origin.

## What happened

Two server origins were to run from one production build. Before sharing it, the engineer searched the build output, including client bundles, for the full origin string of the first server. The search found no file. The setup report recorded the exact command and its empty result, and the build was shared with no second build for the read-only origin.

## Root cause

Build-time environment values can be baked into the artifact.

## Why it was hard to see

Whether a value is baked is not visible from the config alone.

## Fix

Search the built artifact for the origin before sharing it, and record the command and result.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before reusing one production build for several origins, search the build output for the baked origin and record the empty result.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
