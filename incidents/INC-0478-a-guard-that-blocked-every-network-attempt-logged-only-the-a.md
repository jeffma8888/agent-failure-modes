---
id: INC-0478
title: A guard that blocked every network attempt logged only the API name, so a second run was needed to learn the target
date: 2026-11-02
classes: [observability]
severity: low
status: fixed
---

# INC-0478 - A guard that blocked every network attempt logged only the API name, so a second run was needed to learn the target

**Cost:** Minor: one extra guarded run to classify the stop.

## Signature - how you recognise it

A blocking guard recorded what was called but not where.

## What happened

A guard that blocks every network attempt during a generator run logged only the name of the API that was called. The stop was correct but could not be classified as local inter-process communication or a remote connection. A second guarded run was authorized to log the full argument list and a stack trace per attempt.

## Root cause

The guard recorded the call and dropped its arguments and its origin.

## Why it was hard to see

The block itself looked like the whole answer, so the missing detail only showed when someone had to decide whether the stop was acceptable.

## Fix

Make a blocking guard log the API name, the full arguments and a stack trace on the first run, and classify the target from that log instead of guessing.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A blocking guard logs the API name, the full arguments and a stack trace on the first run, so one run is enough to classify the target.

## Related

[INC-0213](./INC-0213-a-network-denied-dependency-audit-was-neither-a-finding-nor.md) [INC-0192](./INC-0192-a-rehearsal-mixed-automatic-guards-with-procedural-stops.md)
