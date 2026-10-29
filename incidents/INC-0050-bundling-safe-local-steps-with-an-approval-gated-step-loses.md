---
id: INC-0050
title: Bundling safe local steps with an approval-gated step loses the local steps when the gate refuses
date: 2026-10-28
classes: [tooling-paths, checkpoint]
severity: low
status: fixed
---

# INC-0050 - Bundling safe local steps with an approval-gated step loses the local steps when the gate refuses

**Cost:** One turn of work redone. No damage: the refusal was clean and nothing was half-applied.

## Signature - how you recognise it

A single shell command performs an edit, a commit and a push, and the push is subject to a per-call human approval rule.

## What happened

An agent ran one command that edited a file, committed it and pushed. Pushes required a human's per-call approval under an explicit rule. The approval prompt expired while the human was away, and the whole command was refused as one unit, so the edit and the commit never happened either.

## Root cause

The approval gate applies to the command, not to the step inside it. Bundling steps that are safe to run unattended with a step that needs a human couples their fate: the gated step's refusal discards the work that needed no approval.

## Why it was hard to see

Chaining is the natural way to write a publish sequence, and it works every time a human is present. The coupling shows only when approval is slow or absent.

## Fix

Run local steps (edit, verify, commit) in their own command. Queue the gated pushes and send them as one batch when approval can be given.

## Verification

The refusal message said the command was refused, and a status check showed nothing had changed; afterwards the local steps landed on their own and the push waited.

## Transferable rule

> Never bundle unattended-safe steps with a step that needs a human's approval. Split the chain at the approval boundary so a refusal costs only the gated step.

## Related

[INC-0046](./INC-0046-a-script-with-external-writes-was-only-dry-run-for-its-first.md) [INC-0044](./INC-0044-pushing-a-local-repository-to-a-new-remote-publishes-its-who.md)
