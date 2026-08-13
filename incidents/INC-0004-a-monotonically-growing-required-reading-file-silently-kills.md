---
id: INC-0004
title: A monotonically growing required-reading file silently kills the loop
date: 2026-08-04
classes: [stage-timeout, steering-channel, spec-and-scope]
severity: high
status: fixed
---

# INC-0004 - A monotonically growing required-reading file silently kills the loop

**Cost:** A product stopped committing for 5 hours - four consecutive attempts, all 48-byte timeout logs.

## Signature - how you recognise it

Same log signature as INC-0002, but the guilty artifact is a required-reading file (a roadmap, a design doc, a large context file) that grew organically over many iterations.

## What happened

A product's planning role must read AND REWRITE a roadmap file every iteration. Over 90-plus iterations it grew to 200KB. The read-plus-rewrite time crossed 600 seconds and every attempt died before producing output. The log signature was identical to INC-0002's.

## Root cause

Any required-reading artifact injected into every step's prompt is a resource that must be bounded by CHARACTERS, not by item count. This file bounded nothing: each iteration appended a new row and never compacted. The steering channel meant to keep the loop informed silently became the thing that killed it.

## Why it was hard to see

The file is doing exactly what it was designed to do - accumulating decisions - and shrinking it feels wrong. The 48-byte log looks identical to a throttle stall. Distinguish: throttle logs say 'service is busy'; stale-endpoint logs contain CLI help text; hard-cap logs are exactly the timeout string and nothing else.

## Fix

Compact the file to an index and move verbatim history to a sibling archive. Add a size budget and enforce it in the loop's own tests, so a regressing growth cannot recur silently. If you must keep the full record, split it: a small always-read index plus a large read-on-demand archive.

## Verification

The file went 200KB to 36KB (83% smaller, all 98 rows preserved). The next planning attempt produced output within 3 minutes.

## Transferable rule

> Any file injected into EVERY iteration's prompt is a resource. Bound it by CHARACTERS, not item count, and cap it at write time. A monotonically growing steering artifact will silently kill the loop on the same timeout cap; when it does, the log looks exactly like a rate-limit stall - distinguish by content, not size.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0020](./INC-0020-a-steering-channel-counts-only-when-the-consumer-s-own-parse.md)
