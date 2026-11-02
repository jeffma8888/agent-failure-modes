---
id: INC-0396
title: A multi-step command reported success for its later steps while its middle step had not happened
date: 2026-11-02
classes: [false-green]
severity: medium
status: fixed
---

# INC-0396 - A multi-step command reported success for its later steps while its middle step had not happened

**Cost:** A plan sat uncommitted while later steps looked complete.

## Signature - how you recognise it

A command's final output said done while one step had never run.

## What happened

a multi-step command reported success for its later steps while its middle step, the plan commit, had not happened; this was found only by checking tree status after a context reset

## Root cause

success was read from the end of the command, and the middle step had failed silently

## Why it was hard to see

The later steps ran and printed normally, which hid the missing commit.

## Fix

Verify each landing by the commit log, not by the command's last line

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify each landing by the commit log, never by the last line of the command

## Related

[INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md) [INC-0389](./INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md)
