---
id: INC-0313
title: Tests in a parallel group raced a test that drops the shared inventory
date: 2026-11-01
classes: [concurrency, test-isolation]
severity: medium
status: fixed
---

# INC-0313 - Tests in a parallel group raced a test that drops the shared inventory

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A single-file run passed or failed alone while the full parallel run could race.

## What happened

tests placed in a parallel group created shared resources while another test snapshotted and force-dropped the shared inventory, a race that a focused single-file run cannot show

## Root cause

tests placed in a parallel group created shared resources while another test snapshotted and force-dropped the shared inventory, a race that a focused single-file run cannot show

## Why it was hard to see

Each file is correct alone, and the race appears only when two files run at the same time.

## Fix

Put the test that creates shared resources in a serial group with no concurrent inventory reader, and do not treat a focused run as evidence of isolation

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that creates shared resources goes in a serial group with no concurrent inventory reader; a focused single-file run is not evidence of isolation

## Related

[INC-0132](./INC-0132-vitest-4-ran-projects-in-parallel-and-file-serialization-ins.md) [INC-0305](./INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md)
