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

A spec required records emitted early in a run to carry an identifier that was not created until later in the run.

## What happened

a spec switched on timing collection at the point where the test database was allocated, but also required the earlier test selection and discovery records to carry the inner run identifier, which stayed private to the harness until that point

## Root cause

the authorization point was placed later in the run than the first event that must carry the identity

## Why it was hard to see

Each requirement reads correctly alone; only the order of events in the run shows that the identity is not yet available.

## Fix

Provide an explicit accessor that is called before selection and keyed to the genuine callback object, and refuse forged objects before any side effect

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put the authorization point before the first event that must carry the identity, and test the forged-object negative

## Related

[INC-0243](./INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md) [INC-0352](./INC-0352-a-size-limit-on-each-transported-record-and-a-full-identity.md) [INC-0354](./INC-0354-gating-by-an-environment-variable-leaked-into-nested-runners.md)
