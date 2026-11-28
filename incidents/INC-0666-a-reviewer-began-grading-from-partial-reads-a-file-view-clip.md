---
id: INC-0666
title: A reviewer began grading from partial reads: a file view clipped in the middle and a criterion read only up to its waiver clause
date: 2026-11-26
classes: [observability, false-green]
severity: low
status: mitigated
topic: observability/missing-or-unverifiable-receipts
occurrences: 1
---

# INC-0666 - A reviewer began grading from partial reads: a file view clipped in the middle and a criterion read only up to its waiver clause

**Catalog:** [root](../catalog/README.md) / [observability](../catalog/observability/README.md) / [Missing evidence keeps findings unverified](../catalog/observability/missing-or-unverifiable-receipts.md)

**Cost:** No wrong finding reached an author; one clipped file re-read in ranges and two provisional grades redone inside the two reviews.

## Signature - how you recognise it

A file view shows an omission marker in the middle, or a grade is written for a criterion or section before its last clause and the requirement it cites have been read.

## What happened

Two document reviews on the same day each began from an incomplete read; this record covers both. In the first, the reviewer's file-view tool returned a file with about 15 KB elided from the middle, shown only by a characters-omitted marker, and the reviewer also classified an acceptance criterion before reading its trailing clause, which carried a waiver. In the second, a design reviewer marked a section clean before opening the requirement that the section claimed to satisfy. In all three cases the reviewer noticed before issuing findings, read the missing text and regraded.

## Root cause

A grade was formed from the part of the text already in view, and nothing forced a check that the view was complete: the tool clips with only a marker, and a criterion or section looks finished before its qualifier or its cited requirement is read.

## Why it was hard to see

A clipped view still begins and ends correctly, so it reads as the whole file unless the marker is noticed. A waiver at the end of a criterion and a requirement in another document both sit outside the lines that prompted the grade.

## Fix

Before grading, compare what was read with the file's size and re-read in ranges until nothing is omitted; grade a criterion only after its final clause; open every requirement a section claims to satisfy before writing clean.

## Verification

Each slip was caught by the reviewer in the same run (the omission marker, a re-read to the end of the line, a re-check of the cited requirement) and the grade was redone. Not checked: whether any other clipped read went unnoticed, or whether the rule prevents recurrence.

## Transferable rule

> Never grade from a partial read: if a view shows an omission marker or fewer bytes than the file holds, re-read in ranges until it is whole; read each criterion to its last clause, and open every requirement a section claims to satisfy, before writing a verdict on it.

## Related

[INC-0515](./INC-0515-a-rulings-file-grew-past-what-a-reader-s-tool-returns-and-a.md)
