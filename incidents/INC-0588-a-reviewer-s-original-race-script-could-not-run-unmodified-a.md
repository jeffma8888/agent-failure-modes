---
id: INC-0588
title: A reviewer's original race script could not run unmodified against the revision because the step it interrupted no longer exists, and the reviewer reported it as stale test semantics
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0588 - A reviewer's original race script could not run unmodified against the revision because the step it interrupted no longer exists, and the reviewer reported it as stale test semantics

**Cost:** None. The reviewer did not count the stop as a kill.

## Signature - how you recognise it

An old reproducer asserts a step that the revision removed.

## What happened

The reviewer copied the original race script byte for byte and pointed it at the revision. It stopped at its own first assertion, which required a termination after a creation step that the revision no longer has. The reviewer reported that the original script could not exercise the removed hooks, and did not count that stop as a kill of the revision. An adapted script, with the changed step replaced, was run separately and its result reported separately.

## Root cause

The reproducer encodes the shape of the old design.

## Why it was hard to see

A failing old script looks like the revision failing.

## Fix

Report the stop as stale test semantics, run an adapted script, and report both.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When an old reproducer cannot run against a revision, report it as stale test semantics, not a kill, and report the adapted run separately.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md)
