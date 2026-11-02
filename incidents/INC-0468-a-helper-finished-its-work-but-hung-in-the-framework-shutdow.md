---
id: INC-0468
title: A helper finished its work but hung in the framework shutdown call, and its pass line came after the shutdown, so no evidence printed
date: 2026-11-02
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0468 - A helper finished its work but hung in the framework shutdown call, and its pass line came after the shutdown, so no evidence printed

**Cost:** About ten minutes of waiting and one substitute evidence ruling.

## Signature - how you recognise it

A step did its work and then sat idle with no output.

## What happened

a helper set a password and wrote its credentials file, then hung for about ten minutes in the framework shutdown call, whose pool waited on a connection that was never released; its pass line was written after the shutdown, so no evidence printed; the lead diagnosed it read only from the file modification time, the row update time and an idle database session, and then stopped the exact recorded process id

## Root cause

the pass line was written after a shutdown call that can wait forever

## Why it was hard to see

The work was finished and visible only in side effects, so the process looked slow, not stuck.

## Fix

write the evidence line before the shutdown, bound the shutdown with a fixed timeout, and exit explicitly with a zero code on pass and two otherwise, so an open pool can never hold the process; the timeout and exit path are part of the non author check

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write the evidence line before any shutdown call, bound the shutdown with a timeout, and exit explicitly

## Related

[INC-0254](./INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md) [INC-0060](./INC-0060-a-probe-hung-on-a-background-child-that-held-the-pipe-and-th.md) [INC-0155](./INC-0155-a-kill-rehearsal-met-its-timeout-but-nobody-checked-what-the.md)
