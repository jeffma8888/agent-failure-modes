---
id: INC-0282
title: A test that claims a role must prove the role before relying on it
date: 2026-11-01
classes: [false-green, test-isolation]
severity: medium
status: fixed
topic: false-green/real-page-or-response-wrong-behind-green
occurrences: 1
recurrence_of: INC-0275
---

# INC-0282 - A test that claims a role must prove the role before relying on it

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [Tests pass but the real page, status or session is wrong](../catalog/false-green/real-page-or-response-wrong-behind-green.md)

> **Recurrence of [INC-0275](./INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md).** This record repeats an earlier failure and is kept for history; INC-0275 is the canonical record (2 occurrences in total) and carries the rule to apply.

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A committed test claimed a staff role while running as a guest.

## What happened

the committed integration test staff case ran as a guest, since the CMS honors the session cookie only with an allowed Origin or a same-origin fetch-site header; distinct from L-244, which was about an ad hoc probe

## Root cause

the committed integration test staff case ran as a guest, since the CMS honors the session cookie only with an allowed Origin or a same-origin fetch-site header; distinct from L-244, which was about an ad hoc probe

## Why it was hard to see

The guest and staff responses look alike for the checks that were made.

## Fix

Assert a positive identity marker before every staff check

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove the claimed role with a positive identity marker before any check relies on it

## Related

[INC-0275](./INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md)
