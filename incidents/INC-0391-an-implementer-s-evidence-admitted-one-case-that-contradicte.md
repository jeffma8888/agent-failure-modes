---
id: INC-0391
title: An implementer's evidence admitted one case that contradicted its own every-undeclared-case-throws rule
date: 2026-11-01
classes: [spec-and-scope]
severity: medium
status: fixed
---

# INC-0391 - An implementer's evidence admitted one case that contradicted its own every-undeclared-case-throws rule

**Cost:** A rule with a silent exception would have let one undeclared case through.

## Signature - how you recognise it

The evidence listed a case the stated rule said could not exist.

## What happened

an implementer's evidence admitted one case that contradicted its own rule that every undeclared case throws; the lead ruled that the rule wins and the code changes, not the wording

## Root cause

the rule was weakened to match what the code did, instead of the code being fixed

## Why it was hard to see

Rewording the rule is cheaper than changing the code, and both leave the evidence consistent.

## Fix

Change the code to match the stated rule; do not reword the rule to fit the evidence

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When evidence contradicts a stated rule, the rule wins: change the code, not the wording

## Related

[INC-0378](./INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md) [INC-0376](./INC-0376-a-signed-design-heading-outranked-a-plan-census-parenthetica.md)
