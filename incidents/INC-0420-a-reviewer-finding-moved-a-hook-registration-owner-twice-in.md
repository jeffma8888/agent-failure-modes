---
id: INC-0420
title: A reviewer finding moved a hook registration owner twice in one hour
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0420 - A reviewer finding moved a hook registration owner twice in one hour

**Cost:** Two plan rows were rewritten and then rewritten again.

## Signature - how you recognise it

The owner of one registration changed twice in about an hour.

## What happened

a reviewer's finding moved a hook registration owner twice in one hour (T05a, then T05b, then L4-T03); the owner was fixed only after reading which row owns the hook's neighbours

## Root cause

the first owner was chosen before the neighbouring rows were read

## Why it was hard to see

Each owner looked right until the next dependency was checked.

## Fix

assign a registration owner only after reading which row owns the hook's neighbours and what that row depends on

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Assign a hook registration owner only after reading which row owns the hook's neighbours

## Related

[INC-0149](./INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md) [INC-0298](./INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md)
