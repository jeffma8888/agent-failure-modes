---
id: INC-0290
title: A setup hook was sized from file time, or from a refused attempt
date: 2026-11-01
classes: [false-green, stage-timeout]
severity: medium
status: fixed
---

# INC-0290 - A setup hook was sized from file time, or from a refused attempt

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A hook timeout was chosen without measuring the hook itself.

## What happened

file totals include server start and teardown, and an attempt refused at preflight ran nothing; neither is a measurement of the setup hook

## Root cause

file totals include server start and teardown, and an attempt refused at preflight ran nothing; neither is a measurement of the setup hook

## Why it was hard to see

File time is easy to read and a refused attempt still produces output.

## Fix

Time the hook with an observation-only instrument outside the candidate, cross-check against runner totals, disclose the instrument, and size from recorded evidence when the author cannot run the file

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure the hook itself, count only runs that executed, and mark owed measurements as owed

## Related

[INC-0195](./INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md)
