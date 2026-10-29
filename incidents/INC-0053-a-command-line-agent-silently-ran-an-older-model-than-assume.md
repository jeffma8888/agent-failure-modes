---
id: INC-0053
title: A command-line agent silently ran an older model than assumed and ignored an explicit model override
date: 2026-10-29
classes: [observability, ipc-and-env]
severity: medium
status: fixed
---

# INC-0053 - A command-line agent silently ran an older model than assumed and ignored an explicit model override

**Cost:** Every build in a pipeline ran on an older model generation than the team believed. No wrong output was found, but capability assumptions in the plans were off for the whole period.

## Signature - how you recognise it

A model setting is accepted without error, the tool answers normally, and nobody has read the model identifier from the response metadata.

## What happened

A pipeline's agent CLI resolved its default model alias through a managed allowlist that stopped at an older model family. A probe with JSON output showed every stage ran on that older model. Passing an explicit flag for a newer model did not fail: the CLI fell back to the default and still answered, so the override looked as if it had worked.

## Root cause

Silent fallback. A configuration value outside the allowlist was treated as unset instead of as an error, so acceptance of the flag was indistinguishable from effect of the flag. Asking the model which model it is is not evidence either.

## Why it was hard to see

Nothing fails and the answers are good. The only place the truth appears is a metadata block that people do not read when the output looks right.

## Fix

Verify the served model from the response metadata after any model change. Once the allowlist was widened the CLI refused outright (its version was too old for the newer model), which is the honest failure that should have been visible from the start.

## Verification

The real model identifier was read from the CLI's JSON usage block rather than from the flag or the model's own claim.

## Transferable rule

> A model setting is verified only by the model ID in the response metadata. A flag that is accepted is not a flag that took effect, and a tool that falls back instead of failing makes every override unverifiable until you read the metadata.

## Related

[INC-0036](./INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md) [INC-0021](./INC-0021-stale-module-import-shipped-is-not-live.md)
