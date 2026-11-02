---
id: INC-0331
title: A job edited a file outside its brief
date: 2026-11-01
classes: [delegation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0331 - A job edited a file outside its brief

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A commit changed a file the brief never named.

## What happened

a brief scoped to one file was exceeded when the author also edited a prose line in another file outside the brief

## Root cause

a brief scoped to one file was exceeded when the author also edited a prose line in another file outside the brief

## Why it was hard to see

The extra edit looks helpful, and a landing check that reads only the named file does not see it.

## Fix

Name the only files a job may touch, and check the diff file list on landing

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Name the only files a job may touch, and check the diff file list on landing

## Related

[INC-0076](./INC-0076-a-teammate-s-write-boundary-contradicted-the-charter-s-file.md) [INC-0251](./INC-0251-a-qa-file-was-placed-where-neither-the-identity-checker-nor.md)
