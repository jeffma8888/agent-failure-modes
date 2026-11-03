---
id: INC-0554
title: A host-wide load gate held a one-shot, time-windowed check until its window passed, because processes outside the team drove the load
date: 2026-11-02
classes: [concurrency, observability]
severity: medium
status: open
---

# INC-0554 - A host-wide load gate held a one-shot, time-windowed check until its window passed, because processes outside the team drove the load

**Cost:** One evidence row was lost: the natural expiry of a lockout was never observed, and the walk closed with that row partial. Runtime jobs waited 20 to 25 minutes for the lock.

## Signature - how you recognise it

Every runtime job, from a full suite to one read-only browser check, waits for the same host one-minute load average to fall under a fixed limit, while processes the team does not own set that load.

## What happened

An eleven-agent team serialized its runtime jobs on one host lock and admitted each job only when the one-minute load average was under a fixed limit (16 for suites, 20 for browser walk phases). During the evening the load rose from about 14 to between 100 and 260. The team itself ran one serialized job at a time; the rest came from co-tenants on the same machine: a separate autonomous test loop that started bursts of about a dozen parallel test workers, another desktop application's backend holding about three cores for ten hours, and the desktop file-event service at about 83 percent of a core for six days, fed by many worktrees and dependency trees inside watched folders. A walker had locked out a disposable account and needed one later browser read after the natural expiry time. When that time came, its gate did not admit the read (load 140.68), and the walker recorded expiry as NOT-RUN instead of inferring recovery. Other jobs recorded lock waits of 1180 and 1490 seconds.

## Root cause

Admission keyed on one host-wide number that the team neither owned nor could lower, with the same kind of limit for heavy and light jobs, and no reserved slot for an observation with a deadline.

## Why it was hard to see

Each job reported only that the load was too high and it was waiting, which reads as patience, not failure. Nobody looked up what was driving the load until late, and the lost observation surfaced only in the final report.

## Fix

Attribute the load by process and owner before reacting; give the owners of co-tenant load a concrete ask (cap parallel workers, keep work trees out of file indexing); never stop a process the team does not own. Gate by job weight, so one read-only check gets a lighter gate or a named exception. Take a time-windowed observation inside a session that is already admitted, or reserve a slot for it before the window opens.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not let one host-wide load threshold admit every job alike: size the gate to the job, attribute the load to its owners first, and reserve capacity for any observation that has a deadline.

## Related

[INC-0544](./INC-0544-a-walk-load-limit-was-unreachable-because-the-host-floor-wit.md) [INC-0551](./INC-0551-a-test-that-passed-alone-at-about-63-percent-of-its-timeout.md)
