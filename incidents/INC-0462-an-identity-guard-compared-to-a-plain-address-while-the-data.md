---
id: INC-0462
title: An identity guard compared to a plain address while the database cast rendered the address with a mask, so it could never pass, and a silent catch hid which check failed
date: 2026-11-02
classes: [detector-fail-closed]
severity: low
status: fixed
---

# INC-0462 - An identity guard compared to a plain address while the database cast rendered the address with a mask, so it could never pass, and a silent catch hid which check failed

**Cost:** One stop, no state changed, and two successor scripts.

## Signature - how you recognise it

A walk stopped at its helper with one generic error.

## What happened

a helper and a walker bound the database identity by comparing the text cast of the server address, which renders with a /32 suffix, to the plain address, so the guard could never pass; a catch in the helper reported one generic error and hid which step failed; it stopped a run before any change and was found by a read only query

## Root cause

the guard was written against an assumed rendering of the value

## Why it was hard to see

The generic error hid the failing step, so it looked like load or a product defect.

## Fix

use the host function of the address, count the bind steps, and have the fail closed script print the failing step number, error name and code, filtered to short word characters, with no secrets; keep the originals unchanged and write successors

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Probe a guard against the real value it will see; a guard that can never pass is a defect, and a catch must print which step failed without secrets

## Related

[INC-0318](./INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md) [INC-0120](./INC-0120-a-guard-control-asserted-only-exit-0-so-a-warn-and-pass-guar.md) [INC-0455](./INC-0455-a-provenance-check-that-the-generator-can-never-satisfy-the.md)
