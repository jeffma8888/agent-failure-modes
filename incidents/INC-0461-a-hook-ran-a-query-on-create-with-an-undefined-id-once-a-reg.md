---
id: INC-0461
title: A hook ran a query on create with an undefined id once a registry became non empty: a latent defect exposed by data, not code
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0461 - A hook ran a query on create with an undefined id once a registry became non empty: a latent defect exposed by data, not code

**Cost:** A fix commit and a rerun of the database class.

## Signature - how you recognise it

A seed failed with a database type error after a data change.

## What happened

a before change hook ran a referrer count with an undefined document id on a create; the count became NaN and the database refused it with an invalid text representation error as soon as a registry that had been empty gained entries; the defect was latent from the earlier row and was exposed by the later row, not by any code change

## Root cause

the query path was never exercised while the registry was empty

## Why it was hard to see

Every earlier test passed because the loop over the registry had nothing to run.

## Fix

run the check only on an update of a persisted document with a finite id, red first with a create case and a positive control that an update is still refused, and pin the error name

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Guard a hook query on the operation and a valid id; a check over an empty population proves nothing about the non empty case

## Related

[INC-0321](./INC-0321-a-green-parallel-run-was-cited-although-the-parallel-group-h.md) [INC-0112](./INC-0112-a-control-relied-on-state-the-test-had-changed-earlier-and-s.md) [INC-0082](./INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md)
