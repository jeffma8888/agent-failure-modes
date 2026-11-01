---
id: INC-0244
title: A correct not-found page was served with a 200 status
date: 2026-11-01
classes: [false-green, observability]
severity: medium
status: fixed
---

# INC-0244 - A correct not-found page was served with a 200 status

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The page looked right and the status was wrong.

## What happened

A not-found page rendered correctly while the response status was 200, and no test checked both.

## Root cause

A not-found page rendered correctly while the response status was 200, and no test checked both.

## Why it was hard to see

The body is what a person sees.

## Fix

Make the defect a failing QA root first, then fix it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Assert the response status and the rendered body together

## Related

[INC-0265](./INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md)
