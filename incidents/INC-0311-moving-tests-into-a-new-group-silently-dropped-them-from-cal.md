---
id: INC-0311
title: Moving tests into a new group silently dropped them from callers that select the old group by name
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0311 - Moving tests into a new group silently dropped them from callers that select the old group by name

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A proposed move would have made every selector that names the old group omit the moved files.

## What happened

a design moved some test files into a new serial group, but fixed quality payloads and full runs select the old group by name, so the files would have left both selections without any failure

## Root cause

a design moved some test files into a new serial group, but fixed quality payloads and full runs select the old group by name, so the files would have left both selections without any failure

## Why it was hard to see

The ordinary runner still works after the move, and the other callers are not in view when the design is written.

## Fix

Before re-routing tests between groups, list every caller that selects the group by name, prove each still selects the same files, and prefer an explicit opt-in over changing the default route

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before re-routing tests between groups, list every caller that selects the group by name and prove each still selects the same files

## Related

[INC-0132](./INC-0132-vitest-4-ran-projects-in-parallel-and-file-serialization-ins.md) [INC-0173](./INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md) [INC-0328](./INC-0328-a-selector-mirroring-a-config-s-exclusions-matched-basenames.md)
