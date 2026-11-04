---
id: INC-0566
title: A run wrapper exited zero although one of its steps exited one
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0566 - A run wrapper exited zero although one of its steps exited one

**Cost:** None. The run was judged from its step file and tier counts, and the failure was an environment fault, not a product result.

## Signature - how you recognise it

The wrapper exit status is zero while a recorded step failed.

## What happened

The first full acceptance run stopped at its fourth step because the database cluster the lead owns was down after a host reboot: connection refused, step failed before the database was created. The heavy-run wrapper nevertheless exited 0 although that step exited 1. The lead judged the run from the step file and the tier counts, restarted the cluster by its documented procedure, and re-ran. A typo in the retry first pointed at a directory that did not exist; it failed at the redirect and ran nothing.

## Root cause

The wrapper reports that it ran the child, not that every step passed.

## Why it was hard to see

A zero exit status reads as success.

## Fix

Judge a run from its step file and tier counts, never from the wrapper exit.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never judge a multi-step run by the wrapper exit status; read the step file and the per-tier counts.

## Related

[INC-0490](./INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md)
