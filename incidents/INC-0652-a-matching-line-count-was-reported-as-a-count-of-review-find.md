---
id: INC-0652
title: A matching-line count was reported as a count of review findings
date: 2026-11-23
classes: [false-green, tooling-paths]
severity: low
status: fixed
topic: false-green/count-or-total-computed-wrong
occurrences: 1
---

# INC-0652 - A matching-line count was reported as a count of review findings

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A reported count, total or ledger does not match what ran](../catalog/false-green/count-or-total-computed-wrong.md)

**Cost:** The initial report understated nine blocking occurrences as six; a corrected recount resolved it, with no time estimate recorded.

## Signature - how you recognise it

A report labels `rg -c` output as occurrences even though several target matches share a line.

## What happened

The lead reported six blocking findings by using `rg -c`, which counts lines containing a match, not the total number of matches. A second count with `rg -o` piped into `wc -l` found nine occurrences, agreeing with the author count.

## Root cause

The counting command measured a different unit from the one stated in the report, and the count was not cross-checked before communication.

## Why it was hard to see

The command returns a plausible integer without an error. Unless two findings fall on the same line or a second counting method is run, matching lines and matches look equivalent.

## Fix

Use an occurrence-producing command when reporting occurrences, independently recount the result, and label reports with the measured unit.

## Verification

A recount produced nine occurrences versus six matching lines, consistent with the author count. Not checked in the input: whether the corrected method is used on future reports.

## Transferable rule

> When reporting matches, count individual occurrences with `rg -o ... | wc -l`, not matching lines with `rg -c`; state the unit and cross-check the count before a verdict.

## Related

[INC-0070](./INC-0070-two-reviewers-table-parsers-undercounted-rows-on-escaped-pip.md) [INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md)
