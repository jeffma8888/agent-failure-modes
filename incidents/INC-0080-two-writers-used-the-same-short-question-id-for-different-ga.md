---
id: INC-0080
title: Two writers used the same short question ID for different gaps, so a real gap looked ruled
date: 2026-10-30
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0080 - Two writers used the same short question ID for different gaps, so a real gap looked ruled

**Cost:** Moderate: new gaps looked already tracked or answered, so nobody owned them until a cross review noticed the collision.

## Signature - how you recognise it

A shared question table uses short bare names, and several writers add questions without a namespace.

## What happened

One engineer raised a question under a short ID for an undefined environment set and cited another short ID for missing cases. The lead's table already used both IDs for different matters, one of them already ruled, so the new gaps appeared tracked or answered.

## Root cause

Bare short names are shared across writers with no owner, so the same name can mean two things and a ruling on one silently covers the other.

## Why it was hard to see

Each use looks locally correct, and the collision shows only when two tables are compared.

## Fix

Question IDs are namespaced by row or author, and colliding entries were renamed in the records.

## Verification

Checked: the renamed entries against the lead's table. Not checked: older records for further collisions.

## Transferable rule

> Give every shared ID a namespace one writer owns, such as the row or author; a bare short name is a collision waiting to happen.

## Related

[INC-0079](./INC-0079-a-second-writer-reused-a-shared-registry-s-batch-name-and-it.md)
