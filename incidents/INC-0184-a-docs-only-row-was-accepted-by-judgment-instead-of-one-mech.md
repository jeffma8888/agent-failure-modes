---
id: INC-0184
title: A docs-only row was accepted by judgment instead of one mechanical diff
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0184 - A docs-only row was accepted by judgment instead of one mechanical diff

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Acceptance depended on reading.

## What happened

A docs-only rehearsal row needs a mechanical acceptance: one name-status diff against the stated parent proves file scope, plus the one state cell and no cited commit id.

## Root cause

Scope was checked by reading, not by a diff.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Run the one diff and check the state cell.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Accept a docs-only row by one name-status diff against the stated parent.

## Related

[INC-0163](./INC-0163-acceptance-ran-bare-vitest-while-the-real-gate-ran-setup-the.md)
