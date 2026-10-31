---
id: INC-0206
title: A guessed commit id was sent to two teammates
date: 2026-10-30
classes: [delegation, observability]
severity: medium
status: fixed
---

# INC-0206 - A guessed commit id was sent to two teammates

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Two teammates received a wrong id.

## What happened

A guessed commit id for a landing was sent to two teammates, who then needed corrections.

## Root cause

A guessed commit id for a landing was sent to two teammates, who then needed corrections.

## Why it was hard to see

The guess was nearly right.

## Fix

Send the id only after git has printed it

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never cite a commit id in a message before git has printed it

## Related

[INC-0185](./INC-0185-rename-detection-reported-a-false-rename-in-a-merge.md)
