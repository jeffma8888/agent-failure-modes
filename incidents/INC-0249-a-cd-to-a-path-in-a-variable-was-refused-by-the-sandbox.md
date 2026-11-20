---
id: INC-0249
title: A cd to a path in a variable was refused by the sandbox
date: 2026-11-01
classes: [tooling-paths]
severity: medium
status: fixed
topic: tooling-paths/sandbox-refuses-allowed-target
occurrences: 2
---

# INC-0249 - A cd to a path in a variable was refused by the sandbox

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [Sandbox cannot resolve or authorize the target you actually meant](../catalog/tooling-paths/sandbox-refuses-allowed-target.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The command was refused although the path was allowed.

## What happened

A sandbox refuses cd to a path held in a shell variable because it cannot see the path.

## Root cause

A sandbox refuses cd to a path held in a shell variable because it cannot see the path.

## Why it was hard to see

The path is the same once expanded.

## Fix

Use literal paths

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Use literal paths for cd in a sandbox

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0607](./INC-0607-a-sandboxed-shell-refused-a-directory-change-whose-target-wa.md) - 2026-11-04 - A sandboxed shell refused a directory change whose target was held in a variable

## Related

[INC-0212](./INC-0212-a-relative-path-was-resolved-against-the-wrong-root.md) [INC-0369](./INC-0369-a-bare-syntax-check-resolved-to-a-different-runtime-that-ign.md) [INC-0370](./INC-0370-a-scrub-command-was-refused-as-a-broad-home-directory-scan-b.md)
