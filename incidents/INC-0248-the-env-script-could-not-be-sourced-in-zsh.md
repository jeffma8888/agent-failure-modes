---
id: INC-0248
title: The env script could not be sourced in zsh
date: 2026-11-01
classes: [tooling-paths, ipc-and-env]
severity: medium
status: fixed
---

# INC-0248 - The env script could not be sourced in zsh

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The checker ran without its environment.

## What happened

zsh cannot source the env script, so a checker run directly in zsh lacked its environment.

## Root cause

zsh cannot source the env script, so a checker run directly in zsh lacked its environment.

## Why it was hard to see

The script works in the shell it was written for.

## Fix

Run checkers through bash -c

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run checkers through bash -c when the env script is not zsh-compatible

## Related

[INC-0165](./INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md) [INC-0362](./INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md) [INC-0418](./INC-0418-the-milestone-runbook-shell-sourced-an-environment-file-and.md) [INC-0454](./INC-0454-a-file-creation-mask-from-an-earlier-tool-call-did-not-carry.md)
