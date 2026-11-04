---
id: INC-0589
title: The only copies of eight reviewed drafts sat untracked in one worktree, and the ruling kept them untouched
date: 2026-11-04
classes: [delegation]
severity: low
status: mitigated
---

# INC-0589 - The only copies of eight reviewed drafts sat untracked in one worktree, and the ruling kept them untouched

**Cost:** None. A triage found nothing superseded them, so no cleaning was done.

## Signature - how you recognise it

Reviewed work exists only as untracked files in a worktree that someone may clean.

## What happened

A triage of the untracked items in one worktree found that all eight exist nowhere else and that nothing supersedes them. The lead ruled to keep all of them untracked and untouched, not to clean the tree. One needed fix is still needed on main, and a static check of its prerequisites on current main comes before it is landed as a pending root. Other parked drafts stay parked, and a bytecode cache directory is left alone.

## Root cause

Untracked files look like leftovers, but these were the only copies.

## Why it was hard to see

A tree clean-up would have destroyed the only copies.

## Fix

Triage the untracked items against main before any clean-up, and keep what nothing supersedes.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before cleaning a worktree, triage its untracked items against main; keep untouched any item nothing supersedes.

## Related

[INC-0510](./INC-0510-mutation-restore-receipts-were-kept-only-in-tool-output-so-t.md)
