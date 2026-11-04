---
id: INC-0626
title: A landing subject was written from the lead's expectation of what a plan revision covered, and the author report said less
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0626 - A landing subject was written from the lead's expectation of what a plan revision covered, and the author report said less

**Cost:** A landed commit subject overstated what it landed; history was not rewritten, so an erratum records it.

## Signature - how you recognise it

A commit subject names a wider range than the artifact it lands.

## What happened

The subject of a landing commit said a plan revision records a range of rulings and assignments wider than the revision covers. The author's own report named a narrower range, one assignment and four rulings. The subject was written from expectation, not from the report. A downstream worktree had already fast-forwarded to it, so the ruling recorded an erratum instead of rewriting history, and the remaining items go to the next revision.

## Root cause

The subject was written from what the lead expected the revision to cover.

## Why it was hard to see

The subject read plausible, and the range it overstated was the range of the work in progress.

## Fix

Write the landing subject from the artifact's own header, and record an erratum where history is shared.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write a landing subject from the artifact's own header or report, not from what you expect it covers.

## Related

[INC-0593](./INC-0593-a-packet-author-who-could-not-read-the-rulings-file-marked-e.md) [INC-0611](./INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md)
