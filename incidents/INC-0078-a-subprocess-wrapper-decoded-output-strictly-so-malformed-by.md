---
id: INC-0078
title: A subprocess wrapper decoded output strictly, so malformed bytes skipped the retry and redaction path
date: 2026-10-30
classes: [detector-fail-open, false-green]
severity: medium
status: fixed
---

# INC-0078 - A subprocess wrapper decoded output strictly, so malformed bytes skipped the retry and redaction path

**Cost:** Moderate: a run made one try instead of three, wrote no failure event and printed raw exception text, the one path the design was meant to close. Caught in review before release.

## Signature - how you recognise it

A wrapper runs an external command with strict text decoding, and every test feeds it clean strings.

## What happened

A credential provider ran its command with strict text decoding. Invalid bytes on the output raised a decode error before the wrapper's typed failure handling. The run exited as an internal error with the exception text, with no retry and no failure record. All tests used fake runners that returned clean text.

## Root cause

Decoding sat outside the failure boundary around the call, so one class of input bypassed every handler built for the call's failures. Fakes cannot produce malformed bytes.

## Why it was hard to see

The code path looks fully handled because the typed handlers exist, and the only inputs that miss them are ones test doubles never emit.

## Fix

Decode with replacement inside the same boundary, map any residual decode error to a fixed failure kind, and add tests that run a real process emitting invalid bytes.

## Verification

Checked: the revised wrapper against real subprocess fixtures that emit invalid bytes. Not checked: other wrappers in the codebase for the same pattern.

## Transferable rule

> Put transport decoding inside the same failure boundary as the call, and test the boundary with a real process emitting malformed bytes, not only fakes returning clean text.

## Related

[INC-0068](./INC-0068-a-retry-ladder-wrapped-the-model-call-but-not-the-credential.md) [INC-0033](./INC-0033-one-normaliser-is-not-enough-if-it-maps-the-two-sides-into-d.md)
