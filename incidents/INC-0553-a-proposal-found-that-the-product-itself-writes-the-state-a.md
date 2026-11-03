---
id: INC-0553
title: A proposal found that the product itself writes the state a fixture needed, which turned a validation-bypass question into a product path
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0553 - A proposal found that the product itself writes the state a fixture needed, which turned a validation-bypass question into a product path

**Cost:** None. The sanctioned fixture path replaced a forbidden database bypass.

## Signature - how you recognise it

A fixture needs a record that normal validation would refuse, which suggests bypassing validation.

## What happened

A proposal for a test fixture needed a record with only one language, and a ruling had forbidden ad hoc validation bypass. The proposer found that a draft save through the product own create route is product behavior, because the draft path skips validation by design, and that publishing without the second language is refused. The lead accepted that route as the sanctioned fixture path with a readback before the browser step, a guard against the walk database, a reset and reseed afterwards, and a stop with no silent fallback to SQL if the create is refused.

## Root cause

The fixture question assumed a bypass was needed before the product paths were read.

## Why it was hard to see

The state looked impossible to create through the product until the draft path was read.

## Fix

Read the product write paths first; use the product own route, and stop instead of silently falling back to SQL.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before bypassing validation for a fixture, look for a product path that writes the state; if none works, stop and report rather than fall back to SQL.

## Related

[INC-0549](./INC-0549-a-reviewer-wrote-its-own-browser-only-driver-to-reach-a-muta.md)
