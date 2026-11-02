---
id: INC-0405
title: The demo server served a build made before the merge, so a walk after a source merge would have observed nothing new
date: 2026-11-02
classes: [stale-module]
severity: low
status: fixed
---

# INC-0405 - The demo server served a build made before the merge, so a walk after a source merge would have observed nothing new

**Cost:** A walk would have passed against code that did not contain the merge.

## Signature - how you recognise it

A walk after a merge would have run against a server built before it.

## What happened

the demo server serves a build made before the merge and must not be touched, so a click-walk after a source merge would have observed nothing new

## Root cause

the running server reflects its build time, not the merged source

## Why it was hard to see

The server is up and answers normally, so it looks current.

## Fix

Build the merged SHA fresh and walk it on its own port; leave the demo server alone

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A milestone walk needs a fresh build of the merged SHA on its own port, never the running demo server

## Related

[INC-0382](./INC-0382-a-click-around-walk-that-always-exits-1-from-a-known-gap-can.md) [INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md)
