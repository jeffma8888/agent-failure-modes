---
id: INC-0488
title: Static review rounds on a test harness left the same findings open
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0488 - Static review rounds on a test harness left the same findings open

**Cost:** Minor: several review rounds spent on a harness that had not yet been run.

## Signature - how you recognise it

Two static passes ended with the same four findings still open.

## What happened

A browser walk harness went through a static review in which the reviewer found four amendments, the author applied them in place, and the recheck still left all four open after two passes. The loop was not converging fast enough for the duty that depended on it. The decision was to close the reviewer's executable gaps in one bounded pass and, in parallel, to run the harness once as a diagnostic against a scratch server and scratch database, labelled as neither a baseline nor an acceptance run, where a refusal at the binding step counts as a valid result.

## Root cause

Reading a harness cannot show what it does when run, so each round re-derived the same open findings from text.

## Why it was hard to see

Every round produced real findings and a revision, so the loop looked productive, and nothing in it said when to stop reading and run.

## Fix

After two static rounds that leave the same findings open, run the harness once on scratch state under a load limit, label the run as a diagnostic, and read what it observed.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When static review rounds on a harness converge slowly, run one labelled diagnostic early, on scratch state, with its result marked as neither a baseline nor an acceptance run, to learn what is really wrong.

## Related

[INC-0444](./INC-0444-a-static-closure-packet-that-did-not-converge-in-three-round.md)
