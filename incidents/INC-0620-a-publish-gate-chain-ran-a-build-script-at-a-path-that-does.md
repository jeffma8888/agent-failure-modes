---
id: INC-0620
title: A publish gate chain ran a build script at a path that does not exist, printed the failing exit status and carried on to the export and the leak scan
date: 2026-11-04
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0620 - A publish gate chain ran a build script at a path that does not exist, printed the failing exit status and carried on to the export and the leak scan

**Cost:** None. The slip was caught by reading the output before the push, and the gate was rerun with the right path.

## Signature - how you recognise it

A chained gate prints a non-zero status for one step and still runs the steps after it.

## What happened

In the corpus push gate the lead called the build script at the repository root, where it does not exist, and it exited 2. The call sat inside one chained command that printed each exit status and carried on to the export and the leak scan. It was caught on reading the output before the push, and the build was rerun at its real path, exit 0 twice with an empty porcelain.

## Root cause

The chain printed statuses and did not stop on them.

## Why it was hard to see

Later steps ran and looked fine, so the chain finished with output that read like a pass.

## Fix

Join gate steps with && or run them in fail-fast shell mode so the first failure stops the rest, use the real script path, and read the output before pushing.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A gate chain stops at the first failed step; a printed status is not a check.

## Related

[INC-0611](./INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md) [INC-0605](./INC-0605-corpus-commits-sat-unpushed-after-the-gate-and-a-push-was-an.md)
