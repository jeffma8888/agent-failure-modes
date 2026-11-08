---
id: INC-0631
title: A landing subject's assignment range was again written from the lead's own brief instead of the author report; the second time
date: 2026-11-07
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0631 - A landing subject's assignment range was again written from the lead's own brief instead of the author report; the second time

**Cost:** A landed commit subject named a wider range than its artifact, and an erratum records it.

## Signature - how you recognise it

A commit subject names a range that the author report lists by individual id as narrower.

## What happened

The subject of a plan revision landing gave an assignment range that came from the lead's brief. The author's report named the assignments by individual id, a shorter list. The ruling range for rulings was right. The erratum records the slip, and history is not rewritten. This is the same slip as the earlier landing-subject entry.

## Root cause

The subject was copied from the brief that asked for the work, not from the report on what was done.

## Why it was hard to see

The earlier rule was known, and the brief's range looked right at a glance.

## Fix

Write the landing subject from the artifact's own header or report, listing ids as the report does, and record an erratum when history is shared.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write a landing subject's ranges from the author report, never from your own brief; copy ids as the report lists them.

## Related

[INC-0626](./INC-0626-a-landing-subject-was-written-from-the-lead-s-expectation-of.md) [INC-0593](./INC-0593-a-packet-author-who-could-not-read-the-rulings-file-marked-e.md)
