---
id: INC-0369
title: A bare syntax check resolved to a different runtime that ignored the flag and executed the script
date: 2026-11-01
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0369 - A bare syntax check resolved to a different runtime that ignored the flag and executed the script

**Cost:** Minor: nothing ran, because the script refused at its first statement.

## Signature - how you recognise it

A syntax-check command executed the script it was meant only to parse.

## What happened

the lead syntax-checked a prepared browser walk script with a bare interpreter command and a check flag. In the tool shell the bare name resolved to a different runtime that ignores the flag and executes the file. The script's first statement refused because two required environment paths were unset, so nothing ran

## Root cause

a bare command name was trusted to resolve to the pinned interpreter, and a flag was trusted to mean the same thing in whatever runtime answered

## Why it was hard to see

The command looked like a pure check, the other runtime accepted it silently, and only the script's own early refusal prevented an externally visible run.

## Fix

Run syntax checks with the pinned binary by absolute path; every script that can act externally refuses at its first line without its required environment

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run syntax checks with the pinned binary by absolute path, and make every script that can act externally refuse at its first line without its required environment

## Related

[INC-0249](./INC-0249-a-cd-to-a-path-in-a-variable-was-refused-by-the-sandbox.md) [INC-0094](./INC-0094-macos-sandbox-exec-refused-to-exec-a-setuid-binary-so-a-sand.md)
