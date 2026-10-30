---
id: INC-0105
title: A function signature named in the plan but never called by any test shipped ignoring its second argument
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0105 - A function signature named in the plan but never called by any test shipped ignoring its second argument

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

The plan names a parameter that no test exercises.

## What happened

A function signature named in the plan had no test that called it with the second argument, so it could ship silently ignoring that argument.

## Root cause

The signature belonged to a row whose tests never used it.

## Why it was hard to see

Everything passes, and the unused parameter is never observed.

## Fix

Move the signature to the row whose test first calls it, or add the test.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Every planned parameter needs a test that makes it matter.
