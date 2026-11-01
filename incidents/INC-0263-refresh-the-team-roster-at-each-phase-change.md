---
id: INC-0263
title: Refresh the team roster at each phase change
date: 2026-11-01
classes: [delegation, observability]
severity: medium
status: fixed
---

# INC-0263 - Refresh the team roster at each phase change

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A team roster went stale for ten rounds.

## What happened

the team roster was stale for ten rounds, so thread IDs and models were hard to find

## Root cause

the team roster was stale for ten rounds, so thread IDs and models were hard to find

## Why it was hard to see

Nothing forces the roster to be updated.

## Fix

Refresh the roster at each phase change

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Refresh the team roster at each phase change so thread IDs and models stay findable

## Related

[INC-0237](./INC-0237-a-team-runtime-cap-blocked-new-teammates-behind-retained-idl.md)
