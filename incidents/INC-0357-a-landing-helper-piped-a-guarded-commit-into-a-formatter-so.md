---
id: INC-0357
title: A landing helper piped a guarded commit into a formatter, so the guard's failure did not stop the cleanup
date: 2026-11-01
classes: [tooling-paths, vcs-destruction]
severity: low
status: fixed
---

# INC-0357 - A landing helper piped a guarded commit into a formatter, so the guard's failure did not stop the cleanup

**Cost:** Minor: nothing was lost because the operator noticed.

## Signature - how you recognise it

A scrub guard failed, yet the helper went on to delete the source file because the pipeline reported the formatter's zero status.

## What happened

a shell helper ran a copy, then a scrub-and-commit script piped into "tail -1", then a cleanup that deletes the source file from the author's worktree; the scrub failed on two absolute paths, but the pipeline's status was the formatter's (zero), so the cleanup ran and the only copy left was an uncommitted file in the main checkout; nothing was lost because the operator noticed

## Root cause

the guarded step was piped into a formatter, so the chain saw the formatter's exit status and the guard's failure could not stop the later destructive step

## Why it was hard to see

The output looked normal and the chain exited zero; the guard's failure showed only in text the formatter cut away.

## Fix

Capture the guarded step's output in a variable and return on its own nonzero status before printing or cleaning

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never pipe a gating command into a formatter in a chain whose later steps destroy the input; check the gate's own exit status

## Related

[INC-0347](./INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md) [INC-0280](./INC-0280-never-chain-a-write-after-a-diagnostic.md) [INC-0162](./INC-0162-a-chained-amend-reworded-the-previous-commit-after-a-failed.md) [INC-0254](./INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md) [INC-0362](./INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md) [INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md)
