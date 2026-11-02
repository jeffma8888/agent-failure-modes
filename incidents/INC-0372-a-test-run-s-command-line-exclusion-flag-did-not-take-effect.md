---
id: INC-0372
title: A test run's command-line exclusion flag did not take effect, so excluded cases ran and called the package manager
date: 2026-11-01
classes: [detector-fail-open, test-isolation]
severity: medium
status: fixed
---

# INC-0372 - A test run's command-line exclusion flag did not take effect, so excluded cases ran and called the package manager

**Cost:** Moderate: a no-package-manager rule was breached by child processes; the breach was disclosed and the run inspected.

## Signature - how you recognise it

Cases that were meant to be excluded from a run executed anyway.

## What happened

a QA unit run used a command-line exclusion flag that did not take effect, so excluded resource-touching cases ran and their child processes called the package manager, against the rule that forbids it. The breach was disclosed in the review file

## Root cause

the exclusion was trusted from the flag instead of from the list of files actually collected before the run

## Why it was hard to see

A run with an exclusion flag looks the same whether or not the flag worked, and the harm happened in child processes the QA run did not directly start.

## Fix

Disclose the breach, inspect the run, and list the collected files before any filtered run

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> List the collected files before a filtered run and stop if any excluded file is still collected

## Related

[INC-0328](./INC-0328-a-selector-mirroring-a-config-s-exclusions-matched-basenames.md) [INC-0332](./INC-0332-a-tier-exclusion-matched-only-one-file-extension.md) [INC-0336](./INC-0336-a-tier-exclusion-was-added-only-after-a-witness-failed-witho.md) [INC-0368](./INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md)
