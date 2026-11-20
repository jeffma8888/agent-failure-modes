---
id: INC-0241
title: Automated tests passed while nobody had walked the real site
date: 2026-10-31
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
topic: false-green/real-page-or-response-wrong-behind-green
occurrences: 2
---

# INC-0241 - Automated tests passed while nobody had walked the real site

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [Tests pass but the real page, status or session is wrong](../catalog/false-green/real-page-or-response-wrong-behind-green.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The suite covered what was written, not what a person would click.

## What happened

Nobody walked the real site after a milestone, so defects in the real flow were not covered by any test.

## Root cause

Nobody walked the real site after a milestone, so defects in the real flow were not covered by any test.

## Why it was hard to see

Green tests look like a working site.

## Fix

Every defect found becomes a failing test before the fix

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Walk the real site after each milestone and feature close, and write each defect as a failing test first

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0496](./INC-0496-an-acceptance-record-was-ready-for-signature-with-every-test.md) - 2026-11-02 - An acceptance record was ready for signature with every test tier green while the main page of the row was blank

## Related

[INC-0244](./INC-0244-a-correct-not-found-page-was-served-with-a-200-status.md)
