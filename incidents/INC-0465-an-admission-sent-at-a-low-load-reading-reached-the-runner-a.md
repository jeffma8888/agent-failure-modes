---
id: INC-0465
title: An admission sent at a low load reading reached the runner after the load rose again, and the runner fresh reading then refused it
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0465 - An admission sent at a low load reading reached the runner after the load rose again, and the runner fresh reading then refused it

**Cost:** A delayed run and one more admission.

## Signature - how you recognise it

A runner refused a step that had just been admitted.

## What happened

an admission was sent at a low load reading, but it reached the runner after the window closed and the load had risen by about ten within a minute; the runner read load fresh at its first step, saw a value above the gate and refused; the refusal was correct under the rule as written, and the cause was the gap between the admission and the reading

## Root cause

the admission and the runner reading were two gates a minute apart on a host whose load swings fast

## Why it was hard to see

Both the admission and the refusal followed the rule, so nobody was at fault.

## Fix

treat the runner reading taken within 60 seconds of the admission message as a record, not a second gate: launch even above the gate and label any later timeout load suspect; a reading taken later than 60 seconds after the message is a fresh gate

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An admission admits the step: a reading within 60 seconds of the admission is a record, and a reading after that is a fresh gate

## Related

[INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) [INC-0417](./INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) [INC-0452](./INC-0452-a-ruling-cannot-override-a-teammate-tool-rules-so-the-lead-s.md)
