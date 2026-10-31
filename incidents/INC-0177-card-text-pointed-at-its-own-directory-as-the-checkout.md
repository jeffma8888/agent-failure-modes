---
id: INC-0177
title: Card text pointed at its own directory as the checkout
date: 2026-10-30
classes: [tooling-paths, delegation]
severity: medium
status: fixed
---

# INC-0177 - Card text pointed at its own directory as the checkout

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

Cards broke silently when the card set moved.

## What happened

Card text pointed at its own directory as the checkout, and an override section sat beside the earlier duties it overrode.

## Root cause

The path was correct until the cards moved.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Grep every card for the executable path and remove overridden duties.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Grep every card for the executable path; do not keep a duty beside the section that overrides it.

## Related

[INC-0157](./INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md)
