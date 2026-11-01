---
id: INC-0306
title: A conditional diagnosis was closed from the actor's account and the code path
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0306 - A conditional diagnosis was closed from the actor's account and the code path

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A diagnosis named only conditional hazards, yet the incident needed a cause.

## What happened

the code analysis showed the cleanup tool would skip a live owner and listed two hazards that were conditional and not established; the removing actor's own account of names, timing and reason settled the cause as a manual removal

## Root cause

the code analysis showed the cleanup tool would skip a live owner and listed two hazards that were conditional and not established; the removing actor's own account of names, timing and reason settled the cause as a manual removal

## Why it was hard to see

A conditional hazard looks like a defect to fix, and opening a fix row for it widens scope without evidence.

## Fix

Close on the confirmed cause from the actor's account plus the code path, record the conditional hazard with its conditions as a follow-up, and leave the unchanged mechanism running

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not open a fix row for a hazard that is only conditional; close on the confirmed cause and track the hazard as a follow-up

## Related

[INC-0305](./INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md)
