---
id: INC-0487
title: A setting that strips tokens from responses also stripped them from the test helper
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0487 - A setting that strips tokens from responses also stripped them from the test helper

**Cost:** Minor: a database probe stayed red on cases that looked like product auth failures, until the probe itself was repaired.

## Signature - how you recognise it

Every auth check downstream of a local login failed, and the token was empty at the first step.

## What happened

A probe logged in through the framework local operation, which deletes the token from its result because the collection removes tokens from responses. The probe then sent a cookie holding the string undefined, verification failed quietly into an empty user, and the refresh cases were refused as forbidden downstream of a token that never existed. A separate direct write without a required field failed on a null constraint before its conflict update. Seven setup defects in all, and none was a product defect.

## Root cause

The security setting that sanitizes responses applies to local callers too, and the probe read the token from the sanitized result.

## Why it was hard to see

The failures looked like real auth refusals, and the verification step swallowed its own error, so nothing pointed at the missing token.

## Fix

Call the underlying login operation with a real local request and unchanged configuration, capture the token before the response is sanitized, assert it is a nonempty string for the expected user, keep it in memory only, and prove the repaired cases with mutations that go red for the right reason.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a security setting strips tokens from responses, it strips them from local test helpers too; capture the token before the response is sanitized and assert it is present, or every downstream auth check fails at its precondition and looks like a product defect.

## Related

[INC-0275](./INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md)
