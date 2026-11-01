---
id: INC-0303
title: A guard added to a test tool broke the check under test
date: 2026-11-01
classes: [test-isolation, false-green]
severity: medium
status: fixed
---

# INC-0303 - A guard added to a test tool broke the check under test

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A page that works by hand rendered empty under the test tool.

## What happened

a request guard added to a browser context set a context wide header, and the login page then rendered an empty body and timed out; the guard, not the product, caused the failure

## Root cause

a request guard added to a browser context set a context wide header, and the login page then rendered an empty body and timed out; the guard, not the product, caused the failure

## Why it was hard to see

The failure looks like a product defect or a flaky page.

## Fix

Remove the context wide header, keep the other guard parts, and locate the cause by bisecting the context options

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Test a guard added to a test tool against a known good page, and bisect the tool's options when a page that works by hand fails

## Related

[INC-0275](./INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md)
