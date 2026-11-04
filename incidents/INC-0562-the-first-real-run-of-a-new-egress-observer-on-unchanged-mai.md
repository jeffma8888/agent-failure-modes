---
id: INC-0562
title: The first real run of a new egress observer on unchanged main caught the dev server phoning home, and the agent stopped instead of widening the allowlist
date: 2026-11-04
classes: [observability]
severity: medium
status: mitigated
---

# INC-0562 - The first real run of a new egress observer on unchanged main caught the dev server phoning home, and the agent stopped instead of widening the allowlist

**Cost:** The seam work paused for a ruling; a product defect row and a refined rule came out of it.

## Signature - how you recognise it

A new network observer denies connects that the unchanged product already makes.

## What happened

The first real-server run of the new outbound-connection observer on the unchanged base recorded, before denial, requests from the serving process to a package registry and to the framework telemetry host, and connects from worker processes to loopback ports outside the allowlist. The agent stopped on the mandatory stop rule and did not widen the allowlist. The lead split it into a product defect row to disable telemetry and the version check for every script that runs the framework, and a rule that allows a connect to the literal loopback address only when its exact port was recorded as a listen earlier in the same interval by a process with a ready record in the same tree. Every other loopback port, the IPv6 loopback and the name localhost stay denied.

## Root cause

The product made outbound calls that nothing in the repository disabled, and the observer saw them for the first time.

## Why it was hard to see

The new instrument fails on the baseline, so it looks like an instrument defect.

## Fix

Stop, record the receipt, and let the lead rule between a product fix and a rule keyed to recorded listeners.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a new observer denies traffic on the unchanged base, stop and report; never widen the allowlist, and key any refinement to recorded listeners.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
