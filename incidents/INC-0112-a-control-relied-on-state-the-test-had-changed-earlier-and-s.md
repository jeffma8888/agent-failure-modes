---
id: INC-0112
title: A control relied on state the test had changed earlier and silently became vacuous
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0112 - A control relied on state the test had changed earlier and silently became vacuous

**Cost:** Minor: caught by a stop rule, an audit or review before it shipped.

## Signature - how you recognise it

A control that depends on a signed-in or seeded state runs after the test changed that state.

## What happened

A control relied on state the test had altered earlier, such as a signed-out user, so it could no longer fail.

## Root cause

The control was placed after a state change and was not compared against its own before state.

## Why it was hard to see

The test stays green and the control looks present.

## Fix

Compare before and after inside the same state.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Place a control in the state it needs, and show it can change.

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md)
