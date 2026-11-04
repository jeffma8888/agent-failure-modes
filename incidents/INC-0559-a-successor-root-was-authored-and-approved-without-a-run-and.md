---
id: INC-0559
title: A successor root was authored and approved without a run, and its first baseline failed because the installed config had one more internal collection than its exact list
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0559 - A successor root was authored and approved without a run, and its first baseline failed because the installed config had one more internal collection than its exact list

**Cost:** The activation baseline failed in setup before any case ran; the root was left immutable and a new successor was needed.

## Signature - how you recognise it

An exact list of framework internals in a root is stale against the installed configuration.

## What happened

A successor root passed static review and approval but was never run. Its first green baseline failed in the setup step: the exact collection list check excluded three internal collections, and the installed framework configuration also carries a fourth, a key-value one. No browser case ran and no mutant was applied. The lead ruled that this is a defect in the root, not a product finding, that the bytes stay immutable, and that there is no in-place edit and no retry.

## Root cause

The exact list was written from memory of the framework, not read from the installed configuration, and no run happened before approval.

## Why it was hard to see

Static review cannot see what the installed version adds.

## Fix

Derive or verify the list against the installed configuration, and run the root once before approval or activation.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A root that pins a list of framework internals must be checked against the installed configuration and run once before approval; a setup failure is a root defect, fixed by a new successor, never by an in-place edit.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md)
