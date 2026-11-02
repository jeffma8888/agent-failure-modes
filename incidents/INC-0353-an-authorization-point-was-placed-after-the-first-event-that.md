---
id: INC-0353
title: An authorization point was placed after the first event that needs the identity
date: 2026-11-01
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0353 - An authorization point was placed after the first event that needs the identity

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A spec required records that happen before the authorization point to carry an identity that did not exist until after it.

## What happened

the spec authorized timing at database allocation, but required selection and discovery records, which happen earlier, to carry the inner run id, which was private to the harness until then

## Root cause

the authorization point was placed later in the run than the first event that must carry the identity

## Why it was hard to see

Each requirement reads correctly alone; only the order of events in the run shows that the identity is not yet available.

## Fix

An explicit accessor called before selection, keyed to the authentic callback object, with refusal of forged objects before side effects

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put the authorization point before the first event that must carry the identity, and test the forged-object negative

## Related

[INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md) [INC-0352](./INC-0352-a-transport-size-limit-and-a-full-identity-requirement-were.md) [INC-0354](./INC-0354-gating-by-an-environment-variable-leaked-into-nested-runners.md)
