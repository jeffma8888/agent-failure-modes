---
id: INC-0408
title: An evidence gap, a temporary config not retained, was closed by a lead re-run that kept it, not by asking the author to reconstruct it
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0408 - An evidence gap, a temporary config not retained, was closed by a lead re-run that kept it, not by asking the author to reconstruct it

**Cost:** The gap was closed with observed content instead of a recollection.

## Signature - how you recognise it

A run's evidence omitted a temporary config that had been deleted.

## What happened

an evidence gap, that a temporary config was not retained, was closed by a lead re-run with the config kept and its content recorded, not by asking the author to reconstruct it

## Root cause

the temporary file was removed after the run and not recorded

## Why it was hard to see

A reconstruction is quick to write and cannot be told from the original.

## Fix

Re-run with the artifact kept and record its content; do not rely on a reconstruction from memory

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Close an evidence gap by a re-run that keeps and records the artifact, not by a reconstruction

## Related

[INC-0389](./INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md) [INC-0396](./INC-0396-a-multi-step-command-reported-success-for-its-later-steps-wh.md)
