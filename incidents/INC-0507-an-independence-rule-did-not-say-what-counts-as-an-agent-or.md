---
id: INC-0507
title: An independence rule did not say what counts as an agent or as a part, and four of nine parallel slices stopped at once
date: 2026-11-02
classes: [delegation]
severity: medium
status: mitigated
---

# INC-0507 - An independence rule did not say what counts as an agent or as a part, and four of nine parallel slices stopped at once

**Cost:** Four of nine parallel slices stopped at the same time until the rule was clarified.

## Signature - how you recognise it

A rule says to stop if you authored or reviewed any part, and different agents read part and agent differently.

## What happened

An independence rule said to stop if you authored or reviewed any part of a root, without defining either term. One agent counted a different agent that ran on the same model as itself. Others counted a coverage-citation audit or a census table. Four of nine parallel slices stopped at once. The clarified rule is per agent instance, blocks on writing the test or judging its cases, and only requires disclosure for inventories, citation audits, allocation audits and compatibility proposals.

## Root cause

The rule used broad words and left the unit of independence and the list of blocking artifacts undefined.

## Why it was hard to see

A cautious reading of any part is always defensible, so each agent stopped correctly by its own reading and the loss showed only as idle slices.

## Fix

Define independence per agent instance. Name which artifacts block and which only need disclosure, and give the review to another model where one is free.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Define independence per agent instance, and name which artifacts block (wrote the test or judged its cases) and which only need disclosure (inventories, citation audits).

## Related

[INC-0502](./INC-0502-an-implementer-was-assigned-after-checking-only-who-wrote-th.md) [INC-0467](./INC-0467-a-run-plan-barred-the-test-author-from-running-the-script-an.md)
