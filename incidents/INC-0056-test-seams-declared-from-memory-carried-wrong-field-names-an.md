---
id: INC-0056
title: Test seams declared from memory carried wrong field names, and a bulk replacement silently missed a row
date: 2026-10-28
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0056 - Test seams declared from memory carried wrong field names, and a bulk replacement silently missed a row

**Cost:** A test oracle named two design fields without their required prefix. A test author working from it would have written tests against fields that do not exist, which fail or pass vacuously depending on the framework.

## Signature - how you recognise it

A test oracle or interface section lists identifiers that nobody has searched for in the design, and the document has had bulk edits applied by script.

## What happened

A draft oracle declared its seams (field names and signatures) from the author's memory of the design, dropping a prefix on two fields. A later string-replacement edit also missed one row because of letter case.

## Root cause

Identifiers were recalled rather than copied. A near-miss name reads as correct to the author who recalls it. The bulk edit assumed that the replacement hit every intended row without counting.

## Why it was hard to see

A wrong name looks right to its author, and a silently missed replacement leaves a document that is still well formed.

## Fix

Every field name and signature in the oracle was searched for in the design before it was kept. Edit scripts assert the expected match count for each replacement and report all mismatches in one pass.

## Verification

The author's search of the design caught the names while revising, and a per-replacement match-count check caught the case-sensitivity miss.

## Transferable rule

> Search for every identifier you put into a test oracle; never declare a seam from memory. Make each bulk replacement assert its expected match count.

## Related

[INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) [INC-0051](./INC-0051-a-fallible-edit-script-followed-by-a-semicolon-let-the-commi.md)
