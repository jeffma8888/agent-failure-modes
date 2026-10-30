---
id: INC-0129
title: A syntax hygiene rule flagging every literal timer over one second also flagged a cancellation watchdog
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0129 - A syntax hygiene rule flagging every literal timer over one second also flagged a cancellation watchdog

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

A rule against long timers rejects a bound that fails and is cleared.

## What happened

A hygiene rule that flagged every literal timer over one second also flagged a cancellation watchdog that bounds an awaited event.

## Root cause

The rule matched surface syntax, not whether the timer is a sleep.

## Why it was hard to see

The watchdog and a sleep look the same in syntax.

## Fix

Distinguish a cleared, failing bound from a sleep.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A hygiene rule should test intent, not only syntax.

## Related

[INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md)
