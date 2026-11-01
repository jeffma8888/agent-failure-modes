---
id: INC-0246
title: A short password check created the one-time account instead of showing an error
date: 2026-11-01
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0246 - A short password check created the one-time account instead of showing an error

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The probe succeeded and consumed the one-time form.

## What happened

The create-first-user form has no minimum password length, so a short password check created the account.

## Root cause

The create-first-user form has no minimum password length, so a short password check created the account.

## Why it was hard to see

The error case never showed.

## Fix

Put that check last, or run length and mismatch checks on the change-password form

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run destructive checks on a one-time form last, and use a repeatable form for validation checks

## Related

[INC-0241](./INC-0241-automated-tests-passed-while-nobody-had-walked-the-real-site.md)
