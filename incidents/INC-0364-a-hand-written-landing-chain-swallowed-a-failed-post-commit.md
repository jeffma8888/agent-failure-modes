---
id: INC-0364
title: A hand-written landing chain swallowed a failed post-commit leak scan and three commits landed on top
date: 2026-11-01
classes: [tooling-paths, false-green]
severity: medium
status: fixed
---

# INC-0364 - A hand-written landing chain swallowed a failed post-commit leak scan and three commits landed on top

**Cost:** Minor: a rewrite of four local commits and a branch move; nothing was pushed because pushes were frozen.

## Signature - how you recognise it

A landing step printed nothing and the chain moved on, although the script it ran had exited non-zero.

## What happened

a reviewer's file was landed with a hand-written chain: capture the output of a commit-and-check script, then print it only if the script succeeded. The script commits first and then runs a range leak scan, exiting 3 if the new commit leaks. It exited 3 because of a banned internal word in prose, the chain skipped the print, and nothing was shown. Three more commits were landed on top before a later range check flagged the first one. Pushes were frozen, so nothing left the machine. The guarded landing helper, which prints every step's status and stops on any failed check, was not used

## Root cause

a post-commit check whose failure was swallowed by an output-printing chain, and an ad-hoc landing used in place of the guarded helper

## Why it was hard to see

A failed step in such a chain produces no output at all, which looks the same as a quiet success, and the commit already existed when the check ran.

## Fix

Rewrite the one commit in a temporary worktree, cherry-pick the three later commits onto it, move the main branch and the idle worktrees with a safe reset, and re-run the range scan clean

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Print the exit status of every commit and check step explicitly (never only on success), run the range leak scan before landing anything on top of a new commit, and use the guarded landing helper, not an ad-hoc chain

## Related

[INC-0357](./INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md) [INC-0362](./INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md) [INC-0303](./INC-0303-a-guard-added-to-a-test-tool-broke-the-check-under-test.md) [INC-0396](./INC-0396-a-multi-step-command-reported-success-for-its-later-steps-wh.md)
