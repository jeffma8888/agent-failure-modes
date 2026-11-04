---
id: INC-0628
title: A walk's no-write audit counted every non-GET request as a write, and the capture held no request headers or bodies, so override reads stopped the walk
date: 2026-11-04
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0628 - A walk's no-write audit counted every non-GET request as a write, and the capture held no request headers or bodies, so override reads stopped the walk

**Cost:** A walk stopped until installed source, response statuses and an end inventory settled what the requests were.

## Signature - how you recognise it

An audit reports writes for requests that the server treats as reads.

## What happened

A manual walk's no-write audit counted every non-GET request as a write. The admin client sends reads as POST with an override-GET header, which the server turns into a read. The network capture kept no request headers or bodies, so these reads could not be told from writes and stopped the walk. The installed source, the 200 status instead of the 201 a create returns, and an end inventory showing nothing changed settled it.

## Root cause

The audit classified by HTTP method alone, and the capture lacked the data needed to classify by effect.

## Why it was hard to see

A POST looks like a write, and the evidence that it was a read was not in the capture.

## Fix

Capture request headers for non-GET requests, classify override reads at capture time, and keep an end inventory as the final check.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Capture request headers for non-GET requests and classify override reads at capture time; do not classify a request as a write by its method alone.

## Related

[INC-0625](./INC-0625-a-walk-script-ran-a-signed-write-whose-precondition-was-abse.md) [INC-0596](./INC-0596-an-observer-recorded-zero-denied-connects-while-it-also-miss.md)
