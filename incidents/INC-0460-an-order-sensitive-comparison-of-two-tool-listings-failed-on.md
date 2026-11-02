---
id: INC-0460
title: An order sensitive comparison of two tool listings failed only when new files were added, though the contract was set membership
date: 2026-11-02
classes: [test-isolation]
severity: low
status: fixed
---

# INC-0460 - An order sensitive comparison of two tool listings failed only when new files were added, though the contract was set membership

**Cost:** A named one line edit and a rerun.

## Signature - how you recognise it

A test failed after unrelated files were added.

## What happened

a test compared two listings from a test tool with an order sensitive equality, while its name and contract said every ordinary file is kept, which is set membership; it passed until new model files changed the listing order and then failed with no product change

## Root cause

the assertion was stricter than the contract it was named for

## Why it was hard to see

It passed for as long as the listing happened to come out in the same order.

## Fix

compare sorted copies when the contract is set membership, change only that line, and name the edit in the commit message and the report

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Compare sorted copies when the contract is set membership, and keep order sensitive equality for contracts that define order

## Related

[INC-0168](./INC-0168-disjoint-project-discovery-did-not-stop-a-suite-from-running.md) [INC-0126](./INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) [INC-0242](./INC-0242-four-of-five-test-authors-stopped-at-the-same-undeclared-sea.md)
