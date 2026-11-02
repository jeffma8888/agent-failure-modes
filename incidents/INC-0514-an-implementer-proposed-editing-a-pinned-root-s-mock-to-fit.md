---
id: INC-0514
title: An implementer proposed editing a pinned root's mock to fit a new helper contract, and the fix was a wrapper that kept the mocked shape
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: mitigated
---

# INC-0514 - An implementer proposed editing a pinned root's mock to fit a new helper contract, and the fix was a wrapper that kept the mocked shape

**Cost:** One round trip; the proposal was refused before any edit, so no identity failure occurred.

## Signature - how you recognise it

A new return contract is incompatible with a pinned test's mock, and the proposed fix edits the pinned file.

## What happened

An implementer asked to change the return value of a mock in an activated test root so that it fits a new helper return contract. The file was bound by the root manifest, so the edit would fail the identity check, and an implementer may not edit a root. The first choice was to leave the return shape of every mocked function unchanged and carry the new fields in a new function or wrapper called only by the seed module. Only if that cannot work does another author write a successor root with the mechanical change.

## Root cause

The new contract was fitted to the product helper first and the pinned test double was then expected to follow.

## Why it was hard to see

Editing a two-line mock looks harmless, and the pin is visible only to the identity check.

## Fix

Adapt the product code around the pinned test double with a new function or wrapper, and change the test only through a successor root authored by someone else.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a new contract collides with a pinned test mock, keep the mocked function return shape and add a new function or wrapper for the new contract; change the test only through a successor root authored by someone else.

## Related

[INC-0473](./INC-0473-a-test-file-was-edited-on-order-although-its-digest-was-pinn.md)
