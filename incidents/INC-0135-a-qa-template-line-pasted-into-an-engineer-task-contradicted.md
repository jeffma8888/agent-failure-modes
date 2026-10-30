---
id: INC-0135
title: A QA-template line pasted into an engineer task contradicted the engineer commit duty
date: 2026-10-30
classes: [delegation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0135 - A QA-template line pasted into an engineer task contradicted the engineer commit duty

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

A task carries an instruction from another role template.

## What happened

A QA-template line, do not commit, was pasted into an engineer task and contradicted the engineer commit duty.

## Root cause

Templates for different roles were mixed in one brief.

## Why it was hard to see

Each line is valid in its own template.

## Fix

Keep role-specific templates apart.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> One template per role.

## Related

[INC-0087](./INC-0087-an-import-level-audit-missed-helper-calls-that-needed-a-late.md)
