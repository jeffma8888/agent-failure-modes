---
id: INC-0191
title: A one-parser requirement was pinned by only one kind of test
date: 2026-10-30
classes: [spec-and-scope, detector-fail-open]
severity: medium
status: fixed
---

# INC-0191 - A one-parser requirement was pinned by only one kind of test

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A second parser could appear without failing a test.

## What happened

A one-parser requirement was pinned structurally or behaviorally, not both, so a second parser could either hide in another file or diverge on an input no test used.

## Root cause

A one-parser requirement was pinned structurally or behaviorally, not both, so a second parser could either hide in another file or diverge on an input no test used.

## Why it was hard to see

Each pin looks sufficient alone.

## Fix

Pin structurally (no other file names the registry) and behaviorally (the input where a second parser would diverge)

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Pin a one-parser requirement both structurally and behaviorally

## Related

[INC-0159](./INC-0159-a-second-reader-of-the-same-registry-file-was-at-risk-of-rep.md)
