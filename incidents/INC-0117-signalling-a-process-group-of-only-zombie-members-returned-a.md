---
id: INC-0117
title: Signalling a process group of only zombie members returned a permission error on macOS
date: 2026-10-30
classes: [concurrency, tooling-paths]
severity: medium
status: fixed
---

# INC-0117 - Signalling a process group of only zombie members returned a permission error on macOS

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

Cleanup fails intermittently when the group has exited but not been reaped.

## What happened

On macOS, signalling a process group whose members were all zombies could return a permission error, and cleanup treated it as a failure. The race showed only over repeated runs.

## Root cause

The error code was read as a real denial instead of a gone group.

## Why it was hard to see

It is a race, so a single run usually passes.

## Fix

Treat that permission error as the group being gone, and run the test repeatedly to expose the race.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Repeat race-dependent cleanup tests; classify errors by what they mean for the target.

## Related

[INC-0092](./INC-0092-a-whole-group-termination-grace-period-was-shorter-than-the.md)
