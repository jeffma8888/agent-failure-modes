---
id: INC-0318
title: A path guard probed only with nonexistent paths could never fail
date: 2026-11-01
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0318 - A path guard probed only with nonexistent paths could never fail

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Every negative target returned allowed because the probed paths did not exist.

## What happened

the sandbox check answers allowed for any nonexistent path even when unconfined, so a guard probed only with nonexistent negative targets passed every row without testing anything

## Root cause

the sandbox check answers allowed for any nonexistent path even when unconfined, so a guard probed only with nonexistent negative targets passed every row without testing anything

## Why it was hard to see

The check answers consistently, so a vacuous row looks the same as a real one.

## Fix

Make negative targets exist, pair every guard with a positive control that must return the other value, and run one selftest on the real unpatched checker

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Negative targets must exist; pair every guard with a positive control that must return the other value, and run one selftest on the real unpatched checker

## Related

[INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) [INC-0314](./INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) [INC-0329](./INC-0329-a-pool-saturation-probe-waited-on-a-connection-its-own-adapt.md) [INC-0363](./INC-0363-a-module-presence-guard-went-through-the-test-s-own-file-sys.md) [INC-0462](./INC-0462-an-identity-guard-compared-to-a-plain-address-while-the-data.md)
