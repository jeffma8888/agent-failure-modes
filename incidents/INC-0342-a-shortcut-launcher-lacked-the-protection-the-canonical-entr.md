---
id: INC-0342
title: A shortcut launcher lacked the protection the canonical entry supplies implicitly
date: 2026-11-01
classes: [tooling-paths, test-isolation]
severity: medium
status: fixed
---

# INC-0342 - A shortcut launcher lacked the protection the canonical entry supplies implicitly

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A gate was run by starting the test runner directly, and a nested fixture's package manager then pruned the host dependency tree.

## What happened

a selected-project run started the test runner directly instead of through the package manager's exec, so it lacked a setting the canonical entry passes to child processes (dependency verification off); a nested fixture's package manager then pruned the host dependency tree

## Root cause

a selected-project run started the test runner directly instead of through the package manager's exec, so it lacked a setting the canonical entry passes to child processes (dependency verification off); a nested fixture's package manager then pruned the host dependency tree

## Why it was hard to see

The shortcut runs the same tests and looks equivalent, while the protection lived only in the canonical path.

## Fix

Set the protective setting explicitly in the shared environment script and in every launcher, and close the gate only with the canonical entry in a disposable clone

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Close a gate only through the canonical entry; a shortcut launcher may lack protections the canonical path supplies implicitly

## Related

[INC-0340](./INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) [INC-0256](./INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) [INC-0344](./INC-0344-focused-runs-after-a-refactor-hid-static-check-residue-until.md) [INC-0354](./INC-0354-gating-by-an-environment-variable-leaked-into-nested-runners.md)
