---
id: INC-0281
title: Confirm the landing commit contains every file before cleaning the source
date: 2026-11-01
classes: [vcs-destruction, checkpoint]
severity: medium
status: fixed
---

# INC-0281 - Confirm the landing commit contains every file before cleaning the source

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A source was cleaned against a failed commit and its change was reverted.

## What happened

a worktree was cleaned against a commit that did not contain its file because the commit had failed, which reverted the worktree tracked change; another checkout still had the copy, so nothing was lost

## Root cause

a worktree was cleaned against a commit that did not contain its file because the commit had failed, which reverted the worktree tracked change; another checkout still had the copy, so nothing was lost

## Why it was hard to see

The clean step ran against whatever commit existed, not the one intended.

## Fix

Check that the landing commit contains every file before cleaning the source

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Confirm the landing commit contains every file before cleaning the source

## Related

[INC-0254](./INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md)
