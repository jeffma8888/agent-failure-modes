---
id: INC-0012
title: A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit
date: 2026-08-05
classes: [vcs-destruction, concurrency]
severity: high
status: mitigated
topic: null
occurrences: 2
---

# INC-0012 - A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit

**Catalog:** [root](../catalog/README.md) / [vcs-destruction](../catalog/vcs-destruction/README.md)

**Cost:** Two prose edits landed under a loop's commit message; content survived, history was mislabeled. It recurred every iteration until the pattern was noticed. A later recurrence briefly swept 276 tracked files into a one-line status commit; the commit was undone with all working-tree bytes preserved.

## Signature - how you recognise it

`git log --oneline -S "<a phrase you typed>" -- <file>` shows your text landed in a commit whose SUBJECT is the loop's story.

## What happened

A human hand-edited a documentation file in a directory the loop committed from. The loop's next iteration ran `git add -A` before its own commit and swept the human's uncommitted work into the loop's commit under the loop's subject line. Recurred every iteration. The same sweep recurred with a coordinator, not a loop, as the committer: a status update committed with the all-tracked-files flag also took a teammate's in-progress 275-line file into an unrelated commit, mislabelled; the content was final so only the message was wrong, but a slower writer would have had a half-written file committed. Found because the next add of that file reported nothing to commit. On 2026-11-12, a quick follow-up to trim one status line in a shared notes repository used `git commit -am` after two earlier commits had staged only the intended file. Other live sessions had 276 modified tracked files uncommitted, so the commit took all of them under the one-line status message. The next check of the commit stat exposed the sweep. While the bad commit was still HEAD, a mixed reset to its parent preserved every working-tree byte, and a commit naming only the intended file left the other changes uncommitted for their owners.

## Root cause

The git index is process-shared state. A blanket `add -A` stages EVERYTHING that has changed in the working tree, not only what the loop authored. If two writers (or an agent and a human) share the tree, whoever commits second commits both sets of edits. The `commit -a` flag performs the same blanket staging for modified tracked files, even if earlier commits named only the intended path.

## Why it was hard to see

Content is preserved, tests are still green, no error. The only symptom is a wrongly-labeled commit subject. If you weren't looking, you'd never see it.

## Fix

Do not hand-edit a directory a loop commits from. If you must, drop the loop's STOP sentinel first. A path-limited commit (`git commit -m '...' -- <paths>`) protects the LOOP's work from a human's blanket add, but it CANNOT protect a human's work from the loop's blanket add - because the loop is the one running `add -A`. The full protection is exclusivity: quiesce one side before the other writes. In any multi-writer tree, name paths on the commit itself, never use blanket staging flags, and inspect the resulting commit stat before moving on. If an over-broad commit must be undone, do so only while it is still HEAD and without touching working-tree bytes, then recommit only the intended file and leave the other edits for their owners.

## Verification

After the human edit was staged into a proper quiesced window, the next 30 iterations shipped without sweeping any human file into a loop commit. In the later recurrence, the reporter checked the 276-file commit stat and the recovery that preserved the working tree and returned other writers' edits to uncommitted state. Not checked: whether the stat-check rule prevents recurrence.

## Transferable rule

> In a multi-writer tree, never use `git add -A` or `git commit -a`; name paths on the commit itself and check its stat before moving on. A path-limited commit cannot protect your edits from another writer's blanket stage, so quiesce live loops before editing their tree. Undo an over-broad commit only while it is still HEAD and without changing working-tree bytes.

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0229](./INC-0229-a-commit-swept-another-session-uncommitted-entries.md) - 2026-10-31 - A commit swept another session uncommitted entries

## Related

[INC-0013](./INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md) [INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md)
