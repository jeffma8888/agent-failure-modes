---
id: INC-0444
title: A static closure packet that did not converge in three rounds was replaced by running the thing and diagnosing the receipts
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: fixed
---

# INC-0444 - A static closure packet that did not converge in three rounds was replaced by running the thing and diagnosing the receipts

**Cost:** Three review rounds were spent before the approach changed.

## Signature - how you recognise it

Static review rounds kept finding the same open items.

## What happened

a static closure packet for a heavy run did not converge in three review rounds, with the same closure items still partly open, and the target had also gone stale against newer main; the lead retired it and ruled to run the regression tier on current main, keeping the reusable parts and diagnosing any unexpected failure from the run's own receipts instead of a deep static census

## Root cause

a census by reading cannot settle what only a run shows

## Why it was hard to see

Each round made progress, so another round always looked worthwhile.

## Fix

cap static review rounds on a closure packet; when it does not converge, run the thing on current code and diagnose from the receipts

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a static closure packet does not converge in three rounds, replace it by running the thing on current code and diagnosing the receipts

## Related

[INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md) [INC-0385](./INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md)
