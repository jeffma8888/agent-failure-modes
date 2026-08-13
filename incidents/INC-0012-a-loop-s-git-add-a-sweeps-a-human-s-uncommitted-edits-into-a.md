---
id: INC-0012
title: A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit
date: 2026-08-05
classes: [vcs-destruction, concurrency]
severity: high
status: mitigated
---

# INC-0012 - A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit

**Cost:** Two prose edits landed under a loop's commit message; content survived, history was mislabeled. It recurred every iteration until the pattern was noticed.

## Signature - how you recognise it

`git log --oneline -S "<a phrase you typed>" -- <file>` shows your text landed in a commit whose SUBJECT is the loop's story.

## What happened

A human hand-edited a documentation file in a directory the loop committed from. The loop's next iteration ran `git add -A` before its own commit and swept the human's uncommitted work into the loop's commit under the loop's subject line. Recurred every iteration.

## Root cause

The git index is process-shared state. A blanket `add -A` stages EVERYTHING that has changed in the working tree, not only what the loop authored. If two writers (or an agent and a human) share the tree, whoever commits second commits both sets of edits.

## Why it was hard to see

Content is preserved, tests are still green, no error. The only symptom is a wrongly-labeled commit subject. If you weren't looking, you'd never see it.

## Fix

Do not hand-edit a directory a loop commits from. If you must, drop the loop's STOP sentinel first. A path-limited commit (`git commit -m '...' -- <paths>`) protects the LOOP's work from a human's blanket add, but it CANNOT protect a human's work from the loop's blanket add - because the loop is the one running `add -A`. The full protection is exclusivity: quiesce one side before the other writes.

## Verification

After the human edit was staged into a proper quiesced window, the next 30 iterations shipped without sweeping any human file into a loop commit.

## Transferable rule

> The git index is process-shared. A blanket `git add -A` stages everything in the tree, including uncommitted work you did not author. When a loop is live: do not hand-edit its tree; if you must, drop the loop's STOP sentinel first. A path-limited commit protects the loop from you, not you from the loop.

## Related

[INC-0013](./INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md) [INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md)
