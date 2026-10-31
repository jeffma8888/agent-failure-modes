---
id: INC-0142
title: A redirect test searching for one allowed substring accepted a bad target beside a benign decoy
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0142 - A redirect test searching for one allowed substring accepted a bad target beside a benign decoy

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A redirect check passes because one acceptable string appears among several candidates.

## What happened

A redirect test that searched for one allowed substring accepted a bad target placed beside a benign decoy, and hop bodies were not inspected.

## Root cause

The test looked for any match instead of validating every candidate.

## Why it was hard to see

The decoy satisfies the check.

## Fix

Enumerate and validate every candidate and inspect every hop body.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Validate all candidates, not the first acceptable one.

## Related

[INC-0118](./INC-0118-a-reason-regex-matched-text-the-test-itself-injected-and-mis.md)
