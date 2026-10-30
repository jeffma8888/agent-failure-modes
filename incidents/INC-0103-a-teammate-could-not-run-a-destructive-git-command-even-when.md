---
id: INC-0103
title: A teammate could not run a destructive git command even when the lead instructed it
date: 2026-10-30
classes: [vcs-destruction, delegation]
severity: medium
status: fixed
---

# INC-0103 - A teammate could not run a destructive git command even when the lead instructed it

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A lead instructs a teammate to run a reset or similar, and the permission ceiling refuses it.

## What happened

A teammate could not run a destructive git command such as reset --hard even when the lead told it to, because the tool permission ceiling wins over the instruction.

## Root cause

The lead assumed an instruction overrides the sandbox rules of the delegated agent.

## Why it was hard to see

The instruction is reasonable and the refusal looks like a failure of the teammate.

## Fix

Give a non-destructive route, such as a new branch at the base, or run the command in the lead context.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Plan destructive operations for the context that holds the permission.
