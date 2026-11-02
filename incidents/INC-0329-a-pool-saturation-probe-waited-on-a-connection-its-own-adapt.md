---
id: INC-0329
title: A pool saturation probe waited on a connection its own adapter retained
date: 2026-11-01
classes: [false-green, concurrency]
severity: medium
status: fixed
---

# INC-0329 - A pool saturation probe waited on a connection its own adapter retained

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A probe timed out at full pool size and the timeout was read as exhaustion.

## What happened

a saturation probe tried to acquire the full pool maximum although the adapter under test keeps one client checked out, so the probe waited on itself and its timeout was misread as exhaustion of the cluster

## Root cause

a saturation probe tried to acquire the full pool maximum although the adapter under test keeps one client checked out, so the probe waited on itself and its timeout was misread as exhaustion of the cluster

## Why it was hard to see

A timeout looks like proof of a full pool, and the retained client is invisible to the probe.

## Fix

Measure saturation against the maximum minus what the code under test already retains, and never read a timeout as capacity evidence without the acquired and retained counts

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Measure saturation against max minus what the code under test already retains, and never read a timeout as capacity evidence without the acquired and retained counts

## Related

[INC-0313](./INC-0313-tests-in-a-parallel-group-raced-a-test-that-drops-the-shared.md) [INC-0195](./INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md) [INC-0318](./INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md)
