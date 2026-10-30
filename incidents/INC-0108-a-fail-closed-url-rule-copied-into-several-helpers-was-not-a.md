---
id: INC-0108
title: A fail-closed URL rule copied into several helpers was not applied to every copy or every URL part
date: 2026-10-30
classes: [detector-fail-open, identity-and-keying]
severity: medium
status: fixed
---

# INC-0108 - A fail-closed URL rule copied into several helpers was not applied to every copy or every URL part

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

One helper checks the host and another omits the database or port.

## What happened

A fail-closed URL rule was copied into several helpers, and not every copy applied it, nor to every URL part (host, database, port).

## Root cause

Copies drifted and the rule was applied to the part that was easiest to check.

## Why it was hard to see

Each copy looks guarded when read alone.

## Fix

Apply the rule to every copy and to host, database and port.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> One rule, every copy, every URL part.

## Related

[INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md)
