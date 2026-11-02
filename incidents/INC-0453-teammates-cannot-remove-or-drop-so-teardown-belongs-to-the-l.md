---
id: INC-0453
title: Teammates cannot remove or drop, so teardown belongs to the lead and runs from the runner names file
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0453 - Teammates cannot remove or drop, so teardown belongs to the lead and runs from the runner names file

**Cost:** None: planned before the walk.

## Signature - how you recognise it

Cleanup could not be run by the teammate that created the things.

## What happened

teammates cannot run removals or database drops because of their permission ceiling; for a walk the runner stops after copying its evidence and writes a names file, and the lead runs teardown from that file: stop the server by its recorded process id, drop the database under an exact name guard, dump it, and remove the root and worktree; the lead appends a clocked receipt to the runner report and walk pass and cleanup pass stay separate

## Root cause

teammate permissions exclude removal and drop operations

## Why it was hard to see

Cleanup looks like part of the run, so it is easy to leave it in the runner scope.

## Fix

give teardown to the lead and drive it from the exact names the runner recorded

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Plan teardown as a lead owned step driven from the runner names file, and keep walk pass and cleanup pass separate

## Related

[INC-0404](./INC-0404-a-safe-default-could-silently-drop-data-when-an-uncertain-st.md)
