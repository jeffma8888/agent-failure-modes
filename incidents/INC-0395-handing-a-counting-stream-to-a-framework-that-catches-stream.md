---
id: INC-0395
title: Handing a counting stream to a framework that catches stream failures lost the custom refusal contract
date: 2026-11-02
classes: [spec-and-scope]
severity: medium
status: fixed
---

# INC-0395 - Handing a counting stream to a framework that catches stream failures lost the custom refusal contract

**Cost:** The agreed refusal behavior would have been replaced by the framework's default error.

## Signature - how you recognise it

A custom refusal never reached the caller once the framework wrapped the stream.

## What happened

handing a counting stream to a framework that catches stream failures lost the custom refusal contract, because the framework turned the refusal into its own error

## Root cause

the refusal was raised inside the stream, where the framework catches failures

## Why it was hard to see

The refusal works in isolation and is lost only after the handover.

## Fix

Own the refusal before handing the stream over

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Own the refusal contract before handing a stream to a framework that catches stream failures

## Related

[INC-0077](./INC-0077-keeping-an-error-prefix-did-not-keep-the-downstream-classifi.md)
