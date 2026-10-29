---
id: INC-0065
title: A 'graceful' stop flag checked before every stage would have discarded the in-flight iteration's finished work
date: 2026-10-29
classes: [vcs-destruction, spec-and-scope]
severity: high
status: fixed
---

# INC-0065 - A 'graceful' stop flag checked before every stage would have discarded the in-flight iteration's finished work

**Cost:** Near miss, found by reading the dispatcher before writing the flag. Written mid-iteration, it would have abandoned the remaining stages and reverted the tree, possibly throwing away an already finished stage.

## Signature - how you recognise it

A stop sentinel is meant to drain a loop between iterations, but nobody has checked where in the loop it is read.

## What happened

The global stop sentinel in a stage dispatcher is checked before every stage attempt, not only between iterations. Writing it during an iteration would stop the remaining stages and trigger the failure path, which reverts the working tree and can discard a completed engineering stage.

## Root cause

The name 'stop' suggested a drain at the iteration boundary, but the implementation treats it as an abort at every check. The stop flag and the revert-on-failure path were wired together, so an interrupted iteration is a failed one.

## Why it was hard to see

The flag works as expected when written between iterations, so a test of it passes. The destructive case only exists in the middle of an iteration.

## Fix

A watcher writes the stop flag only once the iteration's last stage has started, waits for the old process to exit, then relaunches.

## Verification

The behaviour was established by reading every place the flag is checked, not by trying it on a live iteration.

## Transferable rule

> Before using a stop flag to drain a loop, read every place it is checked, and set it only after the last check that would discard work.

## Related

[INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md) [INC-0045](./INC-0045-disabling-a-loop-s-push-while-its-failure-path-resets-to-the.md)
