---
id: INC-0226
title: A hand-made merge could differ from the mechanical merge unnoticed
date: 2026-10-31
classes: [vcs-destruction, identity-and-keying]
severity: medium
status: fixed
---

# INC-0226 - A hand-made merge could differ from the mechanical merge unnoticed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The extra changes sat inside a large merge.

## What happened

A hand-made merge was not compared with a mechanical merge of the same parents.

## Root cause

A hand-made merge was not compared with a mechanical merge of the same parents.

## Why it was hard to see

Merge commits are large and look plausible.

## Fix

Compare its tree with a mechanical merge of the same parents; the only allowed difference is the hand-resolved conflict file

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify a hand-made merge against a mechanical merge of the same parents

## Related

[INC-0175](./INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md)
