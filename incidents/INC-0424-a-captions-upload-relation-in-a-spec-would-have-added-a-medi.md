---
id: INC-0424
title: A captions upload relation in a spec would have added a media referrer to a collection defined as image-only
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0424 - A captions upload relation in a spec would have added a media referrer to a collection defined as image-only

**Cost:** No code was written; the spec was corrected at review.

## Signature - how you recognise it

A relation targeted a collection that does not accept its content.

## What happened

a spec proposed a captions upload relation to the media collection, but media is image-only with fixed upload limits, so the relation would have added a media referrer to the lists of an earlier row; the lead deferred the file subfield to the later caption and video upload work and recorded the gap

## Root cause

the relation was specified from the field's purpose without checking the target collection's scope

## Why it was hard to see

The relation looked natural for captions and was wrong for an image-only collection.

## Fix

before adding a relation to a shared collection, check what that collection is defined to hold and which referrer lists the relation would join; defer the field and record the gap when it does not fit

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before adding a relation to a shared collection, check what the collection holds and which referrer lists it joins; defer and record a gap if it does not fit

## Related

[INC-0173](./INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md) [INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md)
