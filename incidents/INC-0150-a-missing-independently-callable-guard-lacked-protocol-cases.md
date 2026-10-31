---
id: INC-0150
title: A missing independently callable guard lacked protocol cases, and macOS path aliases looked like regressions
date: 2026-10-30
classes: [detector-fail-open, test-isolation]
severity: medium
status: fixed
---

# INC-0150 - A missing independently callable guard lacked protocol cases, and macOS path aliases looked like regressions

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A guard without its own tests and cwd assertions failing on path aliases.

## What happened

A guard that could not be called independently had no negative protocol cases or positive controls. Regression failures were also misread, because macOS path aliases fail cwd-string assertions without any runtime location error.

## Root cause

Failures were attributed before comparing to the active bytes.

## Why it was hard to see

A path alias error looks like a real change.

## Fix

Give the guard negative protocol cases and positive controls, and compare failures against active bytes before attributing them.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Resolve paths before comparing, and compare to the active bytes first.

## Related

[INC-0110](./INC-0110-a-cross-row-test-needed-setup-absent-from-its-own-lifecycle.md) [INC-0116](./INC-0116-two-validators-enforcing-the-same-rule-masked-single-file-mu.md)
