---
id: INC-0597
title: A run-before-approve test asked for a runtime route that keeps the harness untouched instead of bypassing identity
date: 2026-11-04
classes: [tooling-paths]
severity: medium
status: mitigated
---

# INC-0597 - A run-before-approve test asked for a runtime route that keeps the harness untouched instead of bypassing identity

**Cost:** None. The route was approved for run-before-approve only, with no credit.

## Signature - how you recognise it

A candidate test must run before approval but the normal row selection would pick the active predecessor.

## What happened

The author asked for a runtime route. Inside one heavy-run invocation: select the row and build its commands on the unswapped tree and save them as JSON with a SHA256; set an exit trap that restores the active predecessor and verifies it; swap in the candidate and verify it; run the saved commands through the unchanged orchestration, with no identity call, marker, manifest or registry edit. Each mutant runs only the changed file, must turn red at the stated line, restore by SHA256 and go green, and each mutant also runs once on the unchanged predecessor to show it stays green.

## Root cause

Running a candidate before approval needs a swap, and the nearest swap would edit identity records.

## Why it was hard to see

Editing identity records works but hides the candidate from the approval check it is waiting on.

## Fix

Ask the lead for a bounded runtime route that saves the selection first, restores by trap, and touches no identity file.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a run-before-approve needs a swap, ask for a runtime route with a trap restore instead of editing identity records, and give it no credit.

## Related

[INC-0540](./INC-0540-a-successor-root-needed-to-change-a-file-owned-by-another-ro.md)
