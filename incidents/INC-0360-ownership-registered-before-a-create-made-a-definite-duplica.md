---
id: INC-0360
title: Ownership registered before a create made a definite duplicate error drop a foreign database
date: 2026-11-01
classes: [test-isolation, identity-and-keying]
severity: medium
status: fixed
---

# INC-0360 - Ownership registered before a create made a definite duplicate error drop a foreign database

**Cost:** Minor: found by static reading before any run was affected.

## Signature - how you recognise it

A harness queued a drop of its test database before creating it, so a create that failed because the name existed would drop a database it never made.

## What happened

a test harness queued the drop of a test database before issuing the create, on purpose, so that an uncertain create outcome would still be cleaned up. A create that failed with a definite already-exists error would then drop a database this run never created. A helper in the test suite recorded ownership the same way. Random name suffixes made a real collision improbable, so this was an ownership-rule defect rather than an observed incident

## Root cause

ownership was claimed before the create outcome was known and was never released when the outcome turned out to be a definite duplicate

## Why it was hard to see

The early registration is correct for the uncertain case, and collisions were improbable, so no run ever exercised the duplicate path.

## Fix

Keep the uncertain-outcome cleanup but never drop on a definite duplicate; first add a test that pre-creates a foreign database under the exact target name, forces allocation onto it and asserts the foreign database survives and the run fails closed, then on the duplicate error remove the queued drop and the registration before rethrowing

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Ownership recorded before a create covers an uncertain outcome only; on a definite already-exists error release the claim before rethrowing, and test with a pre-existing object under the exact name

## Related

[INC-0066](./INC-0066-a-worker-s-end-of-run-cleanup-deleted-a-shared-scratch-direc.md) [INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md) [INC-0254](./INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md)
