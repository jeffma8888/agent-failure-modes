---
id: INC-0439
title: A generated down migration dropped a table with cascade and then dropped the removed constraint again
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0439 - A generated down migration dropped a table with cascade and then dropped the removed constraint again

**Cost:** The defect was caught at review before any round trip.

## Signature - how you recognise it

A down migration contained a statement that fails after an earlier statement had already removed its target.

## What happened

a generated down migration dropped the media table with cascade, which already removes the referencing foreign key, and then dropped that same constraint, so the down step would fail with constraint does not exist; the lead sanctioned a hand edit of that one statement to drop the constraint only if it exists, recorded the raw and delivered hashes, and treated the fix as static until a round trip crosses it

## Root cause

the generator emits a cascade drop and an explicit constraint drop for the same object

## Why it was hard to see

The up path worked, and the down path is rarely run.

## Fix

change only the named statement, record raw and delivered hashes, and report the fix as static until a real round trip proves it

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Fix a generated down migration by a minimal named edit with raw and delivered hashes, and report it as static until a round trip proves it

## Related

[INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) [INC-0267](./INC-0267-a-check-named-lint-can-write.md) [INC-0448](./INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md)
