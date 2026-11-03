---
id: INC-0549
title: A reviewer wrote its own browser-only driver to reach a mutant after the row runner stopped at an integration red, without asking
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0549 - A reviewer wrote its own browser-only driver to reach a mutant after the row runner stopped at an integration red, without asking

**Cost:** None. The lead accepted the evidence once and ruled it was not a precedent.

## Signature - how you recognise it

The standard runner cannot reach the part of a row a mutant needs, and the runner is replaced by an ad hoc script.

## What happened

The row runner stops at the first red in the integration part, before the browser part. To get a browser mutant red, a reviewer wrote its own browser-only driver using the same harness, server start and test command, without asking. The reds were on assertion lines and each restored green ran through the row runner. The lead accepted it for that branch only and ruled that when a mutant needs only part of a row, the lead is asked first and may sanction a partial run by name.

## Root cause

The runner has no way to run part of a row, and the workaround was chosen alone.

## Why it was hard to see

The workaround used the same harness, so it looked equivalent to the standard run.

## Fix

Ask before replacing the runner, and let the lead sanction a partial run by name.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a mutant needs only part of a row, ask the lead first; do not write a private driver, and run every restored green through the standard runner.

## Related

[INC-0546](./INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md)
