---
id: INC-0291
title: A known unrelated load timeout blocked a row until one combined run accepted both
date: 2026-11-01
classes: [false-green, stage-timeout]
severity: medium
status: fixed
---

# INC-0291 - A known unrelated load timeout blocked a row until one combined run accepted both

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A branch gate failed only on a known unrelated timeout under heavy load.

## What happened

the single failing case timed out at 5321 ms against a 5000 ms default at high host load, and its fix was in flight on another row; rerunning each branch separately would repeat the load problem

## Root cause

the single failing case timed out at 5321 ms against a 5000 ms default at high host load, and its fix was in flight on another row; rerunning each branch separately would repeat the load problem

## Why it was hard to see

The failure is real in the log but unrelated to the change under test.

## Fix

Merge both rows locally, run one gate on the combined result, name the unrelated failure, and give it its own robustness row

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When the only failure is a known unrelated load timeout with a fix in flight, one passing run on the combined merge accepts both rows

## Related

[INC-0218](./INC-0218-two-loaded-host-reds-shared-one-cause-and-were-at-risk-of-a.md) [INC-0271](./INC-0271-a-load-induced-harness-red-is-not-headroom.md)
