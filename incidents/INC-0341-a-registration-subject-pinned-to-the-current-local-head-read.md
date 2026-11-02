---
id: INC-0341
title: A registration subject pinned to the current local head read as stale under a push freeze
date: 2026-11-01
classes: [identity-and-keying, checkpoint]
severity: medium
status: fixed
---

# INC-0341 - A registration subject pinned to the current local head read as stale under a push freeze

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An owner packet asserted checkout, clone and remote at one hash, and the assertion went stale only because local commits accumulated.

## What happened

an owner packet asserted checkout, clone and remote at one hash; under a push freeze 159 local commits accumulated and the assertion read as stale although nothing was wrong

## Root cause

an owner packet asserted checkout, clone and remote at one hash; under a push freeze 159 local commits accumulated and the assertion read as stale although nothing was wrong

## Why it was hard to see

Equality of three places holds until the first local commit, and a stale remote-tracking ref can look like proof of the freeze.

## Fix

Pin the subject as remote main equals clone head, corroborate the freeze with a remote query (one tip query does not prove the history), exclude the lead checkout from the equality while the freeze holds and record its distance

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Under a push freeze, pin the subject by role and corroborate the freeze with a remote query (one tip query does not prove the history); a stale remote-tracking ref is not freeze evidence

## Related

[INC-0069](./INC-0069-a-gate-compared-the-candidate-commit-with-itself-because-a-l.md) [INC-0239](./INC-0239-a-hold-outcome-had-no-proof-that-nothing-changed.md)
