---
id: INC-0061
title: Exhaustive test wording created expectations the design never defined
date: 2026-10-29
classes: [false-green, spec-and-scope]
severity: medium
status: mitigated
---

# INC-0061 - Exhaustive test wording created expectations the design never defined

**Cost:** A test requirement demanded invented values. Two independent reviewers caught it in a late review round; the fix was queued for a further revision.

## Signature - how you recognise it

A test requirement says 'every' member of a set, and the source of truth defines behaviour for only some of them.

## What happened

A revision widened an error-mapping test to cover every error code. The design maps only six codes to transport statuses, so for the rest the oracle would have required statuses nobody had decided.

## Root cause

Universal quantification added in a fix for coverage, without checking that the source of truth covers every member. The test turned an absence in the design into an assertion.

## Why it was hard to see

'Every' reads as the thorough choice, and a reviewer sees a stricter test. The mismatch is only visible by comparing the set against the design's table.

## Fix

Narrow the matrix to the explicitly mapped codes, or add the missing mappings to the design first, then test them.

## Verification

Two reviewers independently compared the test's set with the design's mapping table.

## Transferable rule

> A per-ID test oracle may only require values its source of truth defines. 'Every' in a test requirement needs a check that the source covers every member.

## Related

[INC-0057](./INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md) [INC-0056](./INC-0056-test-seams-declared-from-memory-carried-wrong-field-names-an.md)
