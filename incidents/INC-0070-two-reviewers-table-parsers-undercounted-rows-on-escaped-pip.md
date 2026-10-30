---
id: INC-0070
title: Two reviewers' table parsers undercounted rows on escaped pipes and a sum included a header
date: 2026-10-29
classes: [false-green, tooling-paths]
severity: low
status: fixed
---

# INC-0070 - Two reviewers' table parsers undercounted rows on escaped pipes and a sum included a header

**Cost:** Two reviewers' first counts of a plan's rows were wrong. Each caught its own error before reporting, so no false verdict was issued.

## Signature - how you recognise it

A count or sum of table rows comes from splitting lines on the column delimiter, and some cells contain the delimiter escaped.

## What happened

Both reviewers first counted a plan's rows by splitting markdown table lines on the pipe character, which also splits on escaped pipes inside cells, so one row was undercounted. One reviewer's effort sum also included a header line.

## Root cause

Table syntax was treated as plain text. A naive split cannot see escaping, and an unfiltered aggregate cannot see that a line is not a data row.

## Why it was hard to see

The result is plausible and off by one. Nothing errors, and an undercount of a single row looks like a disagreement with the plan, not with the parser.

## Fix

Use escape-aware splitting (a negative lookbehind for the backslash) and filter the aggregate to numeric rows.

## Verification

After the fix both reviewers' counts matched the plan's 102 rows and its totals.

## Transferable rule

> Parse table syntax properly before reporting a count, and cross-check any count or sum against a second method before it reaches a verdict.

## Related

[INC-0029](./INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)
