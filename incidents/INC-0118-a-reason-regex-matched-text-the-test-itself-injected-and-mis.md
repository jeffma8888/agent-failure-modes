---
id: INC-0118
title: A reason regex matched text the test itself injected and missed the reason on the error line
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0118 - A reason regex matched text the test itself injected and missed the reason on the error line

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

A refusal assertion passes because its pattern matches the test input.

## What happened

A reason regex matched text the test had injected, and did not require the reason on the same line as the error name.

## Root cause

The pattern was broad and not anchored to the error output.

## Why it was hard to see

The assertion passes with any failure that echoes the input.

## Fix

Make the regex unable to match injected text, and require the reason on the same line as the error name.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Anchor a reason match to the error line and keep injected text out of its reach.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
