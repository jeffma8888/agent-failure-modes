---
id: INC-0550
title: Integration files that need a live server failed with connection refused under a runner that starts none, first read as a branch regression
date: 2026-11-02
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0550 - Integration files that need a live server failed with connection refused under a runner that starts none, first read as a branch regression

**Cost:** One merge was held for triage until the failures were reproduced on the main branch.

## Signature - how you recognise it

Tests fail with connection refused on a branch, and the cause is a missing precondition of the runner.

## What happened

Two HTTP integration files failed with connection refused in the merge run of a branch. They need a live server at a configured address, and the explicit-file integration runner starts none. They fail the same way on the main branch, so the cause is a harness precondition, not the branch. The other red, a hero file, passed fully on main and alone on the branch.

## Root cause

Under a runner that starts no server, any file that needs one fails regardless of the code.

## Why it was hard to see

The red appears only in the branch run, so it looks like a regression of the branch.

## Fix

Reproduce each red on the main branch with the same runner before blaming the branch.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before reading a red as a regression, run the same files with the same runner on the main branch; a connection refused under a runner that starts no server is a precondition, not a regression.

## Related

[INC-0549](./INC-0549-a-reviewer-wrote-its-own-browser-only-driver-to-reach-a-muta.md)
