---
id: INC-0594
title: A successor draft named as its old bytes a revision that was never approved, so it cannot land against the bytes on main
date: 2026-11-04
classes: [identity-and-keying]
severity: medium
status: mitigated
---

# INC-0594 - A successor draft named as its old bytes a revision that was never approved, so it cannot land against the bytes on main

**Cost:** The draft cannot land unchanged, and two drafts stay parked.

## Signature - how you recognise it

A successor line names old bytes that differ from the helper actually on main.

## What happened

The successor draft named the fifth revision of a helper as the old bytes, but main still carries the third. The fifth was never approved or activated. An unsigned successor line fails the identity checker, so the draft cannot land unchanged. The fix it depends on is not on main either. Both drafts stay parked, untracked and untouched, and the open harness defect (a database name published in the run registration before creation, with no revocation on a duplicate) is recorded for the plan.

## Root cause

The draft was written against an unmerged chain of revisions and its prerequisites were not checked against main.

## Why it was hard to see

The draft was internally consistent, so the mismatch only shows against main.

## Fix

Check a successor's old bytes against the hash on main before landing, and park the draft when they differ.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before landing a successor, check that its named old bytes equal the bytes on main; if they name an unapproved revision, park it.

## Related

[INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) [INC-0492](./INC-0492-a-successor-test-root-was-named-so-the-identity-checker-coul.md)
