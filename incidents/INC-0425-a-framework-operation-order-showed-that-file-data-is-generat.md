---
id: INC-0425
title: A framework operation order showed that file data is generated before the field validators, so a security check moved to the operation hook
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0425 - A framework operation order showed that file data is generated before the field validators, so a security check moved to the operation hook

**Cost:** No bad file was accepted; the placement was corrected before the production code was accepted.

## Signature - how you recognise it

A content check ran after the framework had already rewritten the input it was meant to inspect.

## What happened

the design placed the upload content sniff in the field-validation hook, but the installed framework source shows that file data generation can replace the file type and decode the upload before any field validator runs; the engineer's correction was verified at line level in the installed source and the sniff moved to the operation hook, ahead of generation, inspecting the original bytes, with the file-size guard first

## Root cause

the design assumed a hook order that the installed framework does not have

## Why it was hard to see

The design text and the hook name looked right; only the installed source showed the order.

## Fix

read the installed framework operation order before placing a security check, and put a check on original input in a hook that runs before the framework transforms the input; record the move as a named deviation from the design

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Place a security check on original input in a hook that runs before the framework transforms the input, verified in the installed source, and record any move as a named deviation

## Related

[INC-0062](./INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md) [INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md)
