---
id: INC-0232
title: A prompt render succeeded without reading the card bodies
date: 2026-10-31
classes: [false-green, delegation]
severity: medium
status: fixed
---

# INC-0232 - A prompt render succeeded without reading the card bodies

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The render referenced the cards by path only.

## What happened

A successful prompt render was taken as evidence of card content, but it referenced the cards by path without reading their bodies.

## Root cause

A successful prompt render was taken as evidence of card content, but it referenced the cards by path without reading their bodies.

## Why it was hard to see

The render succeeds either way.

## Fix

Verify the card bytes on their own

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify external card bytes separately from a successful prompt render

## Related

[INC-0177](./INC-0177-card-text-pointed-at-its-own-directory-as-the-checkout.md)
