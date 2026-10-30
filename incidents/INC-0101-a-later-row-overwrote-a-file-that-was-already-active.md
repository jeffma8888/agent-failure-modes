---
id: INC-0101
title: A later row overwrote a file that was already active
date: 2026-10-30
classes: [vcs-destruction, spec-and-scope]
severity: medium
status: fixed
---

# INC-0101 - A later row overwrote a file that was already active

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

Part of a file must activate later, and activating it replaces the active file.

## What happened

Part of a file was due to activate at a later row, and the plan had that row overwrite the already active file.

## Root cause

The later part shared a destination with the earlier part.

## Why it was hard to see

A shared destination looks natural for one logical test file.

## Fix

Give the later part a new destination file; a later row must never overwrite an already active file.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Active files are append-only; later parts get new destinations.
