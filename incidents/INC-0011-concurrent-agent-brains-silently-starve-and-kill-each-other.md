---
id: INC-0011
title: Concurrent agent brains silently starve and kill each other
date: 2026-08-10
classes: [concurrency, ipc-and-env]
severity: critical
status: mitigated
---

# INC-0011 - Concurrent agent brains silently starve and kill each other

**Cost:** An 8-task research batch failed 8/8 across 5 retries each, zero outputs, because 8 subagents were launched into a saturated model-provider account already running an always-on dispatcher.

## Signature - how you recognise it

Multiple tasks fail with 'Connection stalled - no data received for 120 s' plus occasional 'service is busy'. AC power is confirmed. A long-running dispatcher process is alive.

## What happened

A background 8-task batch was launched into an account already running an always-on dispatcher (5+ days uptime) that was itself firing agent invocations every few minutes. The batch failed 8/8, 5 attempts each, zero output files. The signature matched no-sleep-but-quota-starvation. The same failure had been recorded in the project's own changelog 5 days earlier and unread.

## Root cause

One provider account, N concurrent brains fighting for it. Each brain retries on failure, which manufactures more concurrent load, which starves the others further. There is no graceful degradation - the losing brain simply cannot make progress.

## Why it was hard to see

The individual failure signature (connection stall, service busy) is identical to a sleep issue or a genuine transient network problem. It only makes sense once you count the number of concurrent brains against one account and see the ratio is wrong.

## Fix

A mandatory pre-flight count before any batch launch: enumerate live agent-run processes; if a long-running dispatcher is alive, either wait for a quiescent window or do the work inline. Consolidate multiple loops under a single scheduler running concurrency 1 (round-robin) so they never split the quota.

## Verification

The next batch launched after the always-on dispatcher was quiesced ran clean 6/6.

## Transferable rule

> Multiple agents share a model-provider quota, and the losing brain cannot degrade gracefully - it dies silently. Before ANY batch launch: count the live brains against one account, and if a dispatcher is already alive, either wait for a quiescent window or run inline. Signature: 'connection stalled 120s' plus 'service busy' on multiple tasks with confirmed AC power.

## Related

[INC-0010](./INC-0010-sleep-beats-the-wake-lock-on-battery-power.md)
