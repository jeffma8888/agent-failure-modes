---
id: INC-0600
title: Two branches each green alone with a clean merge-tree went red together, because one sanctioned product change altered the label the other test selected by
date: 2026-11-04
classes: [test-isolation]
severity: high
status: mitigated
---

# INC-0600 - Two branches each green alone with a clean merge-tree went red together, because one sanctioned product change altered the label the other test selected by

**Cost:** A full run went red on one end-to-end case after both merges, and the next run, the go decision and the manual walk waited for a successor test.

## Signature - how you recognise it

A test passes on its own branch and the merged tree is red with no textual conflict.

## What happened

One branch changed which field a relationship combobox uses as its title, so categories are listed and searched by slug instead of id. Another branch added an end-to-end test that fills the combobox with the id and picks the option named by the id. Each branch was green alone, the merge-tree was clean, and both merged. The first full run that reached the end-to-end step after both was red on that case: expected one option, received none. This was a test assumption broken by a sanctioned change, not a product defect. A successor test fills the slug instead, was run before approval, and a mutant that reverts the title setting turns it red.

## Root cause

The test was activated on a branch whose base lacked the product change, and no check ran the merged result before the full run.

## Why it was hard to see

A clean merge-tree and two green branches say nothing about a selector that depends on a label the other branch changed.

## Fix

Write a successor that selects by the new label, run it before approval on current main with a mutant that reverts the label, and audit every other spec for a selection by the old label.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A clean merge-tree and two green branches do not show the merge is green; before merging a test that selects by a visible label, run it on a base that holds every sanctioned label change, and audit other specs for the old label.

## Related

[INC-0160](./INC-0160-an-activation-was-tied-to-an-unreviewed-successor-and-had-to.md) [INC-0594](./INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md)
