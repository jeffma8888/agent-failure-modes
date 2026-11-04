---
id: INC-0601
title: A nested driver deleted NODE_OPTIONS, so a preload capture never reached the nested harness and a zero counted from copied receipts was not zero
date: 2026-11-04
classes: [false-green]
severity: high
status: mitigated
---

# INC-0601 - A nested driver deleted NODE_OPTIONS, so a preload capture never reached the nested harness and a zero counted from copied receipts was not zero

**Cost:** A measurement reported zero denials while the log held 22 denied decisions, so the zero could not be credited and the seam could not merge.

## Signature - how you recognise it

A results file reports an empty denial list while the log lists denials.

## What happened

A test driver deleted NODE_OPTIONS before it spawned the nested harness, so an external capture preload never reached the nested processes. The results file counted denials only from copied files and showed none. The log-derived inventory held 22 denied decisions: one off-host fetch and 21 loopback connects by loader pool workers of the dev server. The ruling said that is not a zero-denial result, and the next measurement must use a capture route that reaches nested harnesses and count denials from the log as well as from copies.

## Root cause

The capture was injected through an environment variable that a nested driver clears, and the count was taken from copies of the observed files.

## Why it was hard to see

The results file was well formed and its zero looked like a clean run; only the log showed the denials.

## Fix

Use a capture route that reaches nested harnesses, and count denials from the log as well as from copies.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A capture injected through an inherited environment variable is blind to any child that clears it; count from the log, and treat a zero from copies as unproven until a positive control shows the capture reaches the innermost process.

## Related

[INC-0596](./INC-0596-an-observer-recorded-zero-denied-connects-while-it-also-miss.md) [INC-0575](./INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md)
