---
id: INC-0497
title: A flag that hides the token from responses left first-user registration with an empty session cookie
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0497 - A flag that hides the token from responses left first-user registration with an empty session cookie

**Cost:** The first user of an empty system could register but not stay signed in, found only by a browser probe after the hardening tests were green.

## Signature - how you recognise it

Registration returned success and stored the admin, and the browser landed on the login page.

## What happened

A hardening flag on the staff collection removes the token from auth responses. The local login operation deletes the token under that flag, and the first-user registration takes its token from that local call, so its cookie was built from a deleted token. The registration returned success, stored the admin with its roles, and set a session cookie with an empty value. The next page request sent the empty cookie and was redirected to login. Tests written for the flag proved the token absent from every response body, but nothing checked that first-user registration still signs the user in. Cookie attributes and roles were not the cause.

## Root cause

The flag was tested for what it hides and not for the flows that need the hidden credential to finish.

## Why it was hard to see

The hidden-token tests were green, the registration returned success and stored the right data, and the failure showed only in the browser after the redirect.

## Fix

Add an integration case on an empty database that expects success, a non-empty session cookie and a body with no token, observe it red first, then take the token from the login operation that does not delete it, keeping the flag on.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a change hides or removes a credential from responses, test every flow that needs that credential to finish, not only that it is hidden.

## Related

[INC-0487](./INC-0487-a-setting-that-strips-tokens-from-responses-also-stripped-th.md) [INC-0496](./INC-0496-an-acceptance-record-was-ready-for-signature-with-every-test.md)
