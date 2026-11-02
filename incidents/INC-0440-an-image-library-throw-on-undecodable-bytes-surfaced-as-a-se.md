---
id: INC-0440
title: An image library throw on undecodable bytes surfaced as a server error instead of a refusal
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0440 - An image library throw on undecodable bytes surfaced as a server error instead of a refusal

**Cost:** The defect was fixed before the merge; no request was affected.

## Signature - how you recognise it

Malformed upload bytes produced a server error.

## What happened

the image metadata call could throw on bytes that pass the signature check but do not decode, which would surface as a server error; the lead ruled to catch the throw and refuse with a client error status and a fixed reason code, never to swallow it, with a unit case of a valid signature followed by garbage

## Root cause

the signature check passed, so the decoder was assumed to succeed

## Why it was hard to see

The check looked like input validation and stopped short of decoding.

## Fix

catch a library throw on untrusted input and refuse with a client error and a stable reason, and pin it with a case using a valid signature and bad body

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Catch a library throw on untrusted input and refuse with a client error status and a stable reason code; pin it with a valid-signature, bad-body case

## Related

[INC-0425](./INC-0425-a-framework-operation-order-showed-that-file-data-is-generat.md) [INC-0062](./INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md)
