---
id: INC-0661
title: An early review checkpoint held headings but no findings
date: 2026-11-25
classes: [checkpoint]
severity: low
status: mitigated
topic: null
occurrences: 1
---

# INC-0661 - An early review checkpoint held headings but no findings

**Catalog:** [root](../catalog/README.md) / [checkpoint](../catalog/checkpoint/README.md)

**Cost:** One review reached context compaction without saved findings; in a second review, roughly ten checks were exposed before the first substantive save. No permanent loss was reported.

## Signature - how you recognise it

A review file exists early, but it still contains only headings after several checks have been completed.

## What happened

In one review, the reviewer noticed after a context compaction that no checked items or findings had been added to the outline. In a second review, the reviewer ran roughly ten checks before saving any results despite an instruction to save every few checks. The two reviews exposed the same gap: the presence of a file did not mean the work was recoverable from it.

## Root cause

The checkpoint was treated as a one-time file creation rather than a recurring save of completed work.

## Why it was hard to see

An outline satisfies a quick existence check, but a fresh reader cannot tell which items were checked or what they showed.

## Fix

Append findings as they are confirmed and save completed checks in small batches, including checks that produced no finding.

## Verification

The reviewers noticed the missing or delayed entries in their own runs. Recovery after a killed run and compliance with the new cadence were not tested.

## Transferable rule

> Checkpoint completed checks and findings on disk every few checks or after a finding; do not count an outline with no results as a progress checkpoint.
