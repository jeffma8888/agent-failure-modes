---
id: INC-0084
title: Test-summary assertions broke on ANSI color codes, and compile caches were mistaken for resource leaks
date: 2026-10-30
classes: [test-isolation, false-green]
severity: low
status: fixed
topic: test-isolation/assertion-wider-than-contract
occurrences: 1
---

# INC-0084 - Test-summary assertions broke on ANSI color codes, and compile caches were mistaken for resource leaks

**Catalog:** [root](../catalog/README.md) / [test-isolation](../catalog/test-isolation/README.md) / [Assertion measures more than its contract: caches, order, whole totals](../catalog/test-isolation/assertion-wider-than-contract.md)

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A test asserts on tool summary text that contains color escape codes, or a leak check counts cache files.

## What happened

An engineer asserted on test-summary text without stripping ANSI codes, and treated compile cache directories as leaked resources.

## Root cause

The assertion read raw terminal output and the leak check did not separate owned resources from tool caches.

## Why it was hard to see

The text looks right on screen, and cache files appear next to real temporary files.

## Fix

Strip ANSI codes before asserting summary text, and exclude compile caches from leak checks.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Normalize terminal output before matching it, and define what counts as an owned resource before counting leaks.

## Related

[INC-0464](./INC-0464-color-escape-codes-in-a-report-broke-an-extraction-assertion.md)
