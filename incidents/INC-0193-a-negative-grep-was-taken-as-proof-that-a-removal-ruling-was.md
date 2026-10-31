---
id: INC-0193
title: A negative grep was taken as proof that a removal ruling was complete
date: 2026-10-30
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0193 - A negative grep was taken as proof that a removal ruling was complete

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The forbidden token was gone and the duty remained.

## What happened

A grep found no forbidden token left and was read as proof that a removal ruling was complete, while named duties and their follow-through lines remained.

## Root cause

A grep found no forbidden token left and was read as proof that a removal ruling was complete, while named duties and their follow-through lines remained.

## Why it was hard to see

Absence of a token is not absence of the duty.

## Fix

Check every named duty and its follow-through lines

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check each named duty and its follow-through lines; a negative grep alone proves nothing

## Related

[INC-0177](./INC-0177-card-text-pointed-at-its-own-directory-as-the-checkout.md)
