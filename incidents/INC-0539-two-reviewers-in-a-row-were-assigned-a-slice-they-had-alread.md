---
id: INC-0539
title: Two reviewers in a row were assigned a slice they had already worked on, because the pick did not search the record
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
---

# INC-0539 - Two reviewers in a row were assigned a slice they had already worked on, because the pick did not search the record

**Cost:** Two review cycles ended at the independence check with no review; a third reviewer was needed.

## Signature - how you recognise it

A reviewer is picked from availability alone and then stops at the author check.

## What happened

The lead assigned a review to one reviewer, who stopped because they had written cases for the slice, and then to a second, who stopped because they had judged cases for it in an earlier commit. Both stops were correct. The lead then searched commits and reviews for the row first, found an earlier audit that only cited the row, applied the rule that a citation-only audit does not conflict while case or oracle judgment does, excluded the authors, and picked a third reviewer with the findings handed over.

## Root cause

The pick checked who was free, not who had touched the row.

## Why it was hard to see

The history of who wrote or judged a row is spread over several commits and review files.

## Fix

Search commits and reviews for the row before picking, and hand the chosen reviewer what was found.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before assigning a reviewer, search the record for every earlier author or judge of the row and pass the findings to the reviewer.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
