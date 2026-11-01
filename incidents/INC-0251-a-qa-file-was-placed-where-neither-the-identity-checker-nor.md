---
id: INC-0251
title: A QA file was placed where neither the identity checker nor the project would take it
date: 2026-11-01
classes: [spec-and-scope, delegation]
severity: medium
status: fixed
---

# INC-0251 - A QA file was placed where neither the identity checker nor the project would take it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The file was never collected.

## What happened

A QA root placed its file under an app test folder, outside the destinations the identity checker accepts and the pattern the unit project collects.

## Root cause

A QA root placed its file under an app test folder, outside the destinations the identity checker accepts and the pattern the unit project collects.

## Why it was hard to see

The brief named the row, not the destination rules.

## Fix

State the allowed destination prefixes and file suffix in every QA brief

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Every QA brief states the allowed destination prefixes and file suffix

## Related

[INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md)
