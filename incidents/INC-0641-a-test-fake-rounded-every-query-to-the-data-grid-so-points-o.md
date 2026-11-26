---
id: INC-0641
title: A test fake rounded every query to the data grid, so points on a query edge were never tested until a reviewer wrote a stricter fake
date: 2026-11-16
classes: [false-green]
severity: medium
status: fixed
topic: false-green/test-cannot-see-the-defect
occurrences: 1
---

# INC-0641 - A test fake rounded every query to the data grid, so points on a query edge were never tested until a reviewer wrote a stricter fake

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A test stays green with the behavior removed or broken](../catalog/false-green/test-cannot-see-the-defect.md)

**Cost:** Two inputs that double-counted or shifted a point passed the author's tests; caught in review before the solution was used.

## Signature - how you recognise it

A fake standing in for an interface rounds or normalizes its inputs, and no test sends a value that sits exactly on a boundary.

## What happened

An agent wrote a solution module that searched a set of points through a provided query oracle and tested it against its own fake oracle. The fake rounded every query rectangle to the data grid, so a point lying exactly on the edge of a query square was never exercised. A reviewer running a different model wrote a fake that took raw floating-point coordinates and found two inputs where the solution counted a point twice or attributed it to the wrong cell.

## Root cause

The fake was more lenient than the real interface: its rounding removed exactly the precision and boundary cases the real oracle would present.

## Why it was hard to see

The fake and the solution came from the same author and the same mental model, so they shared the blind spot and every test was green.

## Fix

The fake now passes coordinates through unrounded and runs under both edge-inclusion rules (closed and half-open), and the solution queries on half-step lines so no point can sit on an edge.

## Verification

Checked by the reviewer: the stricter fake exposed the two inputs, and the fixed solution runs under both edge rules. Not checked: other fakes in the same work for the same kind of leniency.

## Transferable rule

> A test fake must be no more lenient than the real interface in precision, rounding and boundary rules; when a different-model reviewer checks code tested only against fakes, have it write an adversarial fake of its own.

## Related

[INC-0078](./INC-0078-a-subprocess-wrapper-decoded-output-strictly-so-malformed-by.md)
