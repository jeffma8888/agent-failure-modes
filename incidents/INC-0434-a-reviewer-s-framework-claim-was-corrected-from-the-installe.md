---
id: INC-0434
title: A reviewer's framework claim was corrected from the installed source: a draft save writes only the versions table
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0434 - A reviewer's framework claim was corrected from the installed source: a draft save writes only the versions table

**Cost:** No wrong assertion entered the tests or the spec.

## Signature - how you recognise it

A reviewer stated a framework behavior that the installed source does not show.

## What happened

a reviewer's claim about what a draft save writes was corrected from the installed framework source: a draft save writes only the versions table

## Root cause

the claim was made from memory of the framework, not from the installed version

## Why it was hard to see

The claim was plausible and from a trusted reviewer.

## Fix

verify a reviewer's framework claim in the installed source before adopting it, and cite the source

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify a reviewer's framework claim in the installed source before adopting it, and cite the source

## Related

[INC-0062](./INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md) [INC-0425](./INC-0425-a-framework-operation-order-showed-that-file-data-is-generat.md)
