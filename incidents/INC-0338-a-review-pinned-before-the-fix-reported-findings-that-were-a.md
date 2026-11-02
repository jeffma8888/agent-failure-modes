---
id: INC-0338
title: A review pinned before the fix reported findings that were already closed
date: 2026-11-01
classes: [spec-and-scope, checkpoint]
severity: medium
status: fixed
---

# INC-0338 - A review pinned before the fix reported findings that were already closed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A review of an older checkpoint listed findings as open that had since been fixed and closed.

## What happened

a review was pinned to a checkpoint that predated the fix and marked three sites open, although the author had already fixed them and a second reviewer had closed them at a later revision, so routing the review as written would have reopened closed work

## Root cause

a review was pinned to a checkpoint that predated the fix and marked three sites open, although the author had already fixed them and a second reviewer had closed them at a later revision, so routing the review as written would have reopened closed work

## Why it was hard to see

The review is correct for the revision it read, and nothing in it says a later revision superseded it.

## Fix

Land the review with a supersession note naming the commit and the review that supersede each stale finding, and route only the findings that are still live

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a review's pin is older than the latest fix, land it with a note naming the commit and review that supersede each stale finding

## Related

[INC-0284](./INC-0284-a-gate-result-counts-only-at-a-revision-the-gate-can-fetch-a.md) [INC-0302](./INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md)
