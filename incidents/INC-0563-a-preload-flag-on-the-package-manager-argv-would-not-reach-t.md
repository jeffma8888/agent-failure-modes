---
id: INC-0563
title: A preload flag on the package manager argv would not reach the exec'd child processes
date: 2026-11-04
classes: [ipc-and-env]
severity: low
status: mitigated
---

# INC-0563 - A preload flag on the package manager argv would not reach the exec'd child processes

**Cost:** None. The lead ruled before the observer was built that way.

## Signature - how you recognise it

An instrumentation flag set on a parent command does not reach children that the parent execs.

## What happened

The server is started through a package manager that execs the framework child processes, so an import flag on the package manager own arguments does not reach them. The lead ruled that a value the harness builds itself, exactly one import flag with the file URL of the observer resolved from the harness own repository root, set only in the server child environment and replacing any inherited value, is the fixed preload. Coverage requires a ready record from every Node process in the tree, a mutant without the preload must turn the coverage assertion red, and a unit case plants a parent value and asserts the child carries only the harness value.

## Root cause

The instrumentation was attached to one process, not to the environment the tree inherits.

## Why it was hard to see

The missing coverage is silent unless ready records are required.

## Fix

Build the value in the harness, replace any inherited one, and require ready records.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Carry an instrumentation preload through a harness-built environment value that replaces any inherited one, and require a ready record from every process in the tree.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
