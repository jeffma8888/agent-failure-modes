---
id: INC-0523
title: Three test roots by three authors used the same guessed locator for a generated field that the installed library does not render
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0523 - Three test roots by three authors used the same guessed locator for a generated field that the installed library does not render

**Cost:** Every root with the guess was defective on unchanged main and needed a successor; found by reading installed source.

## Signature - how you recognise it

Several browser tests scope a generated field by a role or label that its library never renders.

## What happened

Three browser roots by three authors scoped a generated upload field with a group role or one of two guessed button labels. The installed source renders the field as a plain element with an id built from its path, with a fixed button label from the installed translations, shown only while the field has no value. One pattern was set for every generated upload field, bound to a cited source line. A capture showed that generated group fields also lack a group role.

## Root cause

Locators were written from how the field should look, not from the source that renders it.

## Why it was hard to see

The same plausible guess occurs to every author, so agreement among the roots looked like confirmation.

## Fix

Bind each locator for a generated field to the installed source line that renders it, and audit the other roots for the same guess.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not guess a locator for a generated field; cite the installed source line that renders it, and when one guess is found, audit every root for the same guess.

## Related

[INC-0499](./INC-0499-the-first-defect-of-a-kind-prompted-an-audit-of-the-whole-ki.md) [INC-0506](./INC-0506-two-fields-claimed-the-same-publication-state-and-the-seed-w.md)
