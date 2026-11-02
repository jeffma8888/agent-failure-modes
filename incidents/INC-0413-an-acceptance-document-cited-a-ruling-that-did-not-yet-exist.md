---
id: INC-0413
title: An acceptance document cited a ruling that did not yet exist when it was signed
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0413 - An acceptance document cited a ruling that did not yet exist when it was signed

**Cost:** A signed record pointed at text that could still change or never be written.

## Signature - how you recognise it

A signed record referred to a ruling that was not yet written.

## What happened

an acceptance document cited a ruling that did not yet exist when it was signed

## Root cause

the ruling was expected and cited as if it had been made

## Why it was hard to see

The citation read like any other, and the ruling followed within minutes.

## Fix

Cite only rulings that exist at signing, or write that the item is to be ruled

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A signed record cites only rulings that exist, or says the item is to be ruled

## Related

[INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) [INC-0376](./INC-0376-a-signed-design-heading-outranked-a-plan-census-parenthetica.md)
