---
id: INC-0170
title: A tracked file rewritten per tool mode could not stay clean in both tiers
date: 2026-10-30
classes: [tooling-paths, false-green]
severity: medium
status: fixed
---

# INC-0170 - A tracked file rewritten per tool mode could not stay clean in both tiers

**Cost:** Minor: spurious dirty trees.

## Signature - how you recognise it

Two modes of one tool wrote different bytes to a tracked file.

## What happened

The development mode and the build mode of a framework write different bytes to the same tracked type declaration file, so neither tier could stay porcelain clean.

## Root cause

A generated file was tracked.

## Why it was hard to see

Each run is clean alone and the diff appears only after the other mode.

## Fix

Untrack the file and generate it before the type check.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not track a file a tool rewrites per mode; generate it before the check that needs it.

## Related

[INC-0147](./INC-0147-a-moved-history-row-was-silently-modernized-instead-of-stayi.md)
