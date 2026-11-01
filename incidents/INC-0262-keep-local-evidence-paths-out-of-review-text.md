---
id: INC-0262
title: Keep local evidence paths out of review text
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0262 - Keep local evidence paths out of review text

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A review cited a private local folder in committed text.

## What happened

a reviewer committed text that cited a private local evidence folder; the lead redacted it at landing

## Root cause

a reviewer committed text that cited a private local evidence folder; the lead redacted it at landing

## Why it was hard to see

The reviewer sees the path as useful evidence.

## Fix

Ask reviewers to keep local evidence paths out of the review text

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Keep local evidence paths out of committed review text

## Related

[INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md)
