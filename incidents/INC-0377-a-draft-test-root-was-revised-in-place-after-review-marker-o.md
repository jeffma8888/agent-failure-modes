---
id: INC-0377
title: A draft test root was revised in place after review, marker or activation
date: 2026-11-01
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0377 - A draft test root was revised in place after review, marker or activation

**Cost:** Edits to a reviewed root would have made earlier review and activation records describe different bytes.

## Signature - how you recognise it

A root that others had reviewed or marked could be edited in place.

## What happened

a draft test root may be revised in place only while it has no review, marker or activation; once any of these exists a change must be a successor

## Root cause

the rule for when a draft stops being editable was not stated

## Why it was hard to see

A small in-place edit looks harmless, and the records that pin the old bytes are elsewhere.

## Fix

Revise a draft in place only before review, marker or activation; after that write a successor and supersede it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Revise a draft test root in place only while it has no review, marker or activation; after that only a successor

## Related

[INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md)
