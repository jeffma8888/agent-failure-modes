---
id: INC-0166
title: A conditional omission could hide behind a helper, an alias or an early return
date: 2026-10-30
classes: [detector-fail-open, test-isolation]
severity: medium
status: fixed
---

# INC-0166 - A conditional omission could hide behind a helper, an alias or an early return

**Cost:** Minor: caught in review before it shipped.

## Signature - how you recognise it

A hygiene rule allowed omissions that took registrations out of a suite.

## What happened

A guarded registration inside a non-describe callback or helper, the suite alias of describe, and a conditional return in a describe body each omit registrations without being flagged by a narrower rule.

## Root cause

The rule covered the direct describe shapes only.

## Why it was hard to see

Each shape is legal code and omits tests quietly.

## Fix

Flag a guarded registration anywhere, flag suite like describe, and flag a conditional return or throw in a describe body; an unconditional return at the end is allowed (R-BQ).

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Forbid conditional omission anywhere, with the same alias resolution as describe.

## Related

[INC-0151](./INC-0151-a-hygiene-rule-against-conditional-test-omission-needed-a-pr.md)
