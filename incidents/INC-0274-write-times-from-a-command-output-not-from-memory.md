---
id: INC-0274
title: Write times from a command output, not from memory
date: 2026-11-01
classes: [observability, spec-and-scope]
severity: medium
status: fixed
---

# INC-0274 - Write times from a command output, not from memory

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An evidence line recorded a time that was not read from a clock.

## What happened

an evidence line first carried a clock time written before the clock was checked; the lead corrected it

## Root cause

an evidence line first carried a clock time written before the clock was checked; the lead corrected it

## Why it was hard to see

A remembered time feels certain.

## Fix

Write times from a command output, not from memory

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write a recorded time from a command output, never from memory

## Related

[INC-0259](./INC-0259-sum-every-runner-the-earlier-record-summed.md)
