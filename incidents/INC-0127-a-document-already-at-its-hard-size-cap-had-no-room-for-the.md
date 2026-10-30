---
id: INC-0127
title: A document already at its hard size cap had no room for the next transcription, so the cap was met only after editing
date: 2026-10-30
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0127 - A document already at its hard size cap had no room for the next transcription, so the cap was met only after editing

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
