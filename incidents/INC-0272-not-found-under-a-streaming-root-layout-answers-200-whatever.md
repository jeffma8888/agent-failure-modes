---
id: INC-0272
title: Not-found under a streaming root layout answers 200 whatever the call site
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0272 - Not-found under a streaming root layout answers 200 whatever the call site

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Every call site for a not-found error still returned 200.

## What happened

notFound under a framework root layout answered 200 even when synchronous, from a layout, or for a crawler user agent, because the error lands in a streamed boundary below the root provider; the status was fixed in a proxy

## Root cause

notFound under a framework root layout answered 200 even when synchronous, from a layout, or for a crawler user agent, because the error lands in a streamed boundary below the root provider; the status was fixed in a proxy

## Why it was hard to see

Each variant looked like a fix and each kept the status.

## Fix

Decide the status in a proxy before the shell streams

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a root layout streams its shell, set the status before it, not from the rendered view

## Related

[INC-0265](./INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md) [INC-0273](./INC-0273-a-status-check-must-take-every-client-reading.md)
