---
id: INC-0528
title: A fix gave a list column a custom cell and dropped the default cell's link to the record, so the list lost its only way to open a record
date: 2026-11-02
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0528 - A fix gave a list column a custom cell and dropped the default cell's link to the record, so the list lost its only way to open a record

**Cost:** The list had no link from a row to its editor from the fix until it was found in review; a new row and a root red by design were created for the repair.

## Signature - how you recognise it

A custom cell component replaces the default cell, and the default cell carried the record link.

## What happened

A fix for localized display gave the first list column a custom cell component. Installed source shows that a field with a custom cell is rendered through it and the default cell, which carries the link to the record, is never used. The custom cell returns a plain span, so the list lost the link from a row to its editor. The link was ruled required admin behavior. The regression root does not assert it, because it must be green on the current code. A new row owns the link, with a root red by design, and a later fix must keep both the link and the localized display.

## Root cause

The change targeted one behavior, display, and replaced a component that also provided navigation.

## Why it was hard to see

The list still renders, the text is correct, and the missing behavior is a link nobody was looking at.

## Fix

Restore the link in the custom cell or the list configuration without losing the localized display.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Replacing a framework default cell, field or component replaces everything it did, not only what the change targeted; list what the default provided before replacing it, and test it.

## Related

[INC-0505](./INC-0505-a-run-command-silently-dropped-a-named-option-and-three-test.md) [INC-0506](./INC-0506-two-fields-claimed-the-same-publication-state-and-the-seed-w.md)
