---
id: INC-0100
title: A new test file was placed in a row whose activation order did not include a collection the file creates, and an oracle was asserted without its spec sentence
date: 2026-10-30
classes: [spec-and-scope]
severity: medium
status: fixed
---

# INC-0100 - A new test file was placed in a row whose activation order did not include a collection the file creates, and an oracle was asserted without its spec sentence

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A test creates a collection or relies on a rule that the row order or spec does not support.

## What happened

A new test file was placed before the row that activates a collection the file creates, and an oracle was asserted without finding the exact spec sentence.

## Root cause

Placement was chosen by topic and the oracle from memory.

## Why it was hard to see

The file looks right by name and the assertion looks plausible.

## Fix

Check the row activation order includes every collection the file creates, and find the exact spec sentence before asserting an oracle.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Place tests by activation order and quote the spec before asserting.

## Related

[INC-0089](./INC-0089-a-qa-question-claimed-a-credential-or-fact-was-undefined-whe.md)
