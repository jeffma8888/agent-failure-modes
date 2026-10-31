---
id: INC-0175
title: A merge of main left an activation due and went red
date: 2026-10-30
classes: [identity-and-keying, checkpoint]
severity: medium
status: fixed
---

# INC-0175 - A merge of main left an activation due and went red

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The merge commit was red on its own.

## What happened

A merge of main into a branch carrying another row activations did not carry every activation that main new markers made due.

## Root cause

The merge was treated as plumbing.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Carry every due activation in the same commit.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A merge of main carries every activation its new markers make due.

## Related

[INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md)
