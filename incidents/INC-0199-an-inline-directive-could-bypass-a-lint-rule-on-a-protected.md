---
id: INC-0199
title: An inline directive could bypass a lint rule on a protected path
date: 2026-10-30
classes: [reward-hacking, detector-fail-open]
severity: medium
status: fixed
---

# INC-0199 - An inline directive could bypass a lint rule on a protected path

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A bypass could be written inline.

## What happened

Inline directives could switch off a rule on a protected path; a files-scoped noInlineConfig disables them for that path only and the ignored directive still warns.

## Root cause

Inline directives could switch off a rule on a protected path; a files-scoped noInlineConfig disables them for that path only and the ignored directive still warns.

## Why it was hard to see

The bypass looks like ordinary configuration.

## Fix

Use the files-scoped setting so a bypass attempt stays visible

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scope noInlineConfig by files; an ignored directive still prints a warning

## Related

[INC-0176](./INC-0176-a-shape-regex-was-used-as-ownership-evidence-for-a-sweep.md)
