---
id: INC-0583
title: A unit row passed only because the caller exported a scratch media directory, and the runner did not own one
date: 2026-11-04
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0583 - A unit row passed only because the caller exported a scratch media directory, and the runner did not own one

**Cost:** No loss. A new harness row was opened before the dependence could hide a failure.

## Signature - how you recognise it

A row passes only when the caller environment supplies a path the runner should own.

## What happened

The unit tier of the row runner gave the unit runner no run-scoped media directory, so a unit row that touches media passed only when the caller exported a scratch directory. Two reviewers noticed. The lead opened a harness row: the runner creates a fresh directory under its own run directory for the unit tier, passes it, removes it by exact path at exit, ignores any caller value for that tier so no caller can point a row at the demo media directory, and keeps every other argument unchanged. It is built test-first, with one real row run with nothing exported, then a unit comparison equal to the frozen baseline.

## Root cause

The runner relied on the caller environment for a path.

## Why it was hard to see

The row is green on the author machine because of the exported variable.

## Fix

Have the runner own a run-scoped directory, remove it by exact path, and ignore the caller value.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A runner must own the scratch directories its tests write to and ignore caller values for that tier; a row that passes only with an exported path is not green.

## Related

[INC-0550](./INC-0550-integration-files-that-need-a-live-server-failed-with-connec.md)
