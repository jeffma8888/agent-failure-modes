---
id: INC-0581
title: A brief named the revision id as the row, and the row runner refused before any test ran
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
topic: tooling-paths/argument-read-as-other-kind
occurrences: 2
---

# INC-0581 - A brief named the revision id as the row, and the row runner refused before any test ran

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [A helper or runner reads your argument as a different kind or name](../catalog/tooling-paths/argument-read-as-other-kind.md)

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

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0604](./INC-0604-a-row-runner-selected-by-family-while-the-brief-named-a-revi.md) - 2026-11-04 - A row runner selected by family while the brief named a revision, so the run stopped before the harness

## Related

[INC-0546](./INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md)
