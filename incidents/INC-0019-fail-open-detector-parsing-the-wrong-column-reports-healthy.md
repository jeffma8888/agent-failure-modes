---
id: INC-0019
title: Fail-open detector: parsing the wrong column reports healthy
date: 2026-08-05
classes: [detector-fail-open, observability]
severity: high
status: fixed
---

# INC-0019 - Fail-open detector: parsing the wrong column reports healthy

**Cost:** Nearly logged 'auth OK' during a period when the long-lived credential had actually expired ~180 minutes earlier.

## Signature - how you recognise it

A cookie- or config-file parser produces empty output that reads as 'nothing to report' when in fact every row is unparseable because the code is reading the wrong field.

## What happened

A watchdog parsed a cookie file where each line has seven tab-separated fields. The code read the expiry from field 7 - which is the VALUE, not the expiry. Every numeric parse failed silently and the summary printed nothing. That silence was almost logged as 'auth is fine'.

## Root cause

Two errors on the same file. First, expiry is field 5 of 7 in the Netscape cookie format, not field 7. Second, some lines are prefixed with `#HttpOnly_` which must be stripped BEFORE the leading-`#` comment skip, or the real rows are silently dropped.

## Why it was hard to see

Empty output is the SAME visual outcome as a clean run. Detectors that fail silently by reporting nothing look identical to detectors that pass.

## Fix

Sanity-check every parser by asserting that its long-lived rows come back with PLAUSIBLE values - remaining-time of ~150 days for a long-lived config token, ~270 days for another, and so on. If every row is unparseable, you have the wrong column. Never print raw cookie values, only names plus remaining-minutes.

## Verification

With field 5 read correctly, the parser surfaced two long-expired credentials that had been invisible for days. A regression test asserts that a known-good file returns non-trivial data.

## Transferable rule

> A parser that fails silently by returning nothing is indistinguishable from a healthy sample. Sanity-check every parser by asserting that its rows come back with PLAUSIBLE values; if every row is unparseable, you have the wrong column, not a healthy system. Never make an alarm's positive answer look like its negative answer.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md)
