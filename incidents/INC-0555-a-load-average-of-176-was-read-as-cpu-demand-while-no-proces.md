---
id: INC-0555
title: A load average of 176 was read as CPU demand while no process used more than one core, because the number counts waiting work and lags
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0555 - A load average of 176 was read as CPU demand while no process used more than one core, because the number counts waiting work and lags

**Cost:** No direct loss; a risk of blaming the team's own jobs, or of stopping the wrong process.

## Signature - how you recognise it

A one-minute load average far above the core count while the per-process CPU list shows no process above one core.

## What happened

At one point the one-minute load average was 176 on a 12-core host. A per-process CPU listing at the same moment showed the file-event service at 83 percent of a core, a device-management agent at 22 percent and nothing else above 7 percent. A few minutes earlier the same listing had shown a dozen co-tenant test workers at about 50 percent each, which had already exited. The load average counts runnable threads and threads blocked in uninterruptible waits, which includes disk-bound work, and it is a moving average, so it kept reporting the burst and the input-output pressure after the CPU was free.

## Root cause

The gate, and the people reading it, treated the load average as a measure of busy CPU.

## Why it was hard to see

The load average is the number every tool prints first, and on a quiet machine it is close enough to CPU demand.

## Fix

Read the per-process CPU list with owners alongside the load average before deciding anything, and record both in the receipt.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before acting on a high load average, list the top processes by CPU with their owners; a load far above the core count with no process above one core is waiting work or lag, not CPU demand.

## Related

[INC-0554](./INC-0554-a-host-wide-load-gate-held-a-one-shot-time-windowed-check-un.md) [INC-0544](./INC-0544-a-walk-load-limit-was-unreachable-because-the-host-floor-wit.md)
