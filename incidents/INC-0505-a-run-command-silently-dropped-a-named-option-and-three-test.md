---
id: INC-0505
title: A run command silently dropped a named option, and three tests that ran it asserted only things that are true for the full data set too
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0505 - A run command silently dropped a named option, and three tests that ran it asserted only things that are true for the full data set too

**Cost:** The full data set loaded where the minimal one was requested, and no test failed; the defect was found only by reading installed source.

## Signature - how you recognise it

A test runs a command with an option and asserts exit status, timing and a side marker, all of which hold with or without the option.

## What happened

A framework run command rebuilt the script argument list from positional arguments only, so a named option was dropped before the script saw it, and the full data set loaded instead of the minimal one. Three tests ran that command and asserted exit status, timing records and the presence of one user, all true for the full set as well. A fourth test called the function directly and skipped the entry point.

## Root cause

The tests checked that the command ran, not what it produced, and the one test aimed at the option bypassed the entry point where the option was lost.

## Why it was hard to see

The command exited zero, the timings were valid and the expected user existed, so every visible signal was green; only the row counts differed.

## Fix

Pass the option in a way the run command keeps. Add a test that runs the real entry point on an empty database, reads its report, asserts the minimal counts, then reruns and asserts nothing new was created.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that exercises an option goes through the real entry point and asserts an observable effect that differs with and without the option; exit 0 and side markers are not evidence the option took effect.

## Related

[INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) [INC-0497](./INC-0497-a-flag-that-hides-the-token-from-responses-left-first-user-r.md)
