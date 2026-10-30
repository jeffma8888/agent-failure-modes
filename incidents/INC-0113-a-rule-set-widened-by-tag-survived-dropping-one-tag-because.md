---
id: INC-0113
title: A rule set widened by tag survived dropping one tag because only some tags had a planted violation
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0113 - A rule set widened by tag survived dropping one tag because only some tags had a planted violation

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

A check covers several tags, and removing one tag leaves the suite green.

## What happened

A rule set was widened by tag, and without a planted violation for each tag, dropping a tag went unnoticed.

## Root cause

Coverage of the rule set was assumed from the widened list.

## Why it was hard to see

The list reads as complete, and the omitted tag has no failing case.

## Fix

Plant one violation per tag.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Every tag in a rule needs its own planted violation.

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) [INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
