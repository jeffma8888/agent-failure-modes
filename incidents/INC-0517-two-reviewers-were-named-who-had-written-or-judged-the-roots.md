---
id: INC-0517
title: Two reviewers were named who had written or judged the roots they were to review, and both stopped at the author check
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
---

# INC-0517 - Two reviewers were named who had written or judged the roots they were to review, and both stopped at the author check

**Cost:** Two reviews were delayed and reassigned, plus a third review moved.

## Signature - how you recognise it

A reviewer is named without reading the root author line and review history, and the reviewer author check refuses.

## What happened

Two reviews were assigned to teammates who had written or judged the root of the slice under review. Both stopped at their own author check, which was correct. The reviews were reassigned, and the assigner now reads the root coverage author line and its review history before naming a reviewer.

## Root cause

The assignment relied on the reviewer own check as the only author check.

## Why it was hard to see

The author line is in a short file that is easy to skip, and each reviewer looked eligible on the slice alone.

## Fix

Read the author line and review history of the root before naming the reviewer.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before naming a reviewer, read the root coverage author line and review history; the reviewer own author check is the second line, not the first.

## Related

[INC-0502](./INC-0502-an-implementer-was-assigned-after-checking-only-who-wrote-th.md) [INC-0507](./INC-0507-an-independence-rule-did-not-say-what-counts-as-an-agent-or.md)
