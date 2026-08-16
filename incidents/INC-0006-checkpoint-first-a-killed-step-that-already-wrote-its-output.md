---
id: INC-0006
title: Checkpoint-first: a killed step that already wrote its output still counts
date: 2026-08-05
classes: [checkpoint, stage-timeout]
severity: medium
status: fixed
---

# INC-0006 - Checkpoint-first: a killed step that already wrote its output still counts

**Cost:** An iteration that would have been the fourth consecutive loss instead shipped, because a role prompt shipped 34 minutes earlier had introduced the write-early rule.

## Signature - how you recognise it

An attempt log is 48 bytes ('timed out after 600s') and the loop treats the iteration as a success anyway - because the OUTPUT FILE exists.

## What happened

A tester step hit the per-step cap. Its log was 48 bytes; its exit code non-zero. And yet the iteration was recorded as SUCCESS - because the agent had written a 3459-byte tester output file BEFORE being killed. A role-card rule shipped earlier had instructed every role to write a minimal-complete output file first, then refine in place.

## Root cause

Not a failure - a successful design pattern proving itself. The FAILURE that this pattern addresses is loops reading exit codes or log lengths to decide success when what actually mattered was whether a usable artifact existed.

## Why it was hard to see

The instinct is to read the exit code and the log. Both said 'killed'. Trusting the artifact instead requires a small leap.

## Fix

Define success as 'the output file exists and is non-empty', not as 'exit code zero'. Instruct every agent role to write its minimal complete artifact within the first few minutes and refine in place until killed. Never call a timeout a failure without checking whether the output file exists.

## Verification

The successful timed-out iteration shipped clean. Independent gates (final-step parser plus post-release fresh-clone re-run) still catch cases where the early checkpoint describes incomplete verification.

## Transferable rule

> Success is an ARTIFACT, not an exit code. Under a hard timeout, an agent that writes its minimal complete output first and refines in place still succeeds if killed. Correspondingly: never call a timeout a failure without checking whether the output file exists.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the write-early contract lives in the `roles/*.md` cards, which are read from disk per run, and the success-is-an-artifact rule is enforced by the stage runner rather than by exit code.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0005](./INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md)
