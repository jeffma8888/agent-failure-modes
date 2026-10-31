---
id: INC-0173
title: A ruling widened a shared valid state and only some payloads followed
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0173 - A ruling widened a shared valid state and only some payloads followed

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Some negatives passed against the tip only.

## What happened

A ruling widened a shared valid state, and not every payload that builds the state was changed; negatives were proved only against the tip.

## Root cause

Payloads were updated one at a time.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Change every payload and prove each negative against both the defective and the fixed checker.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a ruling widens a shared valid state, change every payload that builds it.

## Related

[INC-0151](./INC-0151-a-hygiene-rule-against-conditional-test-omission-needed-a-pr.md)
