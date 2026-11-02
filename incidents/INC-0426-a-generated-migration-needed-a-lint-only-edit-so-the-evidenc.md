---
id: INC-0426
title: A generated migration needed a lint-only edit, so the evidence carries the raw and delivered hashes and the one-line diff
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0426 - A generated migration needed a lint-only edit, so the evidence carries the raw and delivered hashes and the one-line diff

**Cost:** Minor: an unrecorded hand edit to a generated file could have hidden a real change.

## Signature - how you recognise it

A generated file failed lint while its content was correct.

## What happened

a generated migration failed lint on unused destructured names; the lead allowed removing only those names in the up and down functions, with the SQL, the snapshot and every other byte as generated, and required the evidence to record the raw and delivered hashes of the file and the one-line diff for each function

## Root cause

the generator emits names the lint rules reject

## Why it was hard to see

A hand edit to generated output looks like tampering unless the raw bytes are kept.

## Fix

edit a generated file only for the named lint defect, keep every other byte, and record the raw hash, the delivered hash and the diff in the evidence

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a generated file needs a lint-only edit, change only the named defect and record the raw hash, the delivered hash and the diff

## Related

[INC-0267](./INC-0267-a-check-named-lint-can-write.md) [INC-0182](./INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md) [INC-0439](./INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md) [INC-0448](./INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md) [INC-0455](./INC-0455-a-provenance-check-that-the-generator-can-never-satisfy-the.md)
