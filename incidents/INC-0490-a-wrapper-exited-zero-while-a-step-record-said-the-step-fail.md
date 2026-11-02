---
id: INC-0490
title: A wrapper exited zero while a step record said the step failed
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0490 - A wrapper exited zero while a step record said the step failed

**Cost:** None incurred: the exit status was not trusted; reading it alone would have recorded a red run as green.

## Signature - how you recognise it

The wrapper exit status was zero and one step record said failed by timeout.

## What happened

A full-suite run went through a wrapper script. Every step passed up to the server integration step, which failed by its step timeout with all but two cases passed and none failed, and the smoke and browser steps never ran. The wrapper still exited zero. The step records were the truth, and they showed a run that was red by timeout only. The cause was the step budget, not a test.

## Root cause

The wrapper reports that it finished, not that its steps passed, so its exit status carries no verdict on the steps.

## Why it was hard to see

An exit code of zero is the signal most tools and people read first, and the failed step was one line among many passed ones.

## Fix

Gate on each step record, state which steps ran, passed, failed and did not run, and trace the failing step to its cause before ruling.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Gate on the step records, never on the wrapper exit status; a wrapper can exit zero while a step record says failed.

## Related

[INC-0347](./INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md)
