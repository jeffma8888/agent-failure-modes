---
id: INC-0433
title: A job text swapped two commit identities, and reading the log caught it
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0433 - A job text swapped two commit identities, and reading the log caught it

**Cost:** No wrong commit was acted on.

## Signature - how you recognise it

Two commits were named the wrong way round in an instruction.

## What happened

a job text swapped the identities of two commits (the two sub-items were named the wrong way round); the lead read the commit log, noted which commit is which sub-item in the ruling, and followed the log

## Root cause

the identities were written from memory of the order instead of from the log

## Why it was hard to see

The two names were adjacent and similar.

## Fix

check any commit named in a job text against the log before acting on it, and state the correction in the ruling

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Read the log for every commit a job text names before acting on it, and record the correction

## Related

[INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md)
