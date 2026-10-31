---
id: INC-0217
title: A fixed test count in an exit criterion went stale
date: 2026-10-31
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0217 - A fixed test count in an exit criterion went stale

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The count no longer matched the suite.

## What happened

A fixed test count written into an exit criterion goes stale as the suite moves.

## Root cause

A fixed test count written into an exit criterion goes stale as the suite moves.

## Why it was hard to see

The number was right when written.

## Fix

State the exit as the full active inventory of the exact tree with zero failed or skipped, and name the qualifying-run rule (start load at least 10, no overlapping FULL), disclosing excluded runs instead of discarding them

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> State an exit as the full active inventory with zero failed or skipped, name the qualifying-run rule, and disclose excluded runs

## Related

[INC-0209](./INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md)
