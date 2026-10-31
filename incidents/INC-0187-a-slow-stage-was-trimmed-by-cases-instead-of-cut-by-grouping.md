---
id: INC-0187
title: A slow stage was trimmed by cases instead of cut by grouping files
date: 2026-10-30
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0187 - A slow stage was trimmed by cases instead of cut by grouping files

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A stage kept growing while case trimming saved little.

## What happened

A stage that grows by whole files of process-spawning cases free of database use is cut by grouping the files; the slow cases in older files were fixed timeouts written into protected bytes or plan rules.

## Root cause

Trimming was aimed at cases that could not move.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Group the files that parallelize cleanly.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Group files that parallelize cleanly; do not trim cases whose timeouts are fixed.

## Related

[INC-0168](./INC-0168-disjoint-project-discovery-did-not-stop-a-suite-from-running.md)
