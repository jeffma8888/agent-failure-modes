---
id: INC-0622
title: An unbraced shell variable followed by a colon and a letter was read as a history modifier, so a revision was mangled and the hash printed was of empty input
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0622 - An unbraced shell variable followed by a colon and a letter was read as a history modifier, so a revision was mangled and the hash printed was of empty input

**Cost:** One check printed a hash of nothing, caught as the well-known empty-input hash.

## Signature - how you recognise it

A hash printed for a path read from a revision equals the hash of empty input.

## What happened

In zsh, a variable written without braces and followed by a colon and a letter was parsed as a modifier (the tail modifier keeps the last path part). The revision passed to the show command was mangled, the command failed, and the hash printed was the hash of empty input.

## Root cause

The shell treats a colon after an unbraced variable as the start of a modifier.

## Why it was hard to see

The failed command printed an error that was easy to miss, and the hash printed looked like any other digest.

## Fix

Brace the variable before the colon, and treat the empty-input hash as a failure signal.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Brace variables before a colon, as in ${r}:path, and treat the hash of empty input as a failure signal.

## Related

[INC-0607](./INC-0607-a-sandboxed-shell-refused-a-directory-change-whose-target-wa.md) [INC-0620](./INC-0620-a-publish-gate-chain-ran-a-build-script-at-a-path-that-does.md)
