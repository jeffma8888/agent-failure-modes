---
id: INC-0385
title: Two engineers answered the same STOP diagnosis independently, and agreeing answers let the lead route at once
date: 2026-11-01
classes: [delegation]
severity: low
status: fixed
---

# INC-0385 - Two engineers answered the same STOP diagnosis independently, and agreeing answers let the lead route at once

**Cost:** Routing waited on one diagnosis fewer rounds because two independent answers agreed.

## Signature - how you recognise it

A STOP had an unknown cause and a single diagnosis would have been unchecked.

## What happened

two engineers answered the same STOP diagnosis independently and in parallel; their agreeing answers let the lead route the fix at once

## Root cause

one answer to an unknown cause cannot be told apart from a plausible guess

## Why it was hard to see

Agreement between independent answers is the only cheap signal available before running anything.

## Fix

When a STOP cause is unknown, ask two engineers for independent static answers and route when they agree

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a STOP cause is unknown, ask for two independent static answers before routing the fix

## Related

[INC-0379](./INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md)
