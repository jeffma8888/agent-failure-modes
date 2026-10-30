---
id: INC-0134
title: A QA case followed only 3xx redirects while Payload 3 admin redirects under Next 16 are soft redirects with HTTP 200
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0134 - A QA case followed only 3xx redirects while Payload 3 admin redirects under Next 16 are soft redirects with HTTP 200

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

A test expecting a 3xx fails on a correct redirect.

## What happened

Payload 3 admin redirects under Next 16 are RSC soft redirects with HTTP 200, so a QA case that followed only 3xx was stricter than its row. Next 16 also rewrites next-env.d.ts on every dev start.

## Root cause

The test assumed classic HTTP redirects.

## Why it was hard to see

The page redirects for the user, so the failure looks like a product bug.

## Fix

Assert the user-visible destination, and account for the regenerated type file.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Assert what the user sees, not the transport mechanism.
