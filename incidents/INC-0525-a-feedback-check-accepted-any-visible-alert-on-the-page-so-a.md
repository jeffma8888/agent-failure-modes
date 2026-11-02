---
id: INC-0525
title: A feedback check accepted any visible alert on the page, so a stale alert could satisfy it
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0525 - A feedback check accepted any visible alert on the page, so a stale alert could satisfy it

**Cost:** A refusal case could pass with no refusal feedback produced by the action under test.

## Signature - how you recognise it

An assertion looks for any visible alert, and an alert from earlier or from another field satisfies it.

## What happened

A root check for refusal feedback accepted any visible alert element. An alert already on the page, or one belonging to another field, could satisfy it. Each refusal now asserts that no matching error element is present before submission and one is present after the response, on a fresh form, and the field-specific case binds to that field scope with a named product mutation that moves or removes its error.

## Root cause

The assertion tested the presence of an alert and not the change caused by the action.

## Why it was hard to see

On a page with several alerts the check passes in every run, including runs where the product is broken.

## Fix

Assert absence before and presence after, on a fresh form, scoped to the field.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A feedback assertion must fail without the action under test: assert the element is absent before the action and present after it, on a fresh page and scoped to the field, never on any alert on the page.

## Related

[INC-0505](./INC-0505-a-run-command-silently-dropped-a-named-option-and-three-test.md) [INC-0497](./INC-0497-a-flag-that-hides-the-token-from-responses-left-first-user-r.md)
