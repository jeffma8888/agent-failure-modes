---
id: INC-0557
title: The lock holder waited for the load to fall while still holding the host lock, and eleven agents fed that one lock, so waits of 20 minutes became normal
date: 2026-11-02
classes: [concurrency, delegation]
severity: low
status: open
---

# INC-0557 - The lock holder waited for the load to fall while still holding the host lock, and eleven agents fed that one lock, so waits of 20 minutes became normal

**Cost:** Agents sat in queues for 20 to 25 minutes at a time; their running cost continued while their runtime work did not advance.

## Signature - how you recognise it

Recorded lock waits grow with the number of agents, while the lock holder itself is waiting on the load gate.

## What happened

The lock helper took the lock first and then waited, up to 15 minutes, for the load average to fall under its limit, still holding the lock. Under co-tenant load every waiter therefore queued behind a holder that was itself waiting. Eleven agents each had runtime steps (green runs, mutation cycles, restores, full suites), all through the one lock, and receipts showed lock waits of 1180 and 1490 seconds. The lead kept agents productive by giving the surplus static work (reviews, authoring tests, design proposals, audits), which needed no lock.

## Root cause

The order lock-then-load made the load wait exclusive, and runtime parallelism was sized to the number of agents rather than to one lock.

## Why it was hard to see

Each agent's wait looks like a fair share of a scarce resource; the convoy is visible only when the waits are compared across receipts.

## Fix

Wait for load before taking the lock, or release it while waiting; size the number of agents with runtime steps to what the lock can serve, and give the rest static work.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never hold a shared lock while waiting on a condition that other waiters also need, and match the number of agents doing runtime work to the capacity of the serialized resource, not to the size of the team.

## Related

[INC-0554](./INC-0554-a-host-wide-load-gate-held-a-one-shot-time-windowed-check-un.md) [INC-0556](./INC-0556-a-polling-host-lock-does-not-serve-waiters-in-order-so-a-tes.md)
