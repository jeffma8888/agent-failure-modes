---
id: INC-0581
title: A brief named the revision id as the row, and the row runner refused before any test ran
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0581 - A brief named the revision id as the row, and the row runner refused before any test ran

**Cost:** None. The result was recorded as not run.

## Signature - how you recognise it

A runner receives a revision id where it expects the base row name.

## What happened

The row runner takes the base row, never the revision id. A brief named the revision id, and the runner refused with a row selection error before any test ran. The lead recorded that as not run, never a red, and ruled that briefs name the base row.

## Root cause

The brief used the identity name of the root, not the name the runner selects by.

## Why it was hard to see

A refusal before any test looks like a failure of the test.

## Fix

Name the base row in briefs, and record a selection error as not run.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A runner selection error before any test is not run, never a red; briefs name the base row.

## Related

[INC-0546](./INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md)
