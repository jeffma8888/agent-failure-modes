---
id: INC-0153
title: A test checked only the dispatch argv of a child stage, not its semantics
date: 2026-10-30
classes: [false-green, test-isolation]
severity: medium
status: fixed
---

# INC-0153 - A test checked only the dispatch argv of a child stage, not its semantics

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A stage is proven by what it was called with, not by what it did.

## What happened

A test covered the dispatch argv of a child stage and not the child stage behavior, and a database could survive into a later inventory owning stage.

## Root cause

The argv was easy to assert and the behavior was not.

## Why it was hard to see

The call is correct and the stage still misbehaves.

## Fix

Test child-stage semantics, and prove no database survives into a later stage.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Test what a stage does, not how it was started.

## Related

[INC-0138](./INC-0138-a-stage-that-kept-a-database-alive-collided-with-later-inven.md)
