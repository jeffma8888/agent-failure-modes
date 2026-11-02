---
id: INC-0347
title: A final print in a wrapper replaced the command's failure with success
date: 2026-11-01
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0347 - A final print in a wrapper replaced the command's failure with success

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A generated run script ended with a print statement and no explicit exit, so a red gate returned zero.

## What happened

a generated run script invoked the guarded gate, then printed the status with a print statement and no explicit exit; the script returned the print's zero, so a red gate, a dependency mutation or a timeout would end with an outer exit of zero

## Root cause

a generated run script invoked the guarded gate, then printed the status with a print statement and no explicit exit; the script returned the print's zero, so a red gate, a dependency mutation or a timeout would end with an outer exit of zero

## Why it was hard to see

The status is printed and recorded, which looks like reporting it, while the process exit is a different channel.

## Fix

Save the status on the next line, write the record, exit with the saved status, stop nonzero if evidence writing fails, and prove it with stub controls for each nonzero class

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> In a wrapper, save the exit status on the very next line and end with an explicit exit of it; prove a nonzero child makes the wrapper nonzero

## Related

[INC-0051](./INC-0051-a-fallible-edit-script-followed-by-a-semicolon-let-the-commi.md) [INC-0120](./INC-0120-a-guard-control-asserted-only-exit-0-so-a-warn-and-pass-guar.md)
