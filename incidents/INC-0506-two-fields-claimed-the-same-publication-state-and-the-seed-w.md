---
id: INC-0506
title: Two fields claimed the same publication state, and the seed wrote only one, so the admin and the public predicate disagreed
date: 2026-11-02
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0506 - Two fields claimed the same publication state, and the seed wrote only one, so the admin and the public predicate disagreed

**Cost:** Seeded records showed as drafts in the admin while the public predicate treated them as published; found by a read-only database inspection.

## Signature - how you recognise it

An application status says published and the framework draft status says draft for the same record.

## What happened

An application status field and the framework own draft status both claimed to say whether a record is published. The seed wrote the application status as published and never set the framework status, so the admin showed drafts with a publish action while the public predicate, which reads only the application status, matched the same records. The database held rows with the pair published and draft, and rows with draft and draft.

## Root cause

Nothing tied the two fields together, and the seed wrote one directly instead of using the framework transition that sets both.

## Why it was hard to see

Each field is correct on its own terms, and each reader sees a consistent answer from the field it reads.

## Fix

Write the seed through the framework supported publish transition so both fields change together, and assert both fields for seeded records in the same test.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When two fields can claim one state, derive one from the other or assert both in the same test, and write through the framework supported transition.

## Related

[INC-0448](./INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md)
