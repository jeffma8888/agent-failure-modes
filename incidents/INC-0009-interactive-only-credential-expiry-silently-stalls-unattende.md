---
id: INC-0009
title: Interactive-only credential expiry silently stalls unattended loops
date: 2026-07-31
classes: [ipc-and-env, detector-fail-open]
severity: high
status: mitigated
---

# INC-0009 - Interactive-only credential expiry silently stalls unattended loops

**Cost:** About 5 hours of silent stall across two iterations, then a couple more of the same before an alarm was built - all harmless (retries kept failing safely) but zero throughput.

## Signature - how you recognise it

Step logs say 'credential refresh failed' or 'authentication timed out'. Distinct from throttle ('service is busy') and from the hard timeout ('timed out after 600s'). The lead thread also stalls, so hours can pass silently.

## What happened

A long-running unattended loop broke on the model provider's credential expiring, not on rate limiting. The credential was held in a cookie file with a ~12-hour TTL and could only be refreshed via an interactive prompt requiring a hardware key. When the cookie expired, every model call failed and the loop retried harmlessly forever until a human re-authenticated.

## Root cause

The credential is refreshable, but only interactively - no unattended loop can refresh it. The retry loop was doing the right thing (keeping work safe), but the work was stalled indefinitely.

## Why it was hard to see

The signature is easy to confuse with throttling. And there is no single event to alarm on: the useful signal is 'the long-lived credential is about to expire', not 'credential just expired'.

## Fix

A simple watchdog script that (a) proactively warns when the long-lived credential drops below N minutes remaining, and (b) reactively greps recent step logs for the 'credential refresh failed' string as ground truth. Watch the LONG-LIVED credential (12h TTL), not the short-lived derivative one (auto-refreshing), or the alarm fires constantly.

## Verification

A subsequent 6-hour stall auto-recovered the instant the human re-authenticated. Turnaround from silent-multi-hour-stall to under-5-minute re-auth.

## Transferable rule

> Any long unattended loop depending on a human-refreshable credential will eventually stall on expiry, not throttle. Watch the LONG-LIVED credential (12h class), not the short-lived derivative one, and pair a 'time-remaining' alarm with a log-string alarm - each catches what the other misses.

## Related

[INC-0008](./INC-0008-stale-ipc-endpoint-after-the-host-application-restarts.md) [INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md)
