---
id: INC-0508
title: A build step was given the load threshold meant for timing-sensitive runs and was refused twice while the host was busy
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: mitigated
---

# INC-0508 - A build step was given the load threshold meant for timing-sensitive runs and was refused twice while the host was busy

**Cost:** Two refused launches and a delayed build; no result was lost.

## Signature - how you recognise it

A strict admission threshold designed for timing-sensitive runs is applied to a step whose result does not depend on timing.

## What happened

The lead gave a build step the strict load threshold that exists for timing-sensitive browser runs. The host was busy with unrelated work, and the build was refused twice. A build does not depend on timing and only gets slower under load, so the strict class protected nothing and delayed the work.

## Root cause

The threshold was chosen by the kind of tool being run, not by whether the result depends on timing.

## Why it was hard to see

A refusal looks like a correct safety stop, so a mismatched threshold is read as a busy host and not as a wrong class.

## Fix

Pick each step load threshold by whether its result depends on timing, and give a build the looser class.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Pick each step load threshold by whether its result depends on timing; a build that only gets slower uses the looser class.

## Related

[INC-0500](./INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md) [INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md)
