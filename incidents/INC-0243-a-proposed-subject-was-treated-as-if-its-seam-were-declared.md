---
id: INC-0243
title: A proposed subject was treated as if its seam were declared
date: 2026-11-01
classes: [spec-and-scope, test-isolation]
severity: medium
status: fixed
---

# INC-0243 - A proposed subject was treated as if its seam were declared

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The missing binding was not declared anywhere.

## What happened

Authorizing a synthetic collection or owning a generated field was read as declaring an importable, callable boundary.

## Root cause

Authorizing a synthetic collection or owning a generated field was read as declaring an importable, callable boundary.

## Why it was hard to see

Owning the thing looks like owning its import path.

## Fix

Declare the import seam; a missing-module error is useful test-first coverage only when the missing binding is itself declared

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Declare the import seam; ownership or authorization of a subject does not declare a callable boundary

## Related

[INC-0242](./INC-0242-four-of-five-test-authors-stopped-at-the-same-undeclared-sea.md) [INC-0352](./INC-0352-a-size-limit-on-each-transported-record-and-a-full-identity.md) [INC-0353](./INC-0353-an-authorization-point-was-placed-after-the-first-event-that.md)
