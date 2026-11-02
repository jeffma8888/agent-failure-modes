---
id: INC-0387
title: One review asked to delete an error-text assertion while another asked to pin the text
date: 2026-11-01
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0387 - One review asked to delete an error-text assertion while another asked to pin the text

**Cost:** Two reviews pulled a test in opposite directions until a single rule settled both.

## Signature - how you recognise it

Two reviews gave opposite instructions about the same assertion.

## What happened

one review asked to delete an error-text assertion while a second review asked to pin the text; the lead resolved both by pinning an error name and banning message-text oracles

## Root cause

message text was used as the oracle, so it was both brittle and the thing one review wanted pinned

## Why it was hard to see

Each review was right on its own terms, and only a common oracle satisfied both.

## Fix

Pin an error name or code; do not use message text as an oracle

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Pin an error name, never message text, as the oracle

## Related

[INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) [INC-0374](./INC-0374-a-clause-survival-script-flagged-21-digest-rules-that-a-word.md)
