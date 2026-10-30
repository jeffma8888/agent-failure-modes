---
id: INC-0114
title: A second clone named after the remote held a stale tip and was mistaken for the working checkout
date: 2026-10-30
classes: [vcs-destruction, tooling-paths]
severity: medium
status: fixed
---

# INC-0114 - A second clone named after the remote held a stale tip and was mistaken for the working checkout

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

Two checkouts exist, and the folder name suggests the wrong one is current.

## What happened

After context compaction, a second clone named after the remote held a stale tip and could be mistaken for the working checkout.

## Root cause

The checkout was identified by folder name, not by its HEAD commit.

## Why it was hard to see

Both folders look like valid repositories.

## Fix

Identify the working checkout by its HEAD commit before acting.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never identify a checkout by its folder name.
