---
id: INC-0604
title: A row runner selected by family while the brief named a revision, so the run stopped before the harness
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0604 - A row runner selected by family while the brief named a revision, so the run stopped before the harness

**Cost:** One run stopped before the harness started.

## Signature - how you recognise it

A run stops at row selection with an unknown row name.

## What happened

The activation stopped before the harness. The row runner knows rows by family, so the row name is the family name and not the revision name. The brief named the revision, which was an adapter defect in the lead's brief. The author reran with the family name once and listed every selected spec and case.

## Root cause

The brief named a revision where the runner takes a family.

## Why it was hard to see

The revision name is correct for the identity map and wrong for the runner.

## Fix

Run the row by family name once and list every spec and case it selects.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before briefing a row run, check which name the runner takes, family or revision, and list the selected specs and cases.

## Related

[INC-0592](./INC-0592-a-static-triage-found-four-open-rows-already-done-by-named-m.md)
