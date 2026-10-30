---
id: INC-0069
title: A gate compared the candidate commit with itself because a local clone redefines the remote-tracking ref
date: 2026-10-29
classes: [detector-fail-open, false-green]
severity: medium
status: mitigated
---

# INC-0069 - A gate compared the candidate commit with itself because a local clone redefines the remote-tracking ref

**Cost:** A planned hold check could never have fired. Caught in plan review before it shipped, by three independent reviewers, two of whom reproduced it in a scratch repository.

## Signature - how you recognise it

A check diffs against the main branch of the remote, and it runs in a fresh clone of a local checkout rather than of the real remote.

## What happened

A plan's hold check compared row-state changes against the remote's main branch. The pipeline's pre-ship verifier runs the suite in a fresh clone of the LOCAL checkout, and in that clone the remote is the checkout itself, so the remote-tracking ref is the candidate commit and the comparison always shows no change.

## Root cause

Remote-tracking refs are properties of the repository the check runs in, not of the project. Cloning a local path redefines what the remote is, so a baseline named by ref silently becomes the candidate.

## Why it was hard to see

The check is correct in the author's own checkout and in any clone of the real remote. It is a fail-open detector whose silence looks like 'nothing changed'.

## Fix

Queued for the next plan revision: record the baseline commit explicitly, or run the check where the remote is the real one. The clone command was confirmed at its source before the ruling.

## Verification

Two reviewers reproduced the behaviour in a scratch repository and the clone command was read at its source. The revised check itself is not yet verified.

## Transferable rule

> A check that runs inside a clone must not rely on remote-tracking refs. State the baseline commit explicitly, and reproduce the ref topology in a scratch repo before trusting the check.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0023](./INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md)
