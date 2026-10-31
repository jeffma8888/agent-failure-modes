---
id: INC-0159
title: A second reader of the same registry file was at risk of replacing the first
date: 2026-10-30
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0159 - A second reader of the same registry file was at risk of replacing the first

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Two rows each needed to parse the same assignments file.

## What happened

The identity checker prep added a parser of the assignments file while a later row planned its own checks over the same file.

## Root cause

Two rows owned overlapping parts of one file format.

## Why it was hard to see

Each parser looks correct alone; divergence shows later as two answers.

## Fix

Keep one parser in the repo and require the later row to reuse it; review the prep with a mutant that ignores the registry, a malformed line that fails closed, and an unregistered path that still gets the partial activation test.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> One parser per shared file format, reviewed with a mutant and a malformed-input case.

## Related

[INC-0157](./INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md)
