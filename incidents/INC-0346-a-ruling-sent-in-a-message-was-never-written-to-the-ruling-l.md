---
id: INC-0346
title: A ruling sent in a message was never written to the ruling log
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0346 - A ruling sent in a message was never written to the ruling log

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A reviewer found a ruling missing from the log, and it had to be reconstructed from message text with a caveat.

## What happened

a ruling was sent to a worker in a job message but not appended to the ruling log; a reviewer flagged it missing and the plan author had to record it from the job text with a caveat

## Root cause

a ruling was sent to a worker in a job message but not appended to the ruling log; a reviewer flagged it missing and the plan author had to record it from the job text with a caveat

## Why it was hard to see

The recipient acted on it, so the ruling looks complete, while every other reader sees nothing.

## Fix

Append the ruling at once with the real time

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write a ruling into the log in the same step as sending it; a ruling that exists only in a message is invisible to every other reader

## Related

[INC-0337](./INC-0337-reviewers-named-at-ruling-time-were-busy-when-the-artifact-l.md) [INC-0302](./INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md) [INC-0350](./INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) [INC-0358](./INC-0358-a-restated-rule-gained-a-qualifier-the-original-ruling-never.md)
