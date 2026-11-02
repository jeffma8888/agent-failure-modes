---
id: INC-0474
title: A range whitespace check exited 2 on generated migration SQL, while the worktree only form had exited 0 earlier
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0474 - A range whitespace check exited 2 on generated migration SQL, while the worktree only form had exited 0 earlier

**Cost:** Minor: caught before the merge; the earlier exit 0 had been read as range proof.

## Signature - how you recognise it

A worktree only check passed where the branch range check failed.

## What happened

A static whitespace check over the branch range exited 2 on a generated migration file, while the worktree only form had exited 0 earlier, so that earlier result was not range proof. The same class of generator output was already on the main branch in two older migration files.

## Root cause

The worktree only form does not read committed changes in the range, so it could not see the generated file.

## Why it was hard to see

Both forms are the same command with different scope, and an exit 0 looks like a pass for the whole branch.

## Fix

Run the check over the whole branch range, exclude generator output by path, never reformat generated SQL, and keep every other path clean; the range check must exit 0 with that exclusion.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A worktree only whitespace check is not range proof; run the check over the branch range, exclude generator output by path, never reformat it, and keep every other path clean.

## Related

[INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md)
