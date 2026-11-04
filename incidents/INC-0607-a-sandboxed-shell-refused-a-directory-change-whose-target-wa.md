---
id: INC-0607
title: A sandboxed shell refused a directory change whose target was held in a variable
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0607 - A sandboxed shell refused a directory change whose target was held in a variable

**Cost:** One command batch was refused before any part ran, and had to be rerun with literal paths.

## Signature - how you recognise it

A cd is refused as outside the workspace with an unresolvable target.

## What happened

A command that changed directory to a path held in a shell variable was refused by the sandbox because the target could not be resolved before the command ran. Nothing in the batch executed. The same steps succeeded when the absolute path was written out literally.

## Root cause

The sandbox checks the directory change statically, and a variable has no value at that time.

## Why it was hard to see

The refusal covers the whole batch, so earlier steps silently did not run until the state was checked.

## Fix

Write the absolute path literally in every directory change, and check the repository state after a refused batch.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In a sandboxed shell, change directory only to a literal absolute path, never to a variable, and check what ran after any refusal.

## Related

[INC-0603](./INC-0603-a-measurement-wrapper-called-an-agent-cli-inside-a-locked-sh.md)
