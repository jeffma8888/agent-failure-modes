---
id: INC-0378
title: A default that silently let a guard pass made a reviewer read a requirement as met
date: 2026-11-01
classes: [detector-fail-open]
severity: medium
status: fixed
---

# INC-0378 - A default that silently let a guard pass made a reviewer read a requirement as met

**Cost:** A requirement looked satisfied while the guard had checked nothing.

## Signature - how you recognise it

A guard passed on an input it had never been told about.

## What happened

a default that silently lets a guard pass (a never-locked slug) led a reviewer to read a requirement as met, when nothing had been checked

## Root cause

the default for an unknown slug was to allow, so a missing configuration looked like a pass

## Why it was hard to see

A pass from a default is indistinguishable from a pass from a real check.

## Fix

Prefer fail closed: when the input is missing or unknown, stop with an explicit configuration error rather than pass

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A guard must fail closed with an explicit configuration error; never let a default make it pass

## Related

[INC-0372](./INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) [INC-0332](./INC-0332-a-tier-exclusion-matched-only-one-file-extension.md) [INC-0391](./INC-0391-an-implementer-s-evidence-admitted-one-case-that-contradicte.md) [INC-0394](./INC-0394-a-security-predicate-checked-for-truthiness-failed-open-on-a.md) [INC-0404](./INC-0404-a-safe-default-could-silently-drop-data-when-an-uncertain-st.md) [INC-0431](./INC-0431-interim-content-was-signed-as-clearly-marked-placeholder-cop.md) [INC-0438](./INC-0438-a-lint-rule-against-a-throw-inside-a-finally-block-caught-a.md)
