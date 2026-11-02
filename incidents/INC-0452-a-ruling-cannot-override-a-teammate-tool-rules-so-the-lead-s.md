---
id: INC-0452
title: A ruling cannot override a teammate tool rules, so the lead sleep loop load waiter was refused and withdrawn
date: 2026-11-02
classes: [delegation]
severity: low
status: fixed
---

# INC-0452 - A ruling cannot override a teammate tool rules, so the lead sleep loop load waiter was refused and withdrawn

**Cost:** None: the refusal came before any run, and the helper was withdrawn.

## Signature - how you recognise it

A ruled helper was refused by the teammate it was meant for.

## What happened

the lead ruled a load wait helper built as a sleep loop, and the runner was right to refuse it because teammate tool rules forbid sleep loops and a ruling does not override those rules; the helper was withdrawn

## Root cause

the ruled helper needed an action the teammate tool rules forbid

## Why it was hard to see

Rules from the host and rules from the lead look equal, and only the host rules bind a teammate.

## Fix

gate load by admission: the lead observer wakes the lead when load is low, the lead sends the runner an admitted message, and the runner checks load once, fresh, at its first step, then records load before later steps without stopping; a timeout failure recorded at load 14 or above is labeled load suspect and rerun; full test, database and migration runs keep one fresh start gate under 14

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Wait for load with an event driven observer owned by the lead, never a sleep loop in a teammate; a ruling does not override a teammate tool rules

## Related

[INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) [INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) [INC-0450](./INC-0450-a-load-gate-stop-was-the-right-call-and-cost-nothing-because.md)
