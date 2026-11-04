---
id: INC-0579
title: A broad any-alert selector matched the framework's empty route announcer before any action, and a second whole-document probe found the real refusal messages in toasts
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0579 - A broad any-alert selector matched the framework's empty route announcer before any action, and a second whole-document probe found the real refusal messages in toasts

**Cost:** None. Two diagnosis-only probes replaced an invented oracle.

## Signature - how you recognise it

A union selector matches an empty framework element before the action under test.

## What happened

A pre-submit zero-count check on a union of alert selectors matched one element. A probe showed it was the framework route announcer, role alert, empty text, one pixel, in a shadow host outside the form. After saving, three refusal cases added no element matching the union, and a fourth added the form field error. The probe had looked at union matches only. A second diagnosis-only probe diffed every visible element that was not present after fill, including open shadow roots, plus the parsed save response. Every refusal then showed readable feedback: three as error toasts and one as the form field error, and a successor was authored bound to those elements.

## Root cause

The selector was written from the idea of an alert, not from the elements the product renders.

## Why it was hard to see

The probe looked only at what the selector matched, so it could not see a message in a toast.

## Fix

Probe the whole document, bind each element to installed source, and author the oracle from it.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before authoring an error oracle, diff the whole document, including shadow roots, and bind the new element to the installed source.

## Related

[INC-0571](./INC-0571-a-pre-action-zero-count-check-in-a-browser-test-showed-the-e.md)
