---
id: INC-0049
title: A cached credential made a dependency look optional, and the outage was filed under the wrong root cause
date: 2026-10-28
classes: [ipc-and-env, observability]
severity: medium
status: fixed
---

# INC-0049 - A cached credential made a dependency look optional, and the outage was filed under the wrong root cause

**Cost:** A wrong root cause stood in the record for about a day. About nine hours after a recovery attributed to 'the session is not required', the cached upstream session expired and every stage of an autonomous loop failed again, burning failed attempts until it was stopped.

## Signature - how you recognise it

After an outage a component works although its documented credential is known to be expired, and the conclusion drawn is that the credential is not needed.

## What happened

After a reboot, a loop's credential exporter worked even though the single sign-on cookie file it normally reads had been expired for days, so the earlier outage was recorded as 'the session is not required'. The exporter was in fact riding a cached upstream session. When that cache expired the same failure returned, and the exporter's own error named the missing cookie.

## Root cause

One success was read as proof of independence. A cache can keep a dependency satisfied for a while after its source of truth has lapsed, so the first observation after the lapse is the least informative one.

## Why it was hard to see

The recovery was real and the system was healthy for hours, which made the wrong explanation look confirmed. The cache's lifetime was invisible, and the real failure arrived long after anyone was looking.

## Fix

Global stop with the reason written into the stop file; relaunch only after a verified re-authentication; correct the record.

## Verification

The recurrence and the exporter's own error message pointed at the credential chain; relaunch followed a re-auth that was checked first.

## Transferable rule

> A dependency that 'works without' its credential may be riding a cache. Prove independence by checking the whole credential chain's expiry, not by one success, and do not file a root cause until the cache lifetime is accounted for.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the loop engine whose credential exporter and stage failures this describes.

## Related

[INC-0009](./INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) [INC-0036](./INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md)
