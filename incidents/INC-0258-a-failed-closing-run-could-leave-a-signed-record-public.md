---
id: INC-0258
title: A failed closing run could leave a signed record public
date: 2026-11-01
classes: [checkpoint, false-green]
severity: medium
status: fixed
---

# INC-0258 - A failed closing run could leave a signed record public

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Publishing came before the closing check.

## What happened

A closing record was at risk of being merged and uploaded before the exact-closing checks ran on it.

## Root cause

A closing record was at risk of being merged and uploaded before the exact-closing checks ran on it.

## Why it was hard to see

The record looks final once signed.

## Fix

Commit the closing record locally, run the exact-closing checks on it, and only then merge and upload

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the exact-closing checks on a local closing record before merging and uploading it

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md)
