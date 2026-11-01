---
id: INC-0275
title: A probe that sends a session cookie alone may test guest behavior
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0275 - A probe that sends a session cookie alone may test guest behavior

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A probe that sent only a session cookie silently tested guest behavior.

## What happened

a raw request carrying only the session cookie was not authenticated by the server (the current-user endpoint returned 200 with no user); with the matching Origin header the same request was staff

## Root cause

a raw request carrying only the session cookie was not authenticated by the server (the current-user endpoint returned 200 with no user); with the matching Origin header the same request was staff

## Why it was hard to see

The status code looks the same either way.

## Fix

Label cookie-only readings as unauthenticated and keep same-origin controls for the authenticated status

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Send every header an authenticated request needs, and run a control that proves the identity the probe claims

## Related

[INC-0273](./INC-0273-a-status-check-must-take-every-client-reading.md)
