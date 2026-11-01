---
id: INC-0245
title: A third-party avatar request was made without anyone noticing
date: 2026-11-01
classes: [spec-and-scope, observability]
severity: medium
status: fixed
---

# INC-0245 - A third-party avatar request was made without anyone noticing

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The page looked right and still contacted a third party.

## What happened

A third-party avatar request left the site while the page looked correct and no test watched outbound requests.

## Root cause

A third-party avatar request left the site while the page looked correct and no test watched outbound requests.

## Why it was hard to see

The visual result is unchanged.

## Fix

Make the defect a failing QA root first, then fix it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Assert that a page makes no request to a third-party origin unless declared

## Related

[INC-0211](./INC-0211-a-regex-literal-was-read-as-a-file-path-by-the-permission-ch.md)
