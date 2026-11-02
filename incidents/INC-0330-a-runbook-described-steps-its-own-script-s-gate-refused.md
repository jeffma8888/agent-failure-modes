---
id: INC-0330
title: A runbook described steps its own script's gate refused
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0330 - A runbook described steps its own script's gate refused

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The documented run record failed the script's gate because the gate wanted a second record with other keys.

## What happened

the runbook described one run record shape while the script's gate demanded a second record with different keys, so the steps could not pass as written

## Root cause

the runbook described one run record shape while the script's gate demanded a second record with different keys, so the steps could not pass as written

## Why it was hard to see

The text and the script were each reviewed alone, and nobody ran the steps through the gates.

## Fix

Walk every runbook step through the script's gates offline before calling the runbook ready

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Walk every runbook step through the script's gates offline before calling the runbook ready

## Related

[INC-0302](./INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md) [INC-0076](./INC-0076-a-teammate-s-write-boundary-contradicted-the-charter-s-file.md)
