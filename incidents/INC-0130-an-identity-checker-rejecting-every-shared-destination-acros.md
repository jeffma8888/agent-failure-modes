---
id: INC-0130
title: An identity checker rejecting every shared destination across pending roots flagged inert drafts
date: 2026-10-30
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0130 - An identity checker rejecting every shared destination across pending roots flagged inert drafts

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

Two pending drafts name one destination and the checker fails.

## What happened

An identity checker rejected every shared destination across pending roots, which flagged inert drafts that were not active.

## Root cause

Uniqueness was enforced across all pending roots instead of at activation.

## Why it was hard to see

Drafts overlap legitimately until one is activated.

## Fix

Check per manifest and resolve collisions at activation.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Enforce destination uniqueness where files become active.

## Related

[INC-0125](./INC-0125-a-marker-generator-listing-every-earlier-unmarked-root-made.md)
