---
id: INC-0200
title: A sandbox permission failure was at risk of reading as a code defect
date: 2026-10-30
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0200 - A sandbox permission failure was at risk of reading as a code defect

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The red had nothing to do with the code.

## What happened

A review fast run failed because the sandbox denied nested process listing, which looks like a code failure.

## Root cause

A review fast run failed because the sandbox denied nested process listing, which looks like a code failure.

## Why it was hard to see

The error appears at the stage, not at the permission.

## Fix

Say so, do not retry around it, and get the run from an environment that permits it (the lead reran in the permitted profile)

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Treat a permission-denied run as missing evidence and rerun it where it is permitted

## Related

[INC-0179](./INC-0179-a-chat-pre-approval-did-not-lift-an-explicit-approval-rule.md)
