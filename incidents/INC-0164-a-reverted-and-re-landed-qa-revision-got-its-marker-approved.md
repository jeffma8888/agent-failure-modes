---
id: INC-0164
title: A reverted and re-landed QA revision got its marker approved at the wrong commit
date: 2026-10-30
classes: [identity-and-keying, checkpoint]
severity: medium
status: fixed
---

# INC-0164 - A reverted and re-landed QA revision got its marker approved at the wrong commit

**Cost:** Minor: a marker was rejected by the checker.

## Signature - how you recognise it

The identity checker compared old active bytes at the approved commit.

## What happened

A QA revision reverted off main and re-landed later needed its marker approved at the re-land commit, because an older copy became active in between and the checker compares the old active bytes at the approved commit.

## Root cause

The approved commit named the original landing, not the re-land.

## Why it was hard to see

The marker looked right until an older copy became active in between.

## Fix

Approve the marker at the re-land commit.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a reverted revision is re-landed after an older copy became active, approve its marker at the re-land commit.

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md)
