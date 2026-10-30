---
id: INC-0083
title: Controls that fail in only one direction, a drop guard keyed on a name pattern, and refusal tests satisfied by unrelated connection errors
date: 2026-10-30
classes: [false-green, identity-and-keying]
severity: medium
status: fixed
---

# INC-0083 - Controls that fail in only one direction, a drop guard keyed on a name pattern, and refusal tests satisfied by unrelated connection errors

**Cost:** Caught in a re-check of revised tests; several cases could not have detected the guard they were meant to prove.

## Signature - how you recognise it

Refusal tests pass against a stub that accepts everything, or against a guard that does nothing because the target is unreachable anyway.

## What happened

Refusal cases did not fail an always-accept stub, and valid controls did not fail an always-refuse stub. A teardown guard that dropped by name pattern also matched resources owned by the harness. Fresh-child refusal tests passed on connection or module errors from a bad host or port.

## Root cause

Each test checked one direction only, and the guard and the refusal assertions used broad matches instead of a recorded set and a specific error.

## Why it was hard to see

Every test is green with a correct guard and also with a missing one, so only a deliberately wrong stub reveals the gap.

## Fix

Run refusal cases against an always-accept stub and valid controls against an always-refuse stub, both must fail. Have the drop guard check a recorded set of created names. In fresh-child refusal tests exclude connection and module errors.

## Verification

Checked by re-reading the revised tests against these stubs. Not checked: execution, the suites were pending.

## Transferable rule

> A control counts only if it fails in both directions; scope destructive guards to recorded identities, and assert the specific refusal, not any error.

## Related

[INC-0078](./INC-0078-a-subprocess-wrapper-decoded-output-strictly-so-malformed-by.md)
