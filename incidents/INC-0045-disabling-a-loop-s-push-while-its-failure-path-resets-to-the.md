---
id: INC-0045
title: Disabling a loop's push while its failure path resets to the remote erases shipped work
date: 2026-10-28
classes: [vcs-destruction, spec-and-scope]
severity: high
status: fixed
---

# INC-0045 - Disabling a loop's push while its failure path resets to the remote erases shipped work

**Cost:** Near miss in a design draft, caught before review. Had it shipped, the first failed stage would have discarded every iteration shipped since the last manual push, silently.

## Signature - how you recognise it

A proposal simplifies a pipeline by turning off its publish step, while the rollback path of the same pipeline hard-resets to the published state and never fetches.

## What happened

To simplify gates, a minimal-scope draft set an autonomous build loop's push flag to false so that a human would push instead. The loop reverts every failed stage with a hard reset to the remote branch and never fetches. With pushing off, the remote branch would stay frozen, and the first failed stage would reset the loop's clone back to that frozen state, wiping every unpushed iteration.

## Root cause

The push step was classified as an optional gate. In this loop it is half of the durability contract: the reset target is the published state, so anything not published is one failure away from deletion.

## Why it was hard to see

Each piece is individually reasonable: a human-owned push is a conservative-looking choice, and a revert on failure is a standard safety mechanism. The loss appears only from their interaction, and only after a later failure, far from the edit that caused it.

## Fix

Keep the loop pushing, to a private remote and with a leak guard before every push. Other commits are synced into the loop's dedicated clone only between the loop's shifts, never while it runs.

## Verification

Found by reading the revert code and searching it for any fetch or pull, of which there was none, before accepting the simplification.

## Transferable rule

> Before turning off a pipeline's publish or push step, find what its rollback resets TO. If rollback targets the published state, publishing is part of the durability contract, not an optional gate.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the loop engine whose failure path reverts with a hard reset to the remote branch, the behaviour this near miss depended on. The failure was a design draft that was caught; it did not occur in that repository.

## Related

[INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md) [INC-0044](./INC-0044-pushing-a-local-repository-to-a-new-remote-publishes-its-who.md)
