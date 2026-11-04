---
id: INC-0586
title: A waiter whose helper could not open its guard spun to the wait limit with tracebacks, and a malformed owner record was skipped silently
date: 2026-11-04
classes: [observability]
severity: medium
status: mitigated
---

# INC-0586 - A waiter whose helper could not open its guard spun to the wait limit with tracebacks, and a malformed owner record was skipped silently

**Cost:** None. Both were blocking findings of the review.

## Signature - how you recognise it

A failure to open the guard and an unreadable owner record produce no report that names a manual step.

## What happened

A waiter whose helper could not use its guard path kept trying until the wait limit with tracebacks and never reported a manual step. A published owner with an empty process id and an undecodable stage start time were skipped silently. The ruling requires a distinct prompt not-run exit with the manual-step marker and the exact path when the helper cannot run, and a manual step for every owner or stage identity that cannot be proved.

## Root cause

Failure paths had no explicit report; they fell through to retry or skip.

## Why it was hard to see

A silent skip looks like an absent record.

## Fix

Report a manual step with the exact path when the guard or an identity cannot be proved, and exit promptly.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a guard or an owner identity cannot be proved, exit promptly with a manual step naming the exact path; never spin or skip silently.

## Related

[INC-0575](./INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md)
