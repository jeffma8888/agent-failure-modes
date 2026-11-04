---
id: INC-0569
title: Denying unexplained loopback connects in an egress observer broke the app, and the agent stopped instead of widening
date: 2026-11-04
classes: [detector-fail-closed]
severity: medium
status: mitigated
---

# INC-0569 - Denying unexplained loopback connects in an egress observer broke the app, and the agent stopped instead of widening

**Cost:** None to the product. The run was stopped, and the rule was refined only after the listeners were attributed.

## Signature - how you recognise it

A strict denial rule blocks connects the application makes to its own native listeners.

## What happened

A rerun of the egress observer with the owned-listener rule on the unchanged base still denied 47 loopback connects that had no Node-side listen record, plus telemetry and registry requests. Denying them broke the app: admin login timed out. The agent stopped instead of widening the allowlist. The lead ruled to attribute the listeners first: query the operating system for the listening socket on each denied port during one run, cite the installed source that opens and connects to it, and extend the rule only if every listener belongs to a process with a ready record in the same tree, with the query output recorded before the allow. A query failure, a timeout or a listener owned by another process is denied, and if any listener is outside the tree, stop.

## Root cause

The listeners were opened from native code that the Node-level observer cannot see.

## Why it was hard to see

A denial that breaks the app can look like a defect of the app.

## Fix

Stop, then attribute each listener from the operating system and the installed source.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not widen an egress allowlist to make the app work; attribute each listener by an operating system query, and allow only listeners owned by instrumented processes.

## Related

[INC-0562](./INC-0562-the-first-real-run-of-a-new-egress-observer-on-unchanged-mai.md)
