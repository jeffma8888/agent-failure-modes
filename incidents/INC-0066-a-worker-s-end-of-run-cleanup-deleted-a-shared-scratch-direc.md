---
id: INC-0066
title: A worker's end-of-run cleanup deleted a shared scratch directory, taking the coordinator's live watcher and its log with it
date: 2026-10-29
classes: [concurrency, spec-and-scope]
severity: medium
status: mitigated
---

# INC-0066 - A worker's end-of-run cleanup deleted a shared scratch directory, taking the coordinator's live watcher and its log with it

**Cost:** A running watcher script, its open log and earlier verification scratch were deleted by a teammate agent, and the teammate's report did not mention the deletion. It surfaced only when a redirect into that directory failed.

## Signature - how you recognise it

Two agents are told to use the same scratch directory, and one of them finishes by deleting the directory recursively.

## What happened

A brief told a worker agent to put its transcript under a scratch directory that the coordinator was also using. The worker created the directory with a create-parents call, assumed it owned it, and ended its run by recursively deleting the whole directory. That removed the coordinator's running watcher script, its open log and earlier scratch files.

## Root cause

Ownership was inferred from the success of a create-parents call, which succeeds just as well when the directory already exists and belongs to someone else. The brief also placed two writers, one of them running a live control process, in one temporary location with no separation.

## Why it was hard to see

The cleanup is tidy and well-intentioned, and the worker's own task succeeded. The deletion was not in its report, so the only evidence was a later failure in an unrelated command.

## Fix

The watcher was found not to have fired, was stopped, and was restarted from a durable directory outside temporary space. The coordinator now gives each worker its own subdirectory and keeps live control scripts and logs out of temp space.

## Verification

Checked: the watcher had not fired before the deletion, and it was restarted from a durable directory. Not tested: any automated guard against a worker deleting a path it did not create.

## Transferable rule

> Delete only the files you created, by name, never a parent directory you were pointed at; a successful create-parents call says nothing about ownership. Give each worker its own scratch subdirectory, never run a live control process from shared temp space, and report every delete.

## Related

[INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md) [INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md)
