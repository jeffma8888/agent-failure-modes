---
id: INC-0201
title: Two review titles named the wrong reviewer
date: 2026-10-30
classes: [delegation, observability]
severity: medium
status: fixed
topic: delegation/guessed-or-stale-id-name-path
occurrences: 1
---

# INC-0201 - Two review titles named the wrong reviewer

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md) / [A record is guessed or stale, or lives only in a message or worktree](../catalog/delegation/guessed-or-stale-id-name-path.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The report carried another reviewer name.

## What happened

Reviewers reused a template and left the previous reviewer name in the title, so two reports were attributed to the wrong reviewer.

## Root cause

Reviewers reused a template and left the previous reviewer name in the title, so two reports were attributed to the wrong reviewer.

## Why it was hard to see

The body is right and the header is stale.

## Fix

The lead checks the attribution line of every report before landing it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check the attribution line of every report before landing it

## Related

[INC-0185](./INC-0185-rename-detection-reported-a-false-rename-in-a-merge.md)
