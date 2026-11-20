---
id: INC-0548
title: An activator could not recover an earlier brief mutant text, so it named its own mutant and said so
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
topic: delegation/guessed-or-stale-id-name-path
occurrences: 1
---

# INC-0548 - An activator could not recover an earlier brief mutant text, so it named its own mutant and said so

**Catalog:** [root](../catalog/README.md) / [delegation](../catalog/delegation/README.md) / [A record is guessed or stale, or lives only in a message or worktree](../catalog/delegation/guessed-or-stale-id-name-path.md)

**Cost:** None. The mutant was disclosed as the activator own choice.

## Signature - how you recognise it

The brief that carried the mutant text is no longer available to the activator.

## What happened

While activating a root after an interruption, the activator could not recover the mutant text from the earlier assignment. It chose its own mutant, made the editor field read only so the remove control disappeared, recorded the diff, log and receipt, showed the red at the case line, restored the file to its original hash, and stated that the mutant was its own choice.

## Root cause

The mutant lived only in a message that was not carried into the files.

## Why it was hard to see

A substituted mutant can look like the assigned one if the choice is not stated.

## Fix

Disclose the choice, record the diff and restore hash, and keep the mutant text in a file.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> If an assigned mutant cannot be recovered, name your own, say so, and record its diff and restore hash; put mutant text in a file, not only in a message.

## Related

[INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
