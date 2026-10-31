---
id: INC-0168
title: Disjoint project discovery did not stop a suite from running twice
date: 2026-10-30
classes: [false-green, stage-timeout]
severity: medium
status: fixed
---

# INC-0168 - Disjoint project discovery did not stop a suite from running twice

**Cost:** Minor: about 40 seconds of every fast run.

## Signature - how you recognise it

One stage doubled its cases and its time.

## What happened

A unit case launched the whole integration runner, so every integration case ran twice in the fast tier even though the projects were discovered disjointly.

## Root cause

Disjoint discovery was assumed to imply disjoint execution.

## Why it was hard to see

The nested runner is invisible in the case list; only the stage time shows it.

## Fix

Run the nested runner on one probe file and keep the lifecycle oracle; the case dropped from 20.7 s to 2.5 s and the fast tier from 208 s to 166 s.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that launches a runner must run it on a probe file, not the whole suite.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
