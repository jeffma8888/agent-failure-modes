---
id: INC-0121
title: A rule scoped to work after a ruling was applied per commit while one commit held old and new patterns
date: 2026-10-30
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0121 - A rule scoped to work after a ruling was applied per commit while one commit held old and new patterns

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

One commit contains files that predate the ruling and files that follow it.

## What happened

A rule scoped to work after a ruling was applied to a whole commit, but that commit held both old and new patterns.

## Root cause

The scope was set per commit, not per file.

## Why it was hard to see

The commit date suggests a single side of the ruling.

## Fix

Apply the rule per file within the commit.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scope a rule by the file, not the commit that carries it.
