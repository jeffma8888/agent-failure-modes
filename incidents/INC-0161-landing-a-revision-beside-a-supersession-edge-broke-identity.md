---
id: INC-0161
title: Landing a revision beside a supersession edge broke identity on main
date: 2026-10-30
classes: [identity-and-keying, detector-fail-open]
severity: medium
status: fixed
---

# INC-0161 - Landing a revision beside a supersession edge broke identity on main

**Cost:** Minor: main sat red until a sweep caught it.

## Signature - how you recognise it

The landing script passed while the identity checker was red on main.

## What happened

Landing a QA revision beside an existing active-path supersession edge broke the identity checker, which resolved the edge source to the highest revision of any other root instead of the highest earlier one. The landing script did not run the checker, so main stayed red until a sweep caught it.

## Root cause

The checker picked supersession sources among all revisions, and the landing path never ran it.

## Why it was hard to see

The checker was run after markers only, so a plain landing looked safe.

## Fix

Revert the landing, and fix the checker on the engineer branch to resolve sources only among earlier revisions.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the identity checker after every landing, not only after markers; resolve supersession sources only among earlier revisions.

## Related

[INC-0154](./INC-0154-a-marker-for-an-already-activated-revision-used-the-pending.md)
