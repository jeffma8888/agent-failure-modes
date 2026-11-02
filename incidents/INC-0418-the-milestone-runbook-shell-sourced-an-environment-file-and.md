---
id: INC-0418
title: The milestone runbook shell-sourced an environment file and failed before the build on a value with angle brackets
date: 2026-11-02
classes: [ipc-and-env]
severity: low
status: fixed
---

# INC-0418 - The milestone runbook shell-sourced an environment file and failed before the build on a value with angle brackets

**Cost:** The first walk attempt failed before the build and was rerun.

## Signature - how you recognise it

The runbook failed at its first step on a value the shell parsed as syntax.

## What happened

the milestone runbook shell-sourced an environment file and failed before the build on a value with angle brackets; reading the file line by line fixed it

## Root cause

the shell interpreted characters inside a value as syntax

## Why it was hard to see

The same file worked as data and failed as code.

## Fix

read the environment file line by line and never shell-source it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read an environment file line by line, never shell-source it; a value with angle brackets breaks sourcing

## Related

[INC-0248](./INC-0248-the-env-script-could-not-be-sourced-in-zsh.md)
