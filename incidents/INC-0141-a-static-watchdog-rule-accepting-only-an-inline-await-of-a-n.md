---
id: INC-0141
title: A static watchdog rule accepting only an inline await of a new promise flagged stored promises and other valid shapes
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0141 - A static watchdog rule accepting only an inline await of a new promise flagged stored promises and other valid shapes

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A rule written against one syntax shape rejects equivalent valid code.

## What happened

A static watchdog rule that accepted only an inline await new Promise flagged stored promises, outer let handles, catch-reject-return branches and Playwright test.setTimeout.

## Root cause

The rule matched one shape instead of the intent.

## Why it was hard to see

Rewriting every root to fit looks simpler than widening the rule.

## Fix

Widen by shape with near-miss negatives instead of rewriting every root.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Widen a rule by shape and prove it with near-miss negatives.

## Related

[INC-0129](./INC-0129-a-syntax-hygiene-rule-flagging-every-literal-timer-over-one.md)
