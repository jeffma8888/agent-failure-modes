---
id: INC-0127
title: A document already at its hard size cap had no room for the next transcription, so the cap was met only after editing
date: 2026-10-30
classes: [spec-and-scope, observability]
severity: medium
status: fixed
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 2
---

# INC-0127 - A document already at its hard size cap had no room for the next transcription, so the cap was met only after editing

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Requirements, units, or hard limits cannot hold together](../catalog/spec-and-scope/requirements-and-limits-collide.md)

**Cost:** Minor: caught in review, an audit or an engineer check before it shipped.

## Signature - how you recognise it

An edit is made first and the size cap is discovered afterward.

## What happened

A document sat 132 bytes under a hard size cap, so the next transcription had to start by moving history out. The cap was not budgeted before editing.

## Root cause

The size limit was checked after the edit rather than planned.

## Why it was hard to see

The document looks fine until the first addition exceeds the cap.

## Fix

Budget the cap before editing and move history out first.

## Verification

Checked by the reviewer, engineer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Plan against a hard cap before the edit, not after.

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-26 - A design document's first five sections used 69 KB of a 70 KB cap before the tail sections existed, forcing about 6 KB of trims over 70 exact-match edits; the skeleton had no per-section byte budget. A template check left to the end also found six sections missing a required table.
