---
id: INC-0140
title: A known red was listed before checking the scan roots of the hygiene rule that raised it
date: 2026-10-30
classes: [detector-fail-open, observability]
severity: medium
status: fixed
---

# INC-0140 - A known red was listed before checking the scan roots of the hygiene rule that raised it

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A finding is recorded as a known failure without confirming the rule scans that file.

## What happened

A hygiene rule finding was listed as a known red before its scan roots were checked.

## Root cause

The finding was trusted without confirming the rule scope.

## Why it was hard to see

A rule report looks authoritative.

## Fix

Check the rule scan roots before listing one of its findings as a known red.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Confirm a rule scope before reporting its finding.

## Related

[INC-0129](./INC-0129-a-syntax-hygiene-rule-flagging-every-literal-timer-over-one.md)
