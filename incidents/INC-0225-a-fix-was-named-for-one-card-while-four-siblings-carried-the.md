---
id: INC-0225
title: A fix was named for one card while four siblings carried the same command
date: 2026-10-31
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0225 - A fix was named for one card while four siblings carried the same command

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The siblings were left unfixed or silently changed.

## What happened

A reviewer named one instance of a rule while four sibling cards carry the same command.

## Root cause

A reviewer named one instance of a rule while four sibling cards carry the same command.

## Why it was hard to see

The named instance is the one in view.

## Fix

Search for siblings and report them instead of silently widening scope

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When applying a fix, search for siblings of the named instance and report them

## Related

[INC-0177](./INC-0177-card-text-pointed-at-its-own-directory-as-the-checkout.md)
