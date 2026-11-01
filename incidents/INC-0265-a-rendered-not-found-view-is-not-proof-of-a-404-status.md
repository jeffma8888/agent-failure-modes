---
id: INC-0265
title: A rendered not-found view is not proof of a 404 status
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0265 - A rendered not-found view is not proof of a 404 status

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A not-found page was rendered with a 200 status.

## What happened

a page-level notFound call after the application shell had streamed could not change the HTTP status, and the attempted early call still answered 200 for an unknown path

## Root cause

a page-level notFound call after the application shell had streamed could not change the HTTP status, and the attempted early call still answered 200 for an unknown path

## Why it was hard to see

The page looks right to a human and to a content check.

## Fix

Decide existence before the first response bytes are committed, and assert the status code

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Treat a rendered not-found view as no proof of 404; check the HTTP status once streaming has committed the shell

## Related

[INC-0244](./INC-0244-a-correct-not-found-page-was-served-with-a-200-status.md) [INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md)
