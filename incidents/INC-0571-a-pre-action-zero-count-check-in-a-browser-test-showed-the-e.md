---
id: INC-0571
title: A pre-action zero-count check in a browser test showed the error selector already matched one element before any action
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0571 - A pre-action zero-count check in a browser test showed the error selector already matched one element before any action

**Cost:** None. The activation was stopped before a mutant or retry, and the cause is under a probe.

## Signature - how you recognise it

The error-visible selector matches an element before the action under test.

## What happened

The unchanged-product baseline of a new root failed in one case at a count-zero check before the save: the error selector matched one element for the full wait before the save action. The other cases and setup passed. Without the pre-action check, the post-action visibility check would have passed for the wrong reason. The agent stopped with no retry and no edit, which the lead confirmed was right, because the result is neither a product result nor a mutant kill and the root was approved without a run. The element is unknown, and a lead hypothesis of a framework live region outside the form is to be bound by a probe.

## Root cause

The selector is broader than the error element it was meant to find.

## Why it was hard to see

Without the precondition check, the visible-after-action assertion cannot tell the new error from the old element.

## Fix

Assert the zero count before the action, and bind the selector by a probe.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Assert that an error selector matches nothing before the action; otherwise a post-action visibility check can pass for the wrong reason.

## Related

[INC-0559](./INC-0559-a-successor-root-was-authored-and-approved-without-a-run-and.md) [INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md)
