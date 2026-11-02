---
id: INC-0480
title: A push gate that piped the test run into a trimming command would have pushed even if the tests had failed
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0480 - A push gate that piped the test run into a trimming command would have pushed even if the tests had failed

**Cost:** None: the tests happened to pass, so nothing bad shipped; the gate was simply not a gate.

## Signature - how you recognise it

A gating command was piped, so the gate read the last command status.

## What happened

A push gate was written as run the tests, pipe the output to a trimming command, and push on success. The exit status of a pipeline is the last command status, so the trimming command succeeding would have let the push run even if the tests failed. The tests passed, so nothing bad shipped.

## Root cause

The pipeline reported the status of the last command, not of the tests.

## Why it was hard to see

The command line reads naturally and passes every time the tests pass, so the gap shows only on a failing run.

## Fix

Never pipe a gating command; capture its exit status first, with the pipefail option, or by writing the output to a file, checking the status, and then reading the file.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never pipe a gating command; capture its exit status first, by pipefail or by writing to a file and checking the status before reading the file.

## Related

[INC-0357](./INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md) [INC-0347](./INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md) [INC-0389](./INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md)
