---
id: INC-0010
title: Sleep beats the wake-lock on battery power
date: 2026-07-19
classes: [ipc-and-env]
severity: high
status: fixed
---

# INC-0010 - Sleep beats the wake-lock on battery power

**Cost:** An entire overnight batch of 6 tasks produced 0/6 outputs.

## Signature - how you recognise it

Every task fails with the same 'Connection stalled - no data received for 120 s (network issue or system sleep)' error. Retry-and-backoff works correctly and still cannot win.

## What happened

An overnight background batch on a laptop ran with the OS wake-lock utility holding a 'prevent system sleep' flag. Every task failed with the 120-second stall signature. Retries backed off correctly (10, 20, 40, 60 min) and every retry also failed. Zero outputs.

## Root cause

The 'prevent system sleep' primitive is documented to have no effect on battery power - only on AC. The laptop was on battery. The wake-lock utility ran and reported success but its most important flag was silently ignored, the machine slept through every retry window, and every task hit the network-stall timeout.

## Why it was hard to see

The utility runs, reports success, and looks correct. Nothing warns that its most important flag is being ignored.

## Fix

For any unattended overnight run on a laptop: plug in AC. If AC is unavailable, use the OS's stronger sleep-disable primitive (typically requires elevated privileges) instead of the utility flag. Confirm with the OS's own assertion listing - the aggregate assertion flips from 0 to 1 the moment AC is connected on machines that gate the prevent-sleep primitive on power state.

## Verification

The same task batch on the same machine on AC ran cleanly on the first attempt. Diagnostic: read the battery power source AND read active OS sleep-assertions - not just the flag you set.

## Transferable rule

> A wake-lock utility on a laptop is not enough on battery power - the 'prevent system sleep' primitive is often silently gated on AC. Before an overnight unattended run, plug in AC and confirm the OS assertion is actually held. If the machine sleeps, retry-and-backoff cannot save you.

## Related

[INC-0011](./INC-0011-concurrent-agent-brains-silently-starve-and-kill-each-other.md)
