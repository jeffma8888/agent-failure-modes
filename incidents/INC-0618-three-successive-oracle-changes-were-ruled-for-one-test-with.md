---
id: INC-0618
title: Three successive oracle changes were ruled for one test without first reading the whole framework function that mutates the object under test, so the engineer stopped three times
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0618 - Three successive oracle changes were ruled for one test without first reading the whole framework function that mutates the object under test, so the engineer stopped three times

**Cost:** Three engineer stops and three rulings for one test, each found only when the previous fix reached the next assertion.

## Signature - how you recognise it

Each fix to a test oracle passes its assertion and fails the next one that reads the same mutated object.

## What happened

A test compared a collection declaration with expectations, and the framework mutates that object in place during configuration. The first ruling moved the field reads to the sanitized config and did not check the other assertions reading it, so the loop over read-only fields met the framework's timestamp fields. The second ruling read the defaults function and fixed those, but not a later step of the same chain that deletes a default value, so a versions assertion failed. The third ruling read that step and also moved a second read to the sanitized config. Each ruling read only the part of the framework function that the current failure pointed at.

## Root cause

Oracle rulings were made from the part of the framework function the current failure touched, not from the whole chain that mutates the object.

## Why it was hard to see

Each fix was correct for the assertion it addressed, so the next failure looked like a new problem.

## Fix

Read the entire installed function chain that mutates the object end to end, and rule every affected assertion in one edit.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ruling an oracle that depends on framework behaviour, read the entire installed function chain end to end and rule every affected assertion at once.

## Related

[INC-0616](./INC-0616-a-signed-packet-required-a-tail-only-migration-rollback-but.md) [INC-0615](./INC-0615-a-gate-order-put-the-typecheck-right-after-type-generation-w.md) [INC-0612](./INC-0612-a-ruling-set-a-lock-wait-the-installed-lock-could-not-honour.md)
